#!/usr/bin/env python3
import sys, logging

"""calculate digit sums of powers of two"""

def solve(n):
    return sum(int(digit) for digit in str(2 ** n))


# ========================================= boilerplate ========================================== #

def main(cases):
    return '\n'.join([str(solve(int(case))) for case in cases])


if __name__ == '__main__':
    logging.basicConfig(level=logging.WARN)
    print(main(sys.stdin.readlines()[1:]))
