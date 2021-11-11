text = "X-DSPAM-Confidence:    0.8475"
atpos= text.find(':')
#print(atpos)
ntext=text[19:30]
fntext = float(ntext)
print(fntext)
#---------OR---------------------------
text = "X-DSPAM-Confidence:    0.8475"
ipos= text.find(':')
#print(ipos)
piece=text[ipos+1:]
print(piece)
fpiece = float(piece)
print(fpiece)
