import unittest
from MOAL.helpers import adts

"""
MUTATION TESTING:
Uses https://miketeo.net/wp/index.php/projects/python-mutant-testing-pymutester
to inject mutant tests after nose runs the first batch.

Runs with:
`mutant-nosetests --mutant-path MOAL/helpers/tests`
"""


class StrictListInitTest(unittest.TestCase):

    def test_strlist(self):
        _list = adts.strlist(['a', 'b', 'c'])
        expected = ['a', 'b', 'c']
        for k, val in enumerate(_list):
            self.assertEqual(_list[k], expected[k])

    def test_strlist_extra(self):
        _list = adts.strlist(['a', 'b', 'c', 1, 2])
        expected = ['a', 'b', 'c']
        for k, val in enumerate(_list):
            self.assertEqual(_list[k], expected[k])

    def test_intlist(self):
        _list = adts.intlist([1, 2, 3, 4])
        expected = [1, 2, 3, 4]
        for k, val in enumerate(_list):
            self.assertEqual(_list[k], expected[k])

    def test_intlist_extra(self):
        _list = adts.intlist([1, 2, 3, 4, 'cats'])
        expected = [1, 2, 3, 4]
        for k, val in enumerate(_list):
            self.assertEqual(_list[k], expected[k])

    def test_floatlist(self):
        _list = adts.strictlist([0.1, 0.2, 0.3], valid_type=float)
        expected = [0.1, 0.2, 0.3]
        for k, val in enumerate(_list):
            self.assertEqual(_list[k], expected[k])

    def test_floatlist_extra(self):
        _list = adts.strictlist([0.1, 0.2, 0.3, 'cats', 0, 1, 2],
                                valid_type=float)
        expected = [0.1, 0.2, 0.3]
        for k, val in enumerate(_list):
            self.assertEqual(_list[k], expected[k])


class StrListMethodsTest(unittest.TestCase):

    def test_copy(self):
        _list = adts.strlist(['foo', 'bar'])
        _list.copy(2)
        expected = ['foofoo', 'barbar']
        for k, val in enumerate(_list):
            self.assertEqual(_list[k], expected[k])

    def test_add(self):
        _list = adts.strlist(['foo', 'bar'])
        _list.add('2')
        expected = ['foo2', 'bar2']
        for k, val in enumerate(_list):
            self.assertEqual(_list[k], expected[k])

    def test_up(self):
        _list = adts.strlist(['foo', 'bar'])
        _list.up()
        expected = ['FOO', 'BAR']
        for k, val in enumerate(_list):
            self.assertEqual(_list[k], expected[k])

    def test_down(self):
        _list = adts.strlist(['FOO', 'BAR'])
        _list.lo()
        expected = ['foo', 'bar']
        for k, val in enumerate(_list):
            self.assertEqual(_list[k], expected[k])

    def test_reverse(self):
        _list = adts.strlist(['foo', 'bar'])
        _list.reverse()
        expected = ['oof', 'rab']
        for k, val in enumerate(_list):
            self.assertEqual(_list[k], expected[k])

    def test_split(self):
        _list = adts.strlist(['foo', 'bar'])
        _list.split()
        expected = [['f', 'o', 'o'], ['b', 'a', 'r']]
        for k, val in enumerate(_list):
            self.assertEqual(_list[k], expected[k])


class IntListMethodsTest(unittest.TestCase):
    pass


class OneOffTest(unittest.TestCase):

    def test_list_fill(self):
        pass

    def test_dict_fill(self):
        pass

    def test_matrix_fill(self):
        pass
