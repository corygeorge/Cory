largest = None
smallest = None
while True:
   value = input ("Enter Value:")
   if value == "done":
        break
   try:
        ivalue = int(value)
   except:
        print ('Invalid input')
        continue

   if largest is None:
       largest = ivalue
   elif ivalue > largest:
       largest = ivalue

   if smallest is None:
        smallest = ivalue
   elif ivalue < smallest:
        smallest = ivalue
    #print (smallest,value)

print ('Maximum is', largest)
print ('Minimum is', smallest)
