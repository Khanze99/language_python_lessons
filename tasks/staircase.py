import math
import os
import random
import re
import sys


# Complete the staircase function below.
def staircase(n):
    string_result = ''
    for i in enumerate(reversed(range(1, n + 1))):
        string_result += ' ' * i[1] + '#' * i[0] + '\n'

    return string_result


if __name__ == '__main__':
    n = int(input())

    print(staircase(n))
