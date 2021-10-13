# -*- coding: latin-1 -*-
import sys

myStr1 = 'AÄBèC'
myStr2 = 'A\u00c4B\U000000e8C'
myStr3 = 'A' + chr(0xC4) + 'B' + chr(0xE8) +'C'

print('Default encoding:', sys.getdefaultencoding())

for s in myStr1, myStr2, myStr3:
    print('{0}, strlen={1}, '.format(s, len(s)), end='')

    bytes1 = s.encode()
    bytes2 = s.encode('latin-1')

    print('byteslen1={0}, byteslen2={1}'.format(len(bytes1), len(bytes2)))


open()