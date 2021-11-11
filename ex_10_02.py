name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith ('From'):continue
    words = line.split()
    #guardian in a compound statement
    if len(words)< 3 or words[0] != 'From':
        continue
    #print(words[5])
    tsplit = words[5].split(':')[0]
    #print(tsplit)
    hour = tsplit
    counts[hour]=counts.get(hour,0)+1
#print(counts)
t=sorted(counts.items())
for key,val in sorted(counts.items()):
    print (key,val)
