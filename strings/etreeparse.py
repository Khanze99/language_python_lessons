from xml.etree.ElementTree import parse

tree = parse('books.xml')
for E in tree.findall('title'): print(E.text)
