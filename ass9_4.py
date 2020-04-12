#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
for i in handle:
    x = i.split()
    if len(x) < 2:
        continue
    if x[0] == 'From':
        counts[x[1]] = counts.get(x[1],0) + 1

maxmail = None
maxcount = None
for k,v in counts.items():
    if maxcount == None or v > maxcount:
        maxcount = v
        maxmail = k
print(maxmail,maxcount)