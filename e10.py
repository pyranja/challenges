#!/usr/bin/env python3
import sys, logging, math

"""sum up primes smaller than a given limit N"""

LIMIT = 10 ** 6 + 1
LOOKUP = [0] * LIMIT

def sieve(n):
    """create a sieve up to a given number"""
    is_prime = [False if i % 2 == 0 else True for i in range(0, n)]
    # edge cases
    is_prime[2] = True
    is_prime[1] = False
    for number in range(2, math.ceil(math.sqrt(n))):
        if is_prime[number]:
            for multiple in range(number ** 2, n, number):
                is_prime[multiple] = False
    return is_prime

def pre_compute_prime_sums():
    sieved = sieve(LIMIT)
    current = 0
    for index, prime in enumerate(sieved):
        # logging.info("%d (%s) -> %d", index, prime, current)
        current = current + index if prime else current
        LOOKUP[index] = current

pre_compute_prime_sums()

def solve(n):
    return LOOKUP[n]

# ========================================= boilerplate ========================================== #

def main(cases):
    return '\n'.join([str(solve(int(case))) for case in cases])


if __name__ == '__main__':
    logging.basicConfig(level=logging.WARNING)
    print(main(sys.stdin.readlines()[1:]))
