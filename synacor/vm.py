import sys, argparse, logging
from core import ROM
from opcodes import OPCODES

log = logging.getLogger(__name__)

def run(code):
    '''execute a binary program'''
    ip = 0
    while True:
        instruction = OPCODES[code.read_int(ip)]
        args = [code.read_int(ip + idx + 1) for idx in range(0, instruction.arg_count)]
        log.debug('-> %s %s', instruction.name, instruction.render_arguments(*args))
        instruction(*args)
        ip += 1

def disassemble(code, out):
    '''disassemble a binary to given stream'''
    ip = 0
    while ip < len(code):
        opcode = OPCODES.get(code.read_int(ip))
        if opcode is None:
            ip += 1
            continue
        args = [code.read_int(ip + idx + 1) for idx in range(0, opcode.arg_count)]
        instruction = '[{:05}]   {:>4} {}\n'.format(ip, opcode.name, opcode.render_arguments(*args))
        out.write(instruction)
        ip += opcode.arg_count + 1

def assemble(code, out):
    # translate instructions into int sequence
    # convert int sequence to binary representation
    pass

if __name__ == '__main__':
    logging.basicConfig(level = logging.INFO)

    parser = argparse.ArgumentParser(description='Convert synacor binaries to an op-code listing.')
    parser.add_argument('input')
    args = parser.parse_args()

    with open(args.input, 'rb') as input:
        code = ROM(input.read())
        # run(code)
        disassemble(code, sys.stdout)
