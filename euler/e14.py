#!/usr/bin/env python3
import sys
import logging

"""longest collatz sequence starting from a number <= a given N"""

MAX_N = 5 * 1000000

LOOKUP = [0] * (MAX_N + 1)


def solve(n):
    return LOOKUP[n]


CACHE = [0] * (MAX_N + 1)


def populate():
    max_start, max_length = 0, 0
    for it in range(1, MAX_N + 1):
        current_length = collatz_length(it)
        if current_length >= max_length:
            max_start, max_length = it, current_length
        LOOKUP[it] = max_start


def collatz_length(n):
    if n <= MAX_N and CACHE[n]:
        return CACHE[n]
    if n == 1:
        return 1
    if n % 2 == 0:
        length = collatz_length(n // 2)
    else:
        length = collatz_length(3 * n + 1)
    length += 1
    if n <= MAX_N:
        CACHE[n] = length
    return length

populate()

# ========================================= boilerplate ========================================== #

def main(cases):
    return '\n'.join([str(solve(int(case))) for case in cases])


if __name__ == '__main__':
    logging.basicConfig(level=logging.WARN)
    print(main(sys.stdin.readlines()[1:]))
