import sys, unittest

class Pixel():
    def __init__(self, x, y, payload):
        self.x = x
        self.y = y
        self.payload = payload

# pixel filter
def in_crater(point):
    return point.payload == 1

class Image():
    def __init__(self, rows, cols, data):
        self.rows = rows
        self.cols = cols
        self.pixels = [Pixel(idx % cols, idx // cols, in_crater) for idx, in_crater in enumerate(data)]

    def bounding_box(self, selector):
        selected = [pixel for pixel in self.pixels if selector(pixel)]
        topLeftX = min(each.x for each in selected)
        topLeftY = min(each.y for each in selected)
        bottomRightX = max(each.x for each in selected)
        bottomRightY = max(each.y for each in selected)
        return topLeftX - 1, topLeftY - 1, (bottomRightX - topLeftX) + 2, (bottomRightY - topLeftY) + 2

    def dump(self, renderer):
        matrix = [self.pixels[row * self.cols:(row + 1) * self.cols] for row in range(self.rows)]
        print('\n'.join(' '.join(str(renderer(pixel)) for pixel in row) for row in matrix))

# print helpers
def coordinates(point):
    return '({:^2d}|{:^2d})'.format(point.x, point.y)

def payload(point):
    return '({})'.format(point.payload)

def solve(input):
    image = parse(input)
    image.dump(payload)
    return image.bounding_box(in_crater)

def parse(input):
    parts = input.split()
    rows, cols, image = int(parts[0]), int(parts[1]), [int(x) for x in parts[2:]]
    return Image(rows, cols, image)

class Test(unittest.TestCase):

    def test_dummy(self):
        self.assertTrue(False)

if __name__ == '__main__':
    for line in sys.stdin.readlines():
        print(solve(line.strip()))