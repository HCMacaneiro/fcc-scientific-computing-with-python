# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fname = input("Enter the name of the file: ")
try:
    fhand = open(fname)
except:
    print("File could not be opened", fname)
    quit()
msgperhour = dict()
for line in fhand:
    words = line.split()
    if line.startswith("From") and not line.startswith("From:"):
        time = words[5].split(":")
        hour = time[0]
        msgperhour[hour] = msgperhour.get(hour, 0) + 1
lst = list()
for k, v in msgperhour.items():
    newval = (k, v)
    lst.append(newval)
lst = sorted(lst)
for key, value in lst:
    print(key, value)
