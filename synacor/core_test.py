import unittest
from core import *

class ROMTest(unittest.TestCase):
    def setUp(self):
        self.subject = ROM(b'\x01\x00\x02\x00\x00\x01')

    def test_read_raw_by_address(self):
        self.assertEqual(b'\x01\x00', self.subject.read(0))
        self.assertEqual(b'\x02\x00', self.subject.read(1))
        self.assertEqual(b'\x00\x01', self.subject.read(2))

    def test_read_int_by_address(self):
        self.assertEqual(1, self.subject.read_int(0))
        self.assertEqual(2, self.subject.read_int(1))
        self.assertEqual(256, self.subject.read_int(2))

    def test_read_hex_by_address(self):
        self.assertEqual('0100', self.subject.read_hex(0))
        self.assertEqual('0200', self.subject.read_hex(1))
        self.assertEqual('0001', self.subject.read_hex(2))

    def test_read_word_after_eof(self):
        with self.assertRaises(IndexError):
            self.subject.read(3)

    def test_read_illegal_word(self):
        subject = ROM(b'\x08\xFF\xFF\xFF')
        with self.assertRaises(ValueError):
            subject.read_int(0)
        with self.assertRaises(ValueError):
            subject.read_int(1)

    def test_reports_custom_length(self):
        self.assertEqual(11, len(ROM(b'\x00\x01', 22)))

    def test_fail_on_illegal_length(self):
        with self.assertRaises(ValueError):
            ROM(b'', 3)

if __name__ == '__main__':
    unittest.main()
