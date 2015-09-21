# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.display import print_h2
from sklearn import tree
from pprint import pprint as ppr

DEBUG = True if __name__ == '__main__' else False


def run_predictions(tree, max=20):
    # Then use it to predict the next input
    for x in range(-max, 0) + range(0, max):
        v1, v2, v3, v4 = x * 0.1, x * 0.2, x * 0.3, x * 2.0
        prediction = dec_tree.predict([v1, v2, v3])
        print('Values: {} -> Prediction: {}'.format((
            v1, v2, v3, v4), prediction))


if DEBUG:
    with Section('Artificial Intelligence - Decision Trees'):
        """See http://scikit-learn.org/stable/modules/tree.html for info.

        RULE OF THUMB:
        Classification = ClassificationTree
        Prediction = RegressionTreee
        """

        training = [
            [0, 0, 0],
            [1, 1, 1],
            [2, 2, 2],
            [4, 4, 4],
            [10, 10, 10]
        ]
        labels = ['thing0', 'thing1', 'thing2', 'thing4', 'thing10']
        print_h2('Fitting tree with training: {} and labels: {}'.format(
            training, labels))
        dec_tree = tree.DecisionTreeClassifier()
        dec_tree = dec_tree.fit(training, labels)
        run_predictions(tree)

        # ----------------------------------------------------------------------

        training = [
            [32905.00, 1230.00, 4, 4, 32.5, 4],
            [64230.00, 801.00, 4, 4, 29.3, 3],
            [18540.00, 230.00, 4, 4, 27.5, 3],
            [35540.00, 990.00, 2, 2, 22.5, 3],
            [45901.00, 2210.00, 4, 4, 30.0, 5],
        ]
        features = [range(0, 5) for _ in range(5)]
        labels = [
            'buying_price',
            'maintenance_price',
            'num_doors',
            'num_seats',
            'trunk_size',
            'safety_rating']

        print_h2('Fitting tree with training: {} and labels: {}'.format(
            training, labels))
        dec_tree = tree.DecisionTreeClassifier()
        dec_tree = dec_tree.fit(training, features)
        pred = dec_tree.predict([32100, 900, 4, 4, 21.3, 2])
        ppr(pred)
        pred = dec_tree.predict([16400, 300, 4, 4, 18.4, 3])
        ppr(pred)
