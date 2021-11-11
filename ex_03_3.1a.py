hrs = input('Enter Hours:')
h = float(hrs)
rph = input( 'Enter rph:')
r = float(rph)
if h > 40 :
    reg = 40*r
    overtime = (h-40) * (r*1.5)
    otpay = reg + overtime
    print(otpay)
else :
    reg = h*r
    print(reg)
