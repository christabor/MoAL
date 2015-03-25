from blessings import Terminal

term = Terminal()

# Display utilities


def _func_or_print(result, func):
    """Private function to either print or call a function on result"""
    if func is not None:
        func(result)
    else:
        print(result)


def divider(atom='_'):
    """Print a divider. Optionally override the unit of text to use
    (e.g ---, ...., ###)"""
    print(atom * 80)
    print('\n')


def _label(prefix):
    """Private function to format prefix for a label (e.g. [MESSAGE])"""
    return '[{}] '.format(prefix.upper())


def print_info(msg):
    """Print info-type text in red with a prefix"""
    prefix = _label('INFO')
    vals = '{t.blue}{}{}{t.normal}'
    print(vals.format(prefix, msg, t=term))


def print_warning(msg):
    """Print warning-type text in red with a prefix"""
    prefix = _label('WARN')
    vals = '{t.yellow}{}{}{t.normal}'
    print(vals.format(prefix, msg, t=term))


def print_success(msg):
    """Print success-type text in red with a prefix"""
    prefix = _label('YAY')
    vals = '{t.green}{}{}{t.normal}'
    print(vals.format(prefix, msg, t=term))


def print_error(msg):
    """Print error-type text in red with a prefix"""
    prefix = _label('ERROR')
    vals = '{t.red}{}{}{t.normal}'
    print(vals.format(prefix, msg, t=term))


def prnt(title, result, func=None):
    """A more useful default print function for titles and accompanying
    content. Shows stylized title, with content below, and newlines.
    The content can optionally be formatted by a given `func`."""
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
    """Print a title with a newline.
    The newline can be either on bottom (default) or top, if specified."""
    if pos == 'top':
        print('\n{}'.format(title))
    else:
        print('{}\n'.format(title))


def _heading(title, divider, desc=''):
    hyphen = '' if desc == '' else ' - '
    text = ('\n {} {} {}\n' '|{}|\n').format(
        title.upper(), hyphen, desc, divider * 80)
    print_nl(text)


def print_h1(title, desc=''):
    """Print a heading with a very bold underline"""
    _heading(title, '#', desc=desc)


def print_h2(title, desc=''):
    """Print a heading with a bold underline"""
    _heading(title, '=', desc=desc)


def print_h3(title, desc=''):
    """Print a heading with a moderate underline"""
    _heading(title, '-', desc=desc)


def print_h4(title, desc=''):
    """Print a heading with a subdued underline"""
    _heading(title, '.', desc=desc)


def print_simple(words, result, func=None):
    """Print a heading with data. The content can optionally be formatted by
    a given `func`. No styling is done to the text."""
    print(words)
    _func_or_print(result, func)
    print('\n')


def cmd_title(msg, newlines=True):
    """Print a command type message (e.g [COMMAND]) in red."""
    if newlines:
        print('\n')
    print('{t.red}[{msg}]{t.normal}'.format(msg=msg.upper(), t=term))
    if newlines:
        print('\n')


class Section:
    """Provides a context manager for printing 'sections' of text.
    Prints a top and bottom section to visually separate different blocks
    of code/results."""

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


if __name__ == '__main__':
    print_info('Testing Info')
    print_warning('Testing Warning')
    print_success('Testing Success')
    print_error('Testing Error')

    cmd_title('DANGER WILL ROBINSON')

    print_h1('Heading 1...')
    print_h2('Heading 2...')
    print_h3('Heading 3...')
    print_h4('Heading 4...')
