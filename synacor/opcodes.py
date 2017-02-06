# base class for opcodes
class OpCode():
    def __init__(self, arg_count = 0):
        self.name = self.__class__.__name__.lower()
        self.arg_count = arg_count

    def render_arguments(self, args):
        return ''

class Halt(OpCode):
    pass

class Noop(OpCode):
    pass

class Out(OpCode):
    def __init__(self):
        OpCode.__init__(self, 1)

    def render_arguments(self, args):
        return chr(args[0]) if args[0] < 32768 else 'x' + str(args[0] - 32768)

OPCODES = {
    0: Halt(),
    19: Out(),
    21: Noop()
}
