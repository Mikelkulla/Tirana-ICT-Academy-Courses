import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('tracksdb.sqlite')
curr = conn.cursor()

# Make some fresh tables using executescript()
curr.executescript("""
DROP TABLE IF EXISTS Artists;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artists (
    id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id   INTEGER,
    title       TEXT UNIQUE
);

CREATE TABLE Track (
    id          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title       TEXT UNIQUE,
    album_id    INTEGER,
    len         INTEGER, 
    rating      INTEGER, 
    count       INTEGER
)
""")

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "Library.xml"


def lookup(d, key):
    found = False
    for child in d:
        if found:
            return child.text
        if child.tag == "key" and child.text == key:
            found = True
    return None


stuff = ET.parse(fname)
all = stuff.findall("dict/dict/dict")
print("Dict count:", len(all))
i = 1
for entry in all:
    if lookup(entry, "Track ID") is None:
        continue
    name = lookup(entry, "Name")
    artist = lookup(entry, "Artist")
    album = lookup(entry, "Album")
    count = lookup(entry, "Play Count")
    rating = lookup(entry, "Rating")
    length = lookup(entry, "Total Time")

    if name is None or artist is None or album is None:
        continue

    print(i, ":", name, artist, album, count, rating, length)
    i += 1
    curr.execute("""INSERT OR IGNORE INTO Artists (name) VALUES ( ? )""", (artist,))
    curr.execute("""SELECT id FROM Artists WHERE name = ( ? )""", (artist,))
    artist_id = curr.fetchone()[0]

    curr.execute("""INSERT OR IGNORE INTO Album (title, artist_id) VALUES ( ?, ?)""", (album, artist_id))
    curr.execute("SELECT id FROM Album WHERE title = ( ? )", (album,))
    album_id = curr.fetchone()[0]

    curr.execute("""INSERT OR REPLACE INTO Track (title, album_id, len, rating, count)
                    VALUES ( ?, ?, ?, ?, ?)""", (name, album_id, length, rating, count))
    conn.commit()
