import argparse
from functools import lru_cache

parser = argparse.ArgumentParser(description = 'calculate fibonnacci')
parser.add_argument('n', metavar = 'N', type = int)

@lru_cache(maxsize = None)
def fib(n):
    return n if n < 2 else fib(n-1) + fib(n-2)

if __name__ == "__main__":
    args = parser.parse_args()
    print(fib(args.n))
