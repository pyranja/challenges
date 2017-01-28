#!/usr/bin/env python3
import sys, math


def solve(n):
    return max(factorize(n))


def factorize(it):
    assert it > 0, "cannot factorize %s" % it
    yield 1
    factor = 2
    limit = int(math.sqrt(it))  # if no divisor < sqrt(it) found it is a prime
    while (it > 1):
        if it % factor == 0:
            yield factor
            it = it // factor
            limit = int(math.sqrt(it))
        elif factor > limit:
            factor = it # it is a prime, shortcut and use itself as last factor
        else:
            factor += 1


# ========================================= boilerplate ========================================== #

def main(cases):
    return '\n'.join([str(solve(int(case))) for case in cases])


if __name__ == '__main__':
    print(main(sys.stdin.readlines()[1:]))
