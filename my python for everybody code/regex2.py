hand = open('regex.txt')
import re
numlist = list()
for line in hand:
    numlist = numlist + re.findall('[0-9]+', line)
newlist = list()
for st in numlist:
    newlist.append(int(st))
print(sum(newlist))