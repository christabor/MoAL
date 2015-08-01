from random import randrange as rr
from random import choice
from string import ascii_uppercase


def random_node(vals, nums, max_edges):
    return {
        'edges': [choice(nums) for _ in range(rr(0, max_edges))],
        'val': choice(vals)
    }


def random_graph(max_edges=10):
    letters = [choice(ascii_uppercase) for _ in range(max_edges)]
    dag = {}
    nums = range(max_edges)
    for k, letter in enumerate(letters):
        dag[k] = random_node(letter, nums, max_edges)
    return dag


def subnet_mask():
    op1 = '255.255.255.255'
    op2 = '255.0.0.0'
    op3 = '255.255.255.{}{}{}'.format(
        choice(range(1, 2)), choice(range(0, 9)), choice(range(0, 9)))
    return choice([op1, op2, op3])


def random_dna(max=4):
    """Generate a random string of DNA.

    Kwargs:
        max (int) - The maximum length of the string.

    >>> random_dna(max=4)
    'TCGA'
    """
    dna = ''
    acids = ['T', 'G', 'A', 'C']
    for x in range(max):
        dna += choice(acids)
    return dna


def random_inverse_binary_matrix(**kwargs):
    """Generate a matrix filled with random 0's, -1's or 1's.

    >>> random_binary_matrix(rows=2, columns=2)
    [[0, 1, -1], [-1, 1, 0]]
    """
    if kwargs is None:
        kwargs = {}
    kwargs.update({'choices': [0, 1, -1]})
    return random_matrix(**kwargs)


def random_binary_matrix(**kwargs):
    """Generate a matrix filled with random 0's or 1's.

    >>> random_binary_matrix(rows=2, columns=2)
    [[0, 1], [1, 0]]
    """
    if kwargs is None:
        kwargs = {}
    kwargs.update({'choices': [0, 1]})
    return random_matrix(**kwargs)


def random_matrix(rows=4, columns=4, min=1, max=100, choices=None):
    """Generate a matrix filled with random numbers.

    Kwargs:
        rows (int) - The number of rows.
        columns (int) - The number of columns for each row.
        min (int) - The minimum number to use in randrange
        max (int) - The maximum number to use in randrange
        choices (list) - The choices to choose from, if specified.
            If none specified, randrange(min, max) will be used.

    >>> random_matrix(rows=3, columns=3, min=1, max=2)
    [[94, 23, 50], [57, 28, 52], [94, 5, 45]]
    """
    matrix = []
    for row in range(rows):
        _row = []
        for _ in range(columns):
            if choices is not None:
                _row.append(choice(choices))
            else:
                _row.append(rr(min, max))
        matrix.append(_row)
    return matrix


def make_sparselist(vals, total, filler=0):
    """Generate a sparse list with a given set of values.

    Args:
        vals (dict) - the list of indices and values,
            where the key value represents the index to fill in
        total (int) - the total length of the list. A length less than the
            length of len(keys.values()) will throw a ValueError

    Returns:
        sparselist (list) - the sparselist.
    """
    if total < max(vals.keys()):
        raise ValueError(
            'Invalid length. Keys must be less than or equal to total.')
    _sparselist = [filler for _ in range(total)]
    for index, value in vals.iteritems():
        _sparselist[index] = value
    return _sparselist
