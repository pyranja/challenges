#!/usr/bin/env python3
import sys, logging, math

"""
largest palindrome product

Find the largest palindrom below a given N, that is a product of two 3-digit numbers.
101 101 < N < 1 000 000
"""


def solve(n):
    return next(x for x in palindromes_below(n) if is_product_of_two_three_digit_numbers(x))


def append_reversed_tail(it):
    return it * 1000 + int(str(it)[::-1])


def palindromes_below(max):
    """yield 6-digit palindroms smaller than given maximum in descending order"""
    prefix = max // 1000    # valid cut, max is always 6 digit
    palindrome = append_reversed_tail(prefix)
    if palindrome < max:    # edge case like 799_996 => 799_997
        yield palindrome
    while prefix > 100:
        prefix -= 1
        yield append_reversed_tail(prefix)

def is_product_of_two_three_digit_numbers(it):
    logging.info("checking %s", it)
    upper = min(999, int(math.ceil(math.sqrt(it))))
    factor = 100
    while factor <= upper:
        other, remainder = divmod(it, factor)
        if remainder == 0 and 99 < other < 1000:
            return True
        factor += 1
    return False


# ========================================= boilerplate ========================================== #

def main(cases):
    return '\n'.join([str(solve(int(case))) for case in cases])


if __name__ == '__main__':
    logging.basicConfig(level=logging.WARN)
    print(main(sys.stdin.readlines()[1:]))
