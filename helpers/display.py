from blessings import Terminal

term = Terminal()

# Display utilities


def _func_or_print(result, func):
    """Private function to either print or call a function on result"""
    if func is not None:
        func(result)
    else:
        print(result)


def _uncase_x(string, seperator):
    """Split by `seperator` and join the string;
    e.g. 'foo_bar' => foo bar """
    return ' '.join(string.split(str(seperator)))


def uncase_period(string):
    return _uncase_x(string, '.')


def uncase_hyphen(string):
    return _uncase_x(string, '-')


def uncase_snake(string):
    return _uncase_x(string, '_')


def uncase_snake_upper(string):
    return uncase_snake(string).upper()


def firstcaps(string):
    string = list(string.lower())
    string[0] = string[0].upper()
    return ''.join(string)


def title_case(string, seperator='_'):
    """Format a string into title case - e.g. 'some_word' => Some Word """
    return ' '.join(map(firstcaps, string.split(seperator)))


def divider(atom='_', newline=True):
    """Print a divider. Optionally override the unit of text to use
    (e.g ---, ...., ###)"""
    # Correct for longer than 1 character atoms, since it will take up
    # more than 80 chars.
    print(atom * (80 // len(atom)))
    if newline:
        print('\n')


def _label(prefix):
    """Private function to format prefix for a label (e.g. [MESSAGE])"""
    return '[{}] '.format(prefix.upper())


def print_subdued(msg):
    """Print info-type text in dark."""
    vals = '{t.black}{}{t.normal}'
    print(vals.format(msg, t=term))


def print_info(msg, prefix=True):
    """Print info-type text in red with a prefix"""
    prefix = _label('INFO') if prefix else ''
    vals = '{t.blue}{}{}{t.normal}'
    print(vals.format(prefix, msg, t=term))


def print_warning(msg, prefix=True):
    """Print warning-type text in red with a prefix"""
    prefix = _label('WARN') if prefix else ''
    vals = '{t.yellow}{}{}{t.normal}'
    print(vals.format(prefix, msg, t=term))


def print_success(msg, prefix=True):
    """Print success-type text in red with a prefix"""
    prefix = _label('YAY') if prefix else ''
    vals = '{t.green}{}{}{t.normal}'
    print(vals.format(prefix, msg, t=term))


def print_error(msg, prefix=True):
    """Print error-type text in red with a prefix"""
    prefix = _label('ERROR') if prefix else ''
    vals = '{t.red}{}{}{t.normal}'
    print(vals.format(prefix, msg, t=term))


def prnt(title, result, func=None, newlines=False):
    """A more useful default print function for titles and accompanying
    content. Shows stylized title, with content below, and newlines.
    The content can optionally be formatted by a given `func`."""
    if newlines:
        print('\n')
    print('{t.green}{t.underline}{}{t.normal}'.format(title, t=term))
    _func_or_print(result, func)
    if newlines:
        print('\n')


def _make_padded_char(word, padding=5):
    """Create a string format token with padding based on the length
    of the given `word` * `padding`;
    e.g. 'cat' -> {:<3}"""
    return '{:<' + str(len(str(word)) + padding) + '}'


def make_padded_chars(words, seperator=' '):
    """Call `_make_padding_char` on a list of words.
    For example, to create a new format string to pad a list of values.
    (e.g. {:<3} {<:6} {<:9}"""
    fmt_string = ''
    for word in words:
        fmt_string += _make_padded_char(word) + seperator
    return fmt_string


def print_table(rows, formatter=None, striped=True):
    """Print a table that is uniform and aligned."""
    headings = rows[0].keys()
    # Optionally allow custom format functions for each heading
    if formatter:
        headings = map(formatter, headings)
    # This is where it shines - we make a format string template based on
    # each heading token, which can be used for both headings and rows.
    template = make_padded_chars(headings)
    # Print headings first
    print_success(template.format(*headings), prefix=False)
    divider(newline=False)
    num_rows = len(rows)
    for k, row in enumerate(rows):
        values = row.values()
        # Apply the unique values to the template
        print(template.format(*values))
        if striped and k != num_rows - 1:
            divider(atom='-', newline=False)
    divider()


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

    def prnt(self, prefix, newlines=True):
        nl = '\n' if newlines else ''
        print('{t.cyan}{nl}[{}]: {t.bold} {} {sep} {nl}{t.normal}'.format(
            prefix, self.content, t=term, sep=self.separator, nl=nl))

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
