from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

spans = soup('span')
import re
numlist = list()

for span in spans:
    thing = span.decode()
    nums = re.findall('[0-9]+', thing)
    numlist = numlist + nums

newlist = list()

for st in numlist:
    newlist.append(int(st))
print(sum(newlist))