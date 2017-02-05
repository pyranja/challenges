import sys, argparse, unittest, logging

LOG = logging.getLogger(__name__)

class ROM():
    def __init__(self, data, size = None):
        self.memory = data
        byte_count = size if size is not None else len(data)
        if byte_count % 2 > 0:
            raise ValueError("byte count must be a multiple of 2")
        self.size = byte_count // 2
        self.offset = 0

    def read_int(self, address):
        if address >= self.size:
            raise IndexError()
        offset = address * 2
        value = self.memory[offset:offset + 2]
        return int.from_bytes(value, byteorder = 'little')

    def __len__(self):
        return self.size

    def __getitem__(self, key):
        return self.read_int(key)

if __name__ == '__main__':
    logging.basicConfig(level = logging.DEBUG)
