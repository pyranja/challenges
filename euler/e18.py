#!/usr/bin/env python3
import sys
import logging

"""find triangle path with maximum sum"""


# use depth first search

def solve(triangle):
    return descend(triangle, 0, 0, 0)


def descend(triangle, row, column, current):
    logging.info(">> [%d][%d] == %d", row, column, current)
    current += triangle[row][column]
    next_row = row + 1
    if next_row == len(triangle):
        return current  # leaf
    down = descend(triangle, next_row, column, current)
    right = descend(triangle, next_row, column + 1, current)
    return max(down, right)


def parse_triangle(lines):
    return [[int(node) for node in line.split(' ')] for line in lines]


def parse_cases(lines):
    index = 0
    while index < len(lines):
        size = int(lines[index])
        triangle_start = index + 1
        triangle_end = triangle_start + size
        case = lines[triangle_start:triangle_end]
        logging.info("reading: size=%d case=%s", size, case)
        yield case
        index = triangle_end


# ========================================= boilerplate ========================================== #

def main(cases):
    return '\n'.join([str(solve(parse_triangle(case))) for case in parse_cases(cases)])


if __name__ == '__main__':
    logging.basicConfig(level=logging.WARN)
    print(main(sys.stdin.readlines()[1:]))
