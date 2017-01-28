#!/usr/bin/env python3
import sys


def solve(n):
    return arithmetic_series(3, n) + arithmetic_series(5, n) - arithmetic_series(15, n)


def arithmetic_series(d, n):
    top = n - (n % d)
    return (d + top) * (n // d) // 2


# ========================================= boilerplate ========================================== #

def main(cases):
    return '\n'.join([str(solve(int(case))) for case in cases])


if __name__ == '__main__':
    print(main(sys.stdin.readlines()[1:]))
