inp = input('enter file name')
fhand = open(inp)
list1 = list()
count = 0
for line in fhand:
    if line.startswith('From:'):
        continue
    elif line.startswith('From'):
        count = count + 1
        list2 = line.split()
        address = list2[1]
        list1.append(address)
for x in list1:
    print(x)
print("There were", count, "lines in the file with From as the first word")
