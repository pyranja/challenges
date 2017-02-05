import unittest
from vm import ROM

class ROMTest(unittest.TestCase):
    def setUp(self):
        self.subject = ROM(b'\x01\x00\x02\x00\x00\x01')

    def test_read_by_address(self):
        self.assertEqual(1, self.subject[0])
        self.assertEqual(2, self.subject[1])
        self.assertEqual(256, self.subject[2])

    def test_iterate_words(self):
        self.assertEqual([1,2,256], [i for i in self.subject])

    def test_read_word_after_eof(self):
        with self.assertRaises(IndexError):
            self.subject[3]

    def test_reports_custom_length(self):
        self.assertEqual(11, len(ROM(b'\x00\x01', 22)))

    def test_fail_on_illegal_length(self):
        with self.assertRaises(ValueError):
            ROM(b'', 3)

if __name__ == '__main__':
    unittest.main()        