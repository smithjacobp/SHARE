fname = input("Enter file:")
fhand = open(fname)
counts = dict()
for line in fhand:
    line.rstrip()
    if line.startswith('From '):
        words = line.split()
        counts[words[1]] = counts.get(words[1], 0) + 1
    else:
        continue
maxcount = None
maxperson = None
for person, count in counts.items():
    if maxcount is None or count > maxcount:
        maxcount = count
        maxperson = person
print(maxperson, maxcount)
#use line.rstrip to ignore blank lines
#I overcomplicated it before all the count logic can be in one line

    

        














