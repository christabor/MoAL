from random import choice
from string import ascii_letters


def gibberish(length=10):
    return ''.join([choice(
        ascii_letters).replace(' ', '') for _ in range(length)])


def gibberish2(length=3):
    """Returns somewhat normal looking gibberish"""
    _letters = list(ascii_letters)
    vowels = list('aeiou')
    if length < 3:
        length = 3

    def token():
        first, middle, last = choice(
            _letters), choice(vowels), choice(_letters)
        return first + middle + last
    return ''.join([token() for _ in range(length)])


def divide_groups(items, divisions=2):
    """Divides a list of items up into subdivisions based on `divisions`.
    For example, [1, 2, 3, 4] with 2 divisions
        becomes [[1, 2], [3, 4]]
    And [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] with 5 divisions
        becomes [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]].

    Numbers that cannot be distributed equally will
    have the remainder added to the last group.
    """
    groups = []
    num_items = len(items)
    last_offset = 0
    sections = num_items // divisions
    for i in range(num_items):
        sub_group = items[last_offset:last_offset + sections]
        if sub_group:
            groups.append(sub_group)
        # Update the last offset for the next index.
        last_offset += sections
    return groups


def swap_item(items, a, b):
    copy = items[a]
    items[a] = items[b]
    items[b] = copy
    return items


def pick_until(options, maximum):
    """Return an array of random choices, seeded from `options`
    from 0 until `maximum`"""
    return [choice(options) for _ in range(maximum)]


def random_number_set(min_rand=0, max_rand=9999, max_range=100):
    return [rr(min_rand, max_rand) for _ in range(max_range)]


def get_random_number_sets(sets=2, max_random=50):
    return [random_number_set(0, 9999, max_random) for _ in range(sets)]
