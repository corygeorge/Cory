def computepay(h, r):
    h = float(hrs)
    r = float(rph)
    if h > 40 :
        reg = 40*r
        overtime = (h-40) * (r*1.5)
        otpay = reg + overtime
        return otpay
    else :
        reg = h*r
        return reg

hrs = input("Enter Hours:")
h = float(hrs)
rph = input( 'Enter rph:')
r = float(rph)
p = computepay(float(h), float(r))
print("Pay", p)
