#!/usr/bin/env python3
import sys, logging, itertools

"""find max product in a grid"""

GROUP_SIZE = 4

def solve(grid):
    # grid indexing: [row][column]
    maximum = 0
    for positions in itertools.chain(row_wise(grid), col_wise(grid), diagonal_to_right(grid), diagonal_to_left(grid)):
        current = grid_product(grid, positions)
        maximum = current if current > maximum else maximum
    return maximum

def row_count(grid):
    return len(grid)

def column_count(grid):
    return len(grid[0]) # assume quadratic grid

def row_wise(grid):
    for row in range(0, row_count(grid)):
        for offset in range(0, row_count(grid) - GROUP_SIZE + 1):
            yield [(row, column) for column in range(offset, offset + GROUP_SIZE)]

def col_wise(grid):
    for column in range(0, column_count(grid)):
        for offset in range(0, column_count(grid) - GROUP_SIZE + 1):
            yield [(row, column) for row in range(offset, offset + GROUP_SIZE)]

def diagonal_to_right(grid):
    for row_init in range(0, row_count(grid) - GROUP_SIZE + 1):
        for column_init in range(0, column_count(grid) - GROUP_SIZE + 1):
            yield [(row, column) for row, column in zip(range(row_init, row_init + GROUP_SIZE), range(column_init, column_init + GROUP_SIZE))]

def diagonal_to_left(grid):
    for row_init in range(GROUP_SIZE - 1, row_count(grid)):
        for column_init in range(0, column_count(grid) - GROUP_SIZE + 1):
            yield [(row, column) for row, column in zip(range(row_init, row_init - GROUP_SIZE, -1), range(column_init, column_init + GROUP_SIZE))]

def grid_product(grid, positions):
    logging.info('calculating group product for %s', positions)
    product = 1
    for row, column in positions:
        product *= grid[row][column]
    return product

# ========================================= boilerplate ========================================== #

def main(cases):
    return solve([[int(i) for i in line.split(' ')] for line in cases])


if __name__ == '__main__':
    logging.basicConfig(level=logging.WARN)
    print(main(sys.stdin.readlines()))
