#!/usr/bin/env python3
import sys, logging

"""calculate difference between sum of squares and square of sum of first 1..N numbers"""

def solve(n):
    squared_sum = ((n * (n + 1)) // 2) ** 2
    sum_of_squares = (n * (n + 1) * (2 * n + 1)) // 6
    return squared_sum - sum_of_squares


# ========================================= boilerplate ========================================== #

def main(cases):
    return '\n'.join([str(solve(int(case))) for case in cases])


if __name__ == '__main__':
    logging.basicConfig(level=logging.WARN)
    print(main(sys.stdin.readlines()[1:]))
