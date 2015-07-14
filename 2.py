#!/usr/bin/env python3
import sys
from itertools import islice

def solve(n):
  return sum(islice(fib(n), 2, None, 3))

def fib(limit):
  predecessor = 0
  current = 1
  while current < limit:
    yield current
    temp = current
    current = current + predecessor
    predecessor = temp

cases = sys.stdin.readlines()[1:]
#cases = ["0", "10", "100"]
for line in cases:
  print(solve(int(line)))
