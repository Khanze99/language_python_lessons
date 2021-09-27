import pybench
import sys

pythons = [
    (1, "python3"),
    (0, "python2"),
    (0, "./pypy3.7/bin/pypy")
]

stmts = [
    (0, 0, "[x ** 2 for x in range(1000)]"),
    (0, 0, "res = []\nfor x in range(1000): res.append(x ** 2)"),
    (0, 0, "$listif3(map(lambda x: x ** 2, range(1000)))"),
    (0, 0, "list(x ** 2 for x in range(1000))"),
    (0, 0, "s = 'spam' * 2500\nx = [s[i] for i in range(10000)]"),
    (0, 0, "s = '?'\nfor i in range(1000): s += '?'")
]

tracecmd = '-t' in sys.argv
pythons = pythons if '-a' in sys.argv else None
pybench.runner(stmts, pythons, tracecmd)