from blessings import Terminal

term = Terminal()

# Display utilities


def _func_or_print(result, func):
    if func is not None:
        func(result)
    else:
        print(result)


def prnt(words, result, func=None):
    print('\n')
    print('{t.green}{t.underline}{}{t.normal}'.format(words, t=term))
    _func_or_print(result, func)
    print('\n')


def print_simple(words, result, func=None):
    print(words)
    _func_or_print(result, func)
    print('\n')


def _cmd_title(msg):
    print('\n')
    print('{t.red}[{msg}]{t.normal}'.format(msg=msg.upper(), t=term))
    print('\n')


class Section:

    def __init__(self, content):
        self.separator = '=' * 50
        self.content = content

    def prnt(self, prefix):
        print('\n')
        print('{t.cyan}\n= [{}]: {t.bold} {} {sep} \n{t.normal}'.format(
            prefix, self.content, t=term, sep=self.separator))

    def __enter__(self):
        self.prnt('BEGIN')

    def __exit__(self, exception_type, exception_value, traceback):
        self.prnt('END')
