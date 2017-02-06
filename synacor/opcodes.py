from core import StopVirtualMachine
from collections import defaultdict

# base class for opcodes
class OpCode():
    def __init__(self, arg_count = 0):
        self.name = self.__class__.__name__.lower()
        self.arg_count = arg_count

    def render_arguments(self):
        return ''

class IllegalInstruction(ValueError):
    '''thrown if an opcode is not recognized'''

class Unknown(OpCode):
    '''fallback instruction if an opcode is not recognized'''
    def __call__(self):
        raise IllegalInstruction()

class Halt(OpCode):
    '''Terminate program execution'''
    def __call__(self):
        raise StopVirtualMachine(0)

class Noop(OpCode):
    '''This instruction is ignored by the VM'''
    def __call__(self):
        pass

class Out(OpCode):
    def __init__(self):
        OpCode.__init__(self, 1)

    def render_arguments(self, value):
        return chr(value) if value < 32768 else 'x' + str(value - 32768)

    def __call__(self, value):
        print(chr(value), end='')

OPCODES = defaultdict(Noop)
OPCODES[0] = Halt()
OPCODES[19] = Out()
OPCODES[21] = Noop()
