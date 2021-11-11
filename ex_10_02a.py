fname = input ('Enter File:')
if len(fname) < 1 : fname = 'clown.txt'
hand = open (fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
    # idiom: retrieve/create/update counter
        di[w] = di.get(w,0) + 1

#print(di)
tmp = list()
for k,v in di.items():
    newt = (v,k)

# print('Flipped',tmp)
tmp = sorted(tmp,reverse=Time)
# print ('Sorted',tmp[:5])

for v,k in temp[:5]:
    print(k,v)       
