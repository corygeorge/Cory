hrs = input('Enter Hours"')
h = float(hrs)
rph = input( 'Enter rph:')
r = float(rph)
if h <= 40 :
    grosspay = h*r
    print(grosspay)
elif h > 40:
    overtime = h-40
    grosspay = 40*r+(1.5*overtime*r)
print(grosspay)
