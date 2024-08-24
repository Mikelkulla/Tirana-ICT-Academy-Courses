from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certifications errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter - ")
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all the anchore tags
tags = soup("a")
for tag in tags:
    print(tag.get("href", None))