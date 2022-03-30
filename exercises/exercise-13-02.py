# Extracting Data from JSON
# The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:

import urllib.request
import json


url = input("Enter URL: ")
print("Retrieving", url, "...")
uhand = urllib.request.urlopen(url)
data = uhand.read()

info = json.loads(data)
print('User count:', len(info["comments"]))

lst = list()

for item in info["comments"]:
    lst.append(item["count"])

print("Sum:", sum(lst))
