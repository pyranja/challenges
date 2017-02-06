import unittest
from opcodes import *
from core import StopVirtualMachine

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

class UnknownTest(unittest.TestCase):
    def test_throws_IllegalInstruction(self):
        with self.assertRaises(IllegalInstruction):
            Unknown()()

class HaltTest(unittest.TestCase):
    def test_throws_StopExecution(self):
        with self.assertRaises(StopVirtualMachine):
            Halt()()

class NoopTest(unittest.TestCase):
    def test_is_callable(self):
        Noop()()

class OutTest(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()