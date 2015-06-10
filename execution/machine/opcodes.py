# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section
from helpers.display import print_success
from helpers.display import prnt
from helpers.display import divider

DEBUG = True if __name__ == '__main__' else False


class OpCode:

    def __init__(self, code, name, description, assembly):
        """Creates a code with typical metadata, and the actual
        assembly code to run it.

        Args:
            code (string): the opcode
            name (string): the nice (semantic) name, e.g. STOP, POP_TOP, etc...
            description (string): an informal detailed description
            assembly (list): a list of each instruction in
                sequence when this opcode is called.
        Returns:
            None
        """
        self.code = code
        self.name = name
        self.description = description
        self.assembly = assembly

    def call(self):
        prnt('Calling opcode: "{}"'.format(self.code), '')
        for line in self.assembly:
            print_success(line, prefix='[ASSEMBLY]')
        divider()

    def read_external(self, code=[]):
        """Reads an 'external' Python implementation specific opcode.
        Try loading a pyc file in!
        Args:
            code (string): a real python opcode.
        Returns:
            None
        """
        raise NotImplementedError


if DEBUG:
    with Section('Machine OpCodes'):
        """
        From Wikipedia:

        "In computing, an opcode (abbreviated from operation code)
        is the portion of a machine language instruction that specifies
        the operation to be performed. Beside the opcode itself,
        instructions usually specify the data they will process,
        in form of operands. In addition to opcodes used in instruction set
        architectures of various CPUs, which are hardware devices, they can
        also be used in abstract computing machines as part of their
        byte code specifications."

        Example opcodes used here taken from: unpyc.sourceforge.net/Opcodes.html
        """
        program = [
            OpCode(
                '00h', 'STOP_CODE',
                'Indicates end-of-code to the compiler, '
                'not used by the interpreter.', []),
            OpCode(
                '01h', 'POP_TOP', 'Removes the top-of-stack (TOS) item.',
                ['<module>:',
                 '00000000 64 (00 00 = 00000031 CODE()) - LOAD_CONST',
                 '00000003 84 (00 00) - MAKE_FUNCTION',
                 '00000006 83 (00 00) - CALL_FUNCTION',
                 '00000009 01 - POP_TOP',
                 '0000000A 64 (01 00 = 00000096 None (4E)) - LOAD_CONST',
                 '0000000D 53 - RETURN_VALUE',
                 '<lambda>:',
                 '00000000 64 (00 00 = 00000050 INT: 1 (01 00 00 00))'
                    ' - LOAD_CONST',
                 '00000003 53 - RETURN_VALUE']),
            OpCode(
                '47h', 'PRINT_ITEM',
                'Prints TOS to the file-like object bound to sys.stdout. '
                'There is one such instruction for each item in the '
                'print statement.',
                ['00000000 64 (00 00 = 0000002C STR: \'hello world!\' '
                    '(0C 00...) - LOAD_CONST',
                 '00000003 47 - PRINT_ITEM',
                 '00000004 48 - PRINT_NEWLINE',
                 '00000005 64 (01 00 = 0000003D None (4E)) - LOAD_CONST',
                 '00000008 53 - RETURN_VALUE']),
            OpCode(
                '48h', 'PRINT_NEWLINE', 'Prints a new line on sys.stdout.'
                ' This is generated as the last operation of a print statement,'
                ' unless the statement ends with a comma.',
                ['00000000 48 - PRINT_NEWLINE',
                 '00000001 64 (00 00 = 00000028 None (4E)) - LOAD_CONST',
                 '00000004 53 - RETURN_VALUE']),
        ]

        for opcode in program:
            opcode.call()
