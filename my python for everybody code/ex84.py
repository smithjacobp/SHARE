# I have to create a new list
list1 = list()
inp = input('enter file name')
fhand = open(inp)
for line in fhand:
    words = line.split()
    for word in words:
        if word in list1:
            continue
        if word not in list1:
            list1.append(word)
list1.sort()
print(list1)
    
