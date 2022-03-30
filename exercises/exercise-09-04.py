# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print("File could not be opened:", fname)
    quit()
senders = dict()
for line in fhand:
    words = line.split()
    if line.startswith("From") and not line.startswith("From:"):
        senders[words[1]] = senders.get(words[1], 0) + 1
maxword = None
maxcount = None
for word, count in senders.items():
    if maxcount is None or count > maxcount:
        maxword = word
        maxcount = count
print(maxword, maxcount)
