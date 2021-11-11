# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total=0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        line = line.strip()
        count = count+1
        ipos= line.find(':')
        piece=line[ipos+2:]
        fpiece = float(piece)
        total = total + fpiece
        #print(count,total,fpiece)
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
print('Average spam confidence:',total/count)
