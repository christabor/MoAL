# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section
from helpers.display import divider
from data_structures.abstract.tree import Tree

DEBUG = True if __name__ == '__main__' else False


class BinaryDecisionDiagram(Tree):

    def decide(self, start, end):

        def _conv(val):
            return 1 if val else 0

        v = self._dfs(start, end)
        if 'decision' in v:
            if DEBUG:
                path = self.walk(start, end)
                rows = [self[vert]['val'] for vert
                        in path if self[vert]['val']] + ['result']
                vals = [_conv(self[vert]['bool']) for vert
                        in path if self[vert]['val']]
                vals = vals + [v['decision']]
                print(' | '.join(map(str, rows)))
                print('-' * 80)
                print('  | '.join(map(str, vals)))
                divider('#', newline=False)
            return v['decision']
        else:
            raise ValueError('Invalid decision node.')

if DEBUG:
    with Section('Binary Decision Diagram'):
        bdd = BinaryDecisionDiagram({
            0: {'edges': [1, 2], 'val': 'x1', 'is_root': True, 'bool': None},
            1: {'edges': [3, 4], 'val': 'x2', 'bool': False},
            2: {'edges': [5, 6], 'val': 'x2', 'bool': True},
            3: {'edges': [7, 8], 'val': 'x3', 'bool': False},
            4: {'edges': [9, 10], 'val': 'x3', 'bool': True},
            5: {'edges': [11, 12], 'val': 'x3', 'bool': False},
            6: {'edges': [13, 14], 'val': 'x3', 'bool': True},
            # Leaf "decision" nodes
            7: {'edges': [], 'decision': True},
            8: {'edges': [], 'decision': False},
            9: {'edges': [], 'decision': False},
            10: {'edges': [], 'decision': True},
            11: {'edges': [], 'decision': False},
            12: {'edges': [], 'decision': False},
            13: {'edges': [], 'decision': True},
            14: {'edges': [], 'decision': True},
        })
        print(bdd)
        assert bdd.total_height() == 4
        res = bdd.walk(0, 14)
        print(res)

        assert not bdd[1]['bool']
        assert bdd[2]['bool']
        assert not bdd[3]['bool']
        assert bdd[4]['bool']

        assert bdd.decide(0, 7)
        assert bdd.decide(0, 10)
        assert bdd.decide(0, 13)
        assert bdd.decide(0, 14)

        assert not bdd.decide(0, 8)
        assert not bdd.decide(0, 9)
        assert not bdd.decide(0, 11)
        assert not bdd.decide(0, 12)
