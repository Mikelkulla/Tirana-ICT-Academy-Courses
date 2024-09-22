import sqlite3

# Step 1: Connection to the database that check the access to the file
conn = sqlite3.connect("emaildb.sqlite")
# Step 2: Cursor is like a handle
cur = conn.cursor()
# we drop the table if it exists
cur.execute("DROP TABLE IF EXISTS Counts")

cur.execute("CREATE TABLE Counts (email TEXT, count INTEGER)")

fname = input("Enter file name:")
if (len(fname) < 1):
    fname = "mbox-short.txt"
fh = open(fname)
for line in fh:
    if not line.startswith("From: "): continue
    pieces = line.split()
    email = pieces[1]
    # we are opening a set of record and are going to know if this is true
    cur.execute("SELECT count FROM Counts WHERE email = ? ", (email,))
    # we grab the first one and give it to row, row is going to be the info we get from the DB
    row = cur.fetchone()
    if row is None:
        cur.execute("INSERT INTO Counts (email, count) VALUES (?, 1)", (email,))
    else:
        cur.execute("UPDATE Counts SET count = count + 1 WHERE email = ?", (email,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = ("SELECT email, count FROM Counts ORDER BY count DESC LIMIT 20")

for row in cur.execute(sqlstr):
    print(row[0], row[1])
cur.close()