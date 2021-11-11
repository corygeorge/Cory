fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for words in fh:
  for word in words.split():
      if not word in lst:
       lst.append(word)
       lst.sort()
print(lst)
