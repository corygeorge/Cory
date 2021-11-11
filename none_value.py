smallest = None
largest = None
while True:
    value = input ("Enter Value:")
   if value == "done":
        break
    try:
        fvalue = float(value)
    except:
        print ('Invalid input')
        continue

    if largest is None:
       largest = fvalue
    elif fvalue > largest:
       largest = fvalue

    if smallest is None:
        smallest = fvalue
    elif fvalue < smallest:
        smallest = fvalue
    #print (smallest,value)

print (largest)
print (smallest)
