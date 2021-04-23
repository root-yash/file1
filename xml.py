from urllib.request import urlopen
import xml.etree.ElementTree as et

html = urlopen("http://py4e-data.dr-chuck.net/comments_1183807.xml").read()
tree=et.fromstring(html)
tree=tree.findall("comments/comment")
c=0
for t in tree:
    c=int(t.find('count').text)+c
print(c)