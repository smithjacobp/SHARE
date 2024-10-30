hand = open('regex.txt')
import re
numlist = list()
for line in hand:
    nums = re.findall('[0-9]+', line)
    numlist = numlist + nums
#I cannot use append and I need an empty list no idea why
newlist = list()
for st in numlist:
    newlist.append(int(st))
print(sum(newlist))
#now I can use append no idea why
