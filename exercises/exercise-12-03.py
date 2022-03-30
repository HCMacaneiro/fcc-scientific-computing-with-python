import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup


url = input('Enter - ')
count = int(input("Enter count: "))
position = int(input("Enter position: "))


# Retrieve all of the anchor tags
for i in range(count):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    lst = list()
    for tag in tags:
        lst.append(tag.get('href', None))
    url = lst[position - 1]
    print(url)
