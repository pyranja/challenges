import itertools


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


def primes():
    """
    generate prime numbers in increasing order

    naive implementation inspired by http://stackoverflow.com/a/15706985/1267168
    """
    yield 2
    found = []
    for i in itertools.count(start=3, step=2):
        for p in found:
            if i % p == 0:
                break
        else:
            yield i
            found.append(i)

# ========================================= test ================================================= #
import unittest, timeit
from collections import Counter
from hypothesis import given
from hypothesis.strategies import lists, sampled_from


class TestPrimes(unittest.TestCase):
    LIMIT = 1000

    def is_prime(self, it):
        """naive prime test, to avoid logic errors"""
        return it > 0 \
               and (it == 2 or it % 2 != 0) \
               and (it == 1 or not (any(it % number == 0 for number in range(3, it // 2, 2))))

    def test_generated_numbers_are_prime(self):
        for maybe_prime in itertools.islice(primes(), 0, TestPrimes.LIMIT):
            self.assertTrue(self.is_prime(maybe_prime), "%d is not a prime" % maybe_prime)


class TestFactorize(unittest.TestCase):
    PRIMES = list(itertools.islice(primes(), 0, 1000))

    @given(lists(elements=sampled_from(PRIMES), min_size=1, max_size=40, average_size=20))
    def test_finds_constituent_prime_factors(self, factors):
        number = 1
        for f in factors:
            number *= f
        self.assertEqual(Counter(factors), Counter(factorize(number)))


if __name__ == '__main__':
    timeit.main(['--setup', 'from __main__ import factorize', 'factorize(123456789)'])
    unittest.main()
