# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section

DEBUG = True if __name__ == '__main__' else False


class GapBuffer(list):

    def __init__(self, string, gap_size=8):
        self.gap_size = gap_size
        chars = list(string)
        mid = len(string) // 2
        # This forms the gap reference
        self.left_pointer, self.right_pointer = mid, mid + gap_size
        for k, char in enumerate(chars):
            if k == mid:
                for _ in range(gap_size):
                    self.append(' ')
            self.append(char)

    def __str__(self):
        # Useful for visualizing the "gap" in the list.
        val = ''
        for k, char in enumerate(self):
            if k == self.left_pointer:
                val += '['
            elif k == self.right_pointer:
                val += ']'
            val += char
        return val

    def move(self, count):
        # "Wrap around if the count is too high"
        if self.left_pointer + count >= len(self):
            self.left_pointer = count
            self.right_pointer = count + self.gap_size
        elif self.right_pointer + count >= len(self):
            diff = self.right_pointer - len(self)
            self.right_pointer = diff
            self.left_pointer = len(self) - diff
        else:
            self.left_pointer += count
            self.right_pointer += count
        print(self)


if DEBUG:
    with Section('Gap Buffer'):
        test_sentence = raw_input('Enter some starting text: ')
        if test_sentence == '':
            test_sentence = 'Hello world, how are you today?'
        gbuff = GapBuffer(test_sentence)
        print(gbuff)
        for n in range(20):
            gbuff.move(n)
