num = 0
tot = 0.0
while True:
    sval = input('enter a number')
    if sval == 'done' :
        break
    try:
        fval = float(sval)
    except: 
        print('invalid input')
        continue
    num = num + 1
    tot = tot + fval
print(tot, num, (tot / num))
#break is used to end the code if done is entered
#continue is used so the code can continue after invalid input