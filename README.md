# euler

Solutions for [project euler](https://projecteuler.net/) challenges from 
[hackerrank](https://www.hackerrank.com/contests/projecteuler). All solutions are using only pure
python, no dependencies on third-party code.

## code templates

The `template.py` is a skeleton implementation of solution scripts. It takes care of reading cases
from stdin and writing to stdout. `runner.py` can be used to run the solution files from an IDE
during development.

## library

The `lib` folder contains common utility/math functions, which are useful in multiple solutions.
Each lib module has embedded unit tests. Running the test requires the 
[hypothesis](https://hypothesis.readthedocs.org/en/latest/) package.

Solution scripts do *not* import modules from lib, as they need to be run as standalone scripts in
hackerrank.
