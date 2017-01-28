#!/usr/bin/env python3
import sys, logging
from itertools import count

"""find smallest integer that is evenly divisible by each of some numbers 1..N"""

def solve(n):
    return next(x for x in count(n, n) if all(x % q == 0 for q in range(1, n)))

# ========================================= boilerplate ========================================== #

def main(cases):
    return '\n'.join([str(solve(int(case))) for case in cases])


if __name__ == '__main__':
    logging.basicConfig(level=logging.WARN)
    print(main(sys.stdin.readlines()[1:]))
