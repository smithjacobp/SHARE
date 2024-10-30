import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

#import stuff

url = 'http://py4e-data.dr-chuck.net/comments_1593678.xml'
hand = urllib.request.urlopen(url)
data = hand.read()
tree = ET.fromstring(data)

#import data

coms = tree.findall('comments/comment')

#this finds all of the comment within comments

total = 0
for comment in coms:
    counts = comment.find('count').text
    total = total + float(counts)
    
#we find the ocunts, we add up the counts, this is the only way which works, no idea why
    
print(total)
    
#there is no way of doing this based on the intructions or the code which was taught





    







