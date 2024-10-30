name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
#using split and index values to extract counts of hours
#I could slpit the line before the if statement and used if words[0] == 'From '
counts = dict()
for line in handle:
    line.rstrip()
    if line.startswith('From '):
        words = line.split()
        hours = words[5].split(':')
        counts[hours[0]] = counts.get(hours[0], 0) + 1
    else:
        continue
#sort and print the counts of hours
for k, v in sorted(counts.items()):
    print(k, v)
    
    
    
    