text = "X-DSPAM-Confidence:    0.8475"
start = text.find('0')
end = text.find('5')
number = text[start : end + 1]
fnumber = float(number)
print(fnumber)
#the end could have just been no input as the second index value