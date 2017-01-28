#!/usr/bin/env python3
import sys, logging, itertools

"""find the n-th prime number"""

def primes(memento):
    memento.append(2)
    yield 2
    for i in itertools.count(start=3, step=2):
        for p in memento:
            if i % p == 0:
                break
        else:
            memento.append(i)
            yield i

class PrimeSequence:
    def __init__(self):
        self.found = []
        self.sequence = primes(self.found)

    def find(self, n):
        logging.info("searching %sth in %s", n, self.found)
        while not len(self.found) >= n:
            self.sequence.__next__()
        logging.info("searching %sth in %s", n, self.found)
        return self.found[n - 1]

PRIMES = PrimeSequence()

def solve(n):
    return PRIMES.find(n)

# ========================================= boilerplate ========================================== #

def main(cases):
    return '\n'.join([str(solve(int(case))) for case in cases])


if __name__ == '__main__':
    logging.basicConfig(level=logging.WARN)
    print(main(sys.stdin.readlines()[1:]))
