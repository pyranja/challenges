#!/usr/bin/env python3
import sys
import logging
import itertools

"""find smallest triangular number that has more than a given number n of divisors"""

LOOKUP = [1]  # each element is first triangular number index with divisor_count > list index


def find(count):
    # if count already filled use that, else return last element
    return LOOKUP[count] if count < len(LOOKUP) else LOOKUP[-1]


def save(tringular_index, count):
    # fill up LOOKUP as long as divisor_count > last list index
    while count > len(LOOKUP):
        LOOKUP.append(tringular_index)


def solve(n):
    idx = find(n)
    for it in itertools.count(idx):
        count = divisor_count(it)
        save(it, count)
        # logging.info("checking %d-th triangular number (%d) ==> %d divisors", it, it * (it + 1) // 2, count)
        if count > n:
            return it * (it + 1) // 2


# use n * (n + 1) / 2, find prime factors of n and n + 1 (divide the even one by 2)
# derive all divisors by enumerating all possible products of prime factors

# use gaussian sum formula to decompose the triangular number
#   n-th triangular number = (a * b) / 2 ; where a = n and b = n + 1
# either n or n + 1 is even and can be divided by 2 to simplify the formula
# determine prime factors of each component and calculate the "superset" of
# factors, i.e. each possible product combination of factors
def divisor_count(n):
    """calculate number of divisors of n-th triangular number"""
    if n == 1:  # shortcut
        return 1
    a, b = decompose(n)
    prime_factors = list(factorize(a))
    prime_factors.extend(factorize(b))
    # logging.debug("components a=%d b=%d with prime_factors == %s", a, b, prime_factors)
    count = 0
    # generate super set of all possible prime factor combinations
    for combination_size in range(0, len(prime_factors) + 1):
        # conversion to set eliminates duplicates
        combinations = set(itertools.combinations(prime_factors, combination_size))
        # logging.debug("all products of length %d : %s", combination_size, combinations)
        count += len(combinations)
    logging.debug("found divisors for %d : %s", n, count)
    return count


def decompose(n):
    a = n
    b = n + 1
    # divide even component by 2
    if n % 2 == 0:
        a /= 2
    else:
        b /= 2
    # logging.debug("decomposing [%dth == %d] => %d * (%d + 1) // 2 = %d", n, a * b, n, n, n * (n+1) // 2)
    return a, b


def factorize(it):
    """
    find all prime factors of a given positive, non-zero integer and return them in increasing order
    """
    assert it > 0, "cannot factorize %s" % it
    while it % 2 == 0:  # special case 2 - allows exclusion of even numbers later
        yield 2
        it //= 2
    factor = 3
    while factor * factor <= it:
        while it % factor == 0:
            yield factor
            it //= factor
        factor += 2
    if it > 1:  # remainder is a prime
        yield it


# ========================================= boilerplate ========================================== #

def main(cases):
    return '\n'.join([str(solve(int(case))) for case in cases])


if __name__ == '__main__':
    logging.basicConfig(level=logging.WARNING)
    print(main(sys.stdin.readlines()[1:]))
