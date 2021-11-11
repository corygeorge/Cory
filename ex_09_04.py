fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)
counts = dict()
for line in fh:
    if not line.startswith('From:'):continue
    words =line.split()[1]
    #print(words)
    counts[words]= counts.get(words,0)+1
#print(counts)
bigcount = None
bigword  = None
for word,counts in counts.items():
    if bigcount is None or counts > bigcount:
        bigword = word
        bigcount = counts

print(bigword,bigcount)
