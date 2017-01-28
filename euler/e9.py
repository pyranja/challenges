#!/usr/bin/env python3
import sys, logging
from functools import partial

"""find pythagorean triplets adding up to a given N"""

# maybe able to speedup by reducing search space ... up to N/3 only?

def solve(n):
    logging.info("searching for N == %d", n)
    triplet_from = compile_equation_system_for(n)
    maximum = -1
    for i in range(1, n):
        a, b, c = triplet_from(i)
        if a.is_integer() and a > 0 and c.is_integer() and c > 0:
            logging.info("found triplet (%s, %s, %s)", a, b, c)
            product = a * b * c
            maximum = product if product > maximum else maximum
    return int(maximum)

def compile_equation_system_for(n):
    n_squared = n**2
    def solver(b):
        """
        Given b, return a tuple (a,b,c) which satisfies
         (I)  a**2 + b**2 = c**2
         (II) a + b + c = N
        """
        c = n_squared / (2 * n - 2 * b) - b
        a = n - b - c
        return a, b, c
    return solver

# ========================================= boilerplate ========================================== #

def main(cases):
    return '\n'.join([str(solve(int(case))) for case in cases])


if __name__ == '__main__':
    logging.basicConfig(level=logging.WARN)
    print(main(sys.stdin.readlines()[1:]))
