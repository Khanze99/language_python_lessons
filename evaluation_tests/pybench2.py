import sys
import timeit
import os

defnum, defrep = 1000, 5


def runner(stmts, pythons=None, tracecmd=False):
    for number, repeat, setup, stmt in stmts:
        number = number or defnum
        repeat = repeat or defrep

        if not pythons:
            ispy3 = sys.version[0] == '3'
            stmt = stmt.replace('$listif3', 'list' if ispy3 else '')
            best = min(timeit.repeat(
                setup=setup, stmt=stmt, number=number, repeat=repeat
            ))
            print('%.4f [%r]' % (best, stmt[:70]))
        else:
            print('-' * 80)
            print('[%r]' % stmt)

            setup = setup.replace('\t', ' ' * 4)
            setup = ' '.join('-s "%s"' % line for line in setup.split('\n'))

            for ispy3, python in pythons:
                stmt1 = stmt.replace('$listif3', 'list' if ispy3 else '')
                stmt1 = stmt1.replace('\t', ' ' * 4)
                lines = stmt1.split('\n')
                args = ' '.join('"%s"' % line for line in lines)
                cmd = '%s -m timeit -n %s -r %s %s %s' % (python, number, repeat, setup, args)
                print(python)
                if tracecmd: print(cmd)
                print('\t' + os.popen(cmd).read().rstrip())