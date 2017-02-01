import sys, unittest

def solve(input):
    return input

class Test(unittest.TestCase):

    def test_dummy(self):
        self.assertTrue(False)

if __name__ == '__main__':
    for line in sys.stdin.readlines():
        print(solve(line.strip()))