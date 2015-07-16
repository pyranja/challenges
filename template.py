#!/usr/bin/env python3
import sys


def solve(n):
    pass


# ========================================= boilerplate ========================================== #

def main(cases):
    return '\n'.join([str(solve(int(case))) for case in cases])


if __name__ == '__main__':
    print(main(sys.stdin.readlines()[1:]))
