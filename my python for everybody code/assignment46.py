def computepay(h = input('enter hours'), r = input('enter rate')):
    hrs = float(h)
    rt = float(r)
    if hrs > 40:
        regpay = 40.0 * rt
        otp = (hrs - 40) * (1.5 * rt)
        total = regpay + otp
    else:
        total = (hrs * rt)
    return print('Pay', total)
computepay()
