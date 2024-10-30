import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
url = input('enter url')
count = int(input('enter count'))
pos = int(input('enter position'))

#do imports and define inputs
#counts is the number of iterations
#pos is the position of the link

for ind in range(count):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    
#open the links and parse the content of the links 
#do this count number of times

    atags = soup('a')
    urllst = list()
    ataglst = list()
    for atag in atags:
        url2 = atag.get('href', None)
        urllst.append(url2)
        lnk = atag.decode()
        ataglst.append(lnk)
    
#find the anchor tags which are links   
#get the urls from the links and put them in a list in byte format
#make a list of the anchor tags in str format
    
    print(urllst[pos - 1])
    print(ataglst[pos - 1])
    url = urllst[pos - 1]
    
#print the last url in byte format
#print last anchor tag in str format
#put the last url in byte format into the url input
    