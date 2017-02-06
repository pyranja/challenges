import sys, argparse, logging
from core import ROM
from opcodes import OPCODES

log = logging.getLogger(__name__)

def disassemble(code, out):
    '''disassemble a binary to given stream'''
    ip = 0
    while ip < len(code):
        opcode = OPCODES.get(code.read_int(ip))
        if opcode is None:
            ip += 1
            continue
        args = [code.read_int(ip + idx + 1) for idx in range(0, opcode.arg_count)]
        instruction = '[{:05}]   {:>4} {}\n'.format(ip, opcode.name, opcode.render_arguments(args))
        out.write(instruction)
        ip += opcode.arg_count + 1

def assemble(code, out):
    # translate instructions into int sequence
    # convert int sequence to binary representation
    pass

if __name__ == '__main__':
    logging.basicConfig(level = logging.DEBUG)

    parser = argparse.ArgumentParser(description='Convert synacor binaries to an op-code listing.')
    parser.add_argument('binary')
    args = parser.parse_args()

    with open(args.binary, 'rb') as input:
        code = ROM(input.read())
        disassemble(code, sys.stdout)
