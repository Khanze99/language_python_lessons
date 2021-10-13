import xml.sax.handler


class BookHandler(xml.sax.handler.ContentHandler):

    def __init__(self):
        self.in_title = False
        super(BookHandler, self).__init__()

    def startElement(self, name, attrs):
        if name == 'title':
            self.in_title = True

    def characters(self, content):
        if self.in_title:
            print(content)

    def endElement(self, name):
        if name == 'title':
            self.in_title = False


import xml.sax

parser = xml.sax.make_parser()
handler = BookHandler()
parser.setContentHandler(handler)
parser.parse('books.xml')
