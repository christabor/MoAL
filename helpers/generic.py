from random import choice
from random import randrange as rr
from itertools import chain
from itertools import izip


def subdivide_groups(items, divisions=2):
    """Divides a list of items up into subdivisions based on `divisions`.
    For example, [1, 2, 3, 4] with 2 divisions
        becomes [[1, 2], [3, 4]]
    or, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] with 5 divisions
        becomes [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]].

    Numbers that cannot be distributed equally will
    have the remainder added to the last group.
    """
    groups = []
    num_items = len(items)
    last_offset = 0
    # Determine the length of each subdivision
    sections = num_items // divisions
    for _ in range(num_items):
        # Append based on current range, shift, repeat.
        sub_group = items[last_offset:last_offset + sections]
        # Any uneven offsets will simply be empty -- don't include them.
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


def slice_dict(ref_dict, start, end):
    """Create a subsection (slice) of a dictionary, like a list."""
    sliced = {}
    for k, v in ref_dict.iteritems():
        if k < start:
            continue
        if k == end:
            break
        else:
            sliced[k] = v
    return sliced


def powerset_list(main_list, side='left'):
    """Return staggered offsets  of lists of a given list.
    e.g. [1, 2, 3] => [[1, 2, 3], [1, 2], [1]]
    `side` determines which way to offset: left, or right.

    Switching sides would be the same as reversing the list beforehand.
    """
    if side not in ['left', 'right']:
        raise TypeError
    return [[main_list[k:] if side == 'left' else main_list[:k]]
            for k, _ in enumerate(main_list)]


def substring_list(string):
    """Return all substrings of a given string as a list."""
    return [string[k:] for k, char in enumerate(string)]


def substring_dict(string):
    """Return all substrings of a given string as a dict."""
    sub_dict = {}
    for i in range(0, len(string)):
        sub_dict[i] = {i: string[i:] for _, char in enumerate(string)}
    return sub_dict


def powerset_tree(lst, initial=True, terminator=''):
    """Creates nested powersets of the word list for each key
    -- effectively a suffix tree generator.
    `terminator` is a string value that can be passed in to terminate
    each parent element in a list -- indices can be used to denote
    the same thing, but it gives a visual option if you prefer.
    """
    # If it happens to be a list, convert it first.
    if isinstance(lst, str):
        lst = substring_list(lst)
    # Go over each item in the list...
    for k, substr in enumerate(lst):
        # If it's the very first item in the **top outer most list**,
        # just make it a singleton list, since it's the full string
        # and we don't want to subdivide it.
        if initial:
            lst[k] = [substr + terminator]
            # Make sure to set this to false so it **never runs again**.
            initial = False
        else:
            # If the substring is a singleton list, continue,
            # as it's the last item in the substring sublist.
            if len(substr) == 1:
                continue
            # Otherwise, recursively travel down into this list,
            # repeating the process with a string one character
            # smaller than the last -- but nest it inside
            # this list so the parent is referenced as the first key
            # and the children elements are
            # inside the second key, as a list.
            lst[k] = [substr + terminator, powerset_tree(
                substring_list(substr[1:]), initial=initial)]
    # Return the final list.
    return lst


def choice_take(options, maximum):
    """Return an array of random choices.
    Choices are seeded from `options` from 0 until `maximum`.
    """
    return [choice(options) for _ in range(maximum)]


def random_number_set(min_rand=0, max_rand=9999, max_range=100):
    """Generated a set of random number sets."""
    return [rr(min_rand, max_rand) for _ in range(max_range)]


def random_number_sets(sets=2, max_random=50):
    return [random_number_set(0, 9999, max_random) for _ in range(sets)]


def interleave(*lists):
    return list(chain.from_iterable(izip(*lists)))
