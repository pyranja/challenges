#!/usr/bin/env python3
import sys

def solve(n):
  return arithmetic_series(3, n) + arithmetic_series(5, n) - arithmetic_series(15, n)

def arithmetic_series(d, n):
  top = n - (n % d)
  return (d + top) * (n // d) // 2

cases = sys.stdin.readlines()[1:]
#cases = ["10", "100"]
for line in cases:
  print(solve(int(line) - 1))
