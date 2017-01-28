#!/usr/bin/env python3
import sys
from itertools import islice


def solve(n):
    return sum(islice(fib(n), 2, None, 3))


def fib(limit):
    predecessor = 0
    current = 1
    while current < limit:
        yield current
        temp = current
        current = current + predecessor
        predecessor = temp


# ========================================= boilerplate ========================================== #

def main(cases):
    return '\n'.join([str(solve(int(case))) for case in cases])


if __name__ == '__main__':
    print(main(sys.stdin.readlines()[1:]))
