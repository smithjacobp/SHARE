# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
added = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        start = line.find(':')
        number = line[start + 1:]
        fnumber = float(number)
        added = added + fnumber
        avg = (added / count)
print('Average spam confidence:', avg)
