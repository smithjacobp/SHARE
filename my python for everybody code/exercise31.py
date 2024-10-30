h = input('enter hours')
r = input('enter pay rate')
hrs = float(h)
rt = float(r)
if hrs > 40:
    regpay = 40.0 * rt
    otp = (hrs - 40) * (1.5 * rt)
    total = regpay + otp
else:
    total = (hrs * rt)
print('Pay:', total)
# I don't know why I cannot understand word problems well, or maybe just math