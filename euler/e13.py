#!/usr/bin/env python3
import sys
import logging

"""Work out the first ten digits of the sum of N 50-digit numbers.

Input Format
First line contains N, next N lines contain a 50 digit number each.

Output Format
Print only first 10 digit of the final sum

Constraints
1 <= N <= 103"""


def solve(n):
    return ''.join(str(sum(n))[0:10])


# ========================================= boilerplate ========================================== #

def main(cases):
    return str(solve([int(case) for case in cases]))


if __name__ == '__main__':
    logging.basicConfig(level=logging.WARN)
    print(main(sys.stdin.readlines()[1:]))
