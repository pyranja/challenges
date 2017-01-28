#!/usr/bin/env python3
import sys, logging

"""find fixed-length subsequence with max product within a number"""

def solve(n, k):
    logging.info("searching %d-digit subsequence in %s", k, n)
    digits = str(n)
    maximum = 0
    for position in range(k, len(digits)):
        current = sub_product(digits, position - k, position)
        maximum = current if current > maximum else maximum
    return maximum

def sub_product(n, start, stop):
    product = 1
    for i in range(start, stop):
        product *= int(n[i])
    logging.info("calculating sub product [%d..%d]|%s = %d", start, stop, n[start:stop], product)
    return product

# ========================================= boilerplate ========================================== #

def main(cases):
    return '\n'.join(str(solve(*case)) for case in cases)

def parse_cases(lines):
    for current, next in zip(lines[0::2], lines[1::2]):
        yield (next, int(current.split(' ')[1]))

if __name__ == '__main__':
    logging.basicConfig(level=logging.WARNING)
    print(main(parse_cases(sys.stdin.readlines()[1:])))
