
import urllib.request, urllib.parse, urllib.error
import json

url = 'http://py4e-data.dr-chuck.net/comments_1593679.json'
hand = urllib.request.urlopen(url)
data = hand.read().decode()
info = json.loads(data)

thing = info['comments']
         
#this gives me a list of comments
         
x = list()
for com in thing:
    x.append(com['count'])
    
#this gives me a list of counts
    
print(sum(x))
         
         

