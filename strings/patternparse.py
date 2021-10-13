import re


text = open('books.xml').read()
found = re.findall('<title>(.*)</title>', text)
for title in found: print(title)