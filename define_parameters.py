#parameters
def greet(p1):
    if p1 == "es":
        print('Hola')
    elif p1 == 'fr':
        print ('Bonjour')
    else :
        print ('Hello')

greet('es')
greet('fr')
greet('p1')

#return values
def greet():
    return"hello"
print (greet () , "Glen")
print (greet() , "Sally")


# both
def greet(p1):
    if p1 == "es":
        return('Hola')
    elif p1 == 'fr':
        return('Bonjour')
    else :
        return ('Hello')

print (greet('es'),"Sally")
print (greet('en'),"Glenn")
print (greet('fr'),"Micheal")


#multiple parameters
def addtwo(a,b):
    added = a+b
    return added

x = addtwo (3,5)
print (x)
