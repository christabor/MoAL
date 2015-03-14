from blessings import Terminal

term = Terminal()

# Display utilities


def _func_or_print(result, func):
    if func is not None:
        func(result)
    else:
        print(result)


def divider(atom='_'):
    print(atom * 80)
    print('\n')


def prnt(title, result, func=None):
    print('\n')
    print('{t.green}{t.underline}{}{t.normal}'.format(title, t=term))
    _func_or_print(result, func)
    print('\n')


def print_vars(vars, upper=False, convert=False):
    """Single line print with variable and a title, as well
    as some optional kwargs to transform the data."""
    # Allow passing in of single or multiple lists
    if isinstance(vars[0], str) and len(vars) == 2:
        is_single = True
        # Format the list appropriately
        vars = [vars]
    else:
        is_single = False
    for var in vars:
        if len(var) != 2 and not is_single:
            raise TypeError('Need both title and variable.')
        title, data = var
        if isinstance(data, list) and convert:
            if len(data) > 1:
                data = ''.join(map(str, data))
        elif upper:
            title = title.upper()
        print('{}: {}'.format(title, data))


def print_nl(title, pos='top'):
    if pos == 'top':
        print('\n{}'.format(title))
    else:
        print('{}\n'.format(title))


def _heading(title, divider, desc=None):
    desc = '' if None else desc
    text = (
        '\n {} - {}\n'
        '|{}|\n').format(title.upper(), desc, divider * 50)
    print_nl(text)


def print_h1(title, desc=None):
    _heading(title, '#', desc=desc)


def print_h2(title, desc=None):
    _heading(title, '=', desc=desc)


def print_h3(title, desc=None):
    _heading(title, '-', desc=desc)


def print_h4(title, desc=None):
    _heading(title, '.', desc=desc)


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
