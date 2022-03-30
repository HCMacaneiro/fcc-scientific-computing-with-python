import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET


count = 0

url = input('Enter URL: ')
urlhand = urllib.request.urlopen(url)
data = urlhand.read()
tree = ET.fromstring(data)

alltags = tree.findall('.//count')

for tag in alltags:
        count += int(tag.text)

print('Receiving',len(data),'characters')
print('Count:',len(alltags))
print('Sum:',count)
