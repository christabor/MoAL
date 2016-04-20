# -*- coding: utf-8 -*-

"""
Based on:
https://en.wikipedia.org/wiki/Interpreter_(computing)#Bytecode_interpreters

Host machine
   | |_________
[sent to bytecode interpreter]
   |        |
   |     bytecode interpreter
   |        |________virtual machine
[run on VM]
   |             |____bytecode ("VM machine code")
[converted to bytecode]
   |_______________|___code file


Or also, an easier way to understand it:
src -> {lang interpreter} -> bytecode -> {bytecode interpreter} -> machine code

In the above case, the machine code can be virtual machine code.
"""

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

IS_MAIN = True if __name__ == '__main__' else False

if IS_MAIN:
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

import time

from MOAL.helpers.display import Section


class JITCompiler:
    """Just-in-time compiler.

    JIT compilation translates bytecode into machine code as needed.
    """


class BASICLanguageInterpreter:
    """An interpreter for the specific language source.

    In this case, it's a handful of BASIC commands.
    """

    def tokenize(self, code):
        return code.split('\n')

    def interpret(self, code):
        for token in self.tokenize(code):
            if token:
                # Yield a pair - function and argument, in this case.
                yield token.strip().split(' ')


class BASICBytecodeInterpreter:
    """An interpreter for the specific language bytecode.

    Instead of reading an efficient intermediary, here it just reads
    a tuple, then outputs something easier to call in python, acting
    as a simple translation layer.

    In a way, that's efficient, but make note it's
    not efficient in the traditional sense.
    """

    def interpret(self, code):
        for token in code:
            if len(token) > 1:
                func, arg = token
                if func and arg:
                    signature = '{}({})'.format(func, arg)
                    yield func, arg, signature


class PythonVirtualMachineInterpreter:
    """'Interprets' machine code generated from the bytecode interpreter."""

    def interpret(self, code):
        def _print(arg):
            print(arg)

        def cls(*args):
            print('\n\n\n\n\n')

        def sleep(arg):
            return time.sleep(int(args))

        control_table = dict(
            _print=_print,
            sleep=sleep,
            cls=cls,
        )
        for token in code:
            if len(token) > 2:
                func, args, signature = token
                print('Interpreter token signature: {}'.format(signature))
                if func == 'print':
                    print(args)
                else:
                    if func in control_table:
                        yield control_table[func](args)

    def run(self, prog):
        for val in prog:
            # Print just evaluates the generator.
            print(val)


if IS_MAIN:
    with Section('Bytecode interpreter'):
        code = """
        print 'Hello'
        sleep 1
        print 'World'
        cls 1
        end
        """
        langint = BASICLanguageInterpreter()
        byteint = BASICBytecodeInterpreter()
        vm = PythonVirtualMachineInterpreter()

        code = langint.interpret(code)
        code = byteint.interpret(code)
        code = vm.interpret(code)
        vm.run(code)
