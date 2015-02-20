import platform
from random import choice
from string import ascii_letters
from string import ascii_uppercase as uppers


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


def randchars(c):
    return [choice(uppers) for _ in range(c)]


def uniqchars(count):
    def newchars(c):
        return ''.join(list(set(randchars(c))))

    if count < 2:
        count = 2

    string = newchars(count)
    while len(string) < count:
        string = newchars(count)
    return string


def words_unix_dict(min_length=8):
    if platform.system() == 'Windows':
        yield None
    # Gets a new word from the unix file system dict `/usr/share/dict/words`,
    # available in Unix systems! Sorry Windows.
    with open('/usr/share/dict/words') as words:
        for word in words:
            if len(word) >= min_length:
                yield word.strip()
        raise StopIteration
