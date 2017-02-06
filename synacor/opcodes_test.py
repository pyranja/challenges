import unittest
from opcodes import *

class OpCodeTest(unittest.TestCase):
    def test_yields_instruction_name(self):
        class Test(OpCode):
            pass
        subject = Test()
        self.assertEqual('test', subject.name)

    def test_default_arg_count(self):
        subject = OpCode()
        self.assertEqual(0, subject.arg_count)

    def test_render_default_disassembly(self):
        subject = OpCode()
        self.assertEqual('', subject.render_arguments([]))

if __name__ == '__main__':
    unittest.main()