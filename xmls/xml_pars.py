from lxml.etree import iterparse
from inspect import cleandoc


def parse_and_remove(filename, path):
    path_parts = path.split('/')
    doc = iterparse(filename, ('start', 'end'))

    tag_stack = []
    elem_stack = []

    for event, elem in doc:
        if event =='start':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event == 'end':
            yield elem
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
                pass


if __name__ == '__main__':
    for elem in parse_and_remove('GKUZU.xml', 'MP/Package/FormParcels/NewParcel/CadastralBlock'):
        print(cleandoc(elem.text))
