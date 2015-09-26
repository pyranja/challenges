#!/usr/bin/env python3
import sys, logging
from math import factorial

"""find number of ways through NxM grid moving only right and down"""

# a way through the grid is a combination of N right moves and M down moves
# all possible combinations are given by the multinomial coefficient
#   (N + M)! / N! * M!

REDUCE_FACTOR = 10 ** 9 + 7

def solve(n, m):
    combinations = factorial(n + m) // (factorial(n) * factorial(m))
    logging.info("%d x %d ==> %d", n, m, combinations)
    return combinations % REDUCE_FACTOR


# ========================================= boilerplate ========================================== #

def main(cases):
    return '\n'.join([str(solve(int(n), int(m))) for n, m in (line.split(' ') for line in cases)])


if __name__ == '__main__':
    logging.basicConfig(level=logging.WARN)
    print(main(sys.stdin.readlines()[1:]))
