# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
inp = fh.read()
inp2 = inp.upper()
inp3 = inp2.rstrip()
print(inp3)