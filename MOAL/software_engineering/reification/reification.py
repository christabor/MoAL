# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.display import print_h2
from MOAL.helpers.display import firstcaps
from pprint import pprint as ppr
from nltk import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


DEBUG = True if __name__ == '__main__' else False

stemmer = PorterStemmer()


class Car:

    def __init__(self, **kwargs):
        self.props = kwargs

    def drive(self, start, end):
        print('Driving to {} from {}'.format(end, start))

    def stop(self):
        pass

    def start(self):
        pass

    def signal(self, direction):
        print('Turning towards the {}'.format(direction))

    def toggle_status_light(self, light_type):
        print('Toggling status {}'.format(light_type))


class Plane:

    def fly(self):
        pass

    def engage_landing_gear(self):
        pass

    def adjust_rudder(self):
        pass

    def initiate_descent(self):
        pass

    def report_fuel(self):
        pass

    def engage_fuel_reserves(self):
        pass

    def report_temperature(self):
        pass

    def report_wind(self):
        pass

    def initiate_ascent(self):
        pass

    def signal_to_command(self):
        pass

    def adjust_heading(self):
        pass

    def bank(self):
        pass

    def slip(self):
        pass

    def adjust_roll(self, amount):
        print('Adjusting roll by {} units'.format(amount))

    def adjust_pitch(self, amount):
        print('Adjusting pitch by {} units'.format(amount))

    def adjust_yaw(self, direction, amount):
        print('Adjusting yaw towards {} by {} units'.format(direction, amount))


class Fish:

    def swim(self):
        pass

    def feed(self):
        pass

    def flee(self):
        pass


class Recipe:

    def __init__(self, steps):
        self.steps = steps

    def execute(self):
        for k, step in enumerate(self.steps):
            print('Step #{}: {}\n'.format(k + 1, step))


class NaiveReificationScaffolder:
    """Using NLP (via NLTK), we could potentiall reify concepts
    into software dynamically, if the program was smart enough."""

    data = ""
    entity = None

    def parse(self, sentence):
        tokens = word_tokenize(sentence)
        stop_words = stopwords.words('english')
        tokens = list(set([t for t in tokens if t.lower() not in stop_words]))
        parts = pos_tag(tokens)
        ppr(parts)
        self.tokens = tokens
        self.parts = parts
        return self

    def generate(self):
        entity_generated = False
        indent = ' ' * 8

        for part in self.parts:
            val, pos = part
            if pos == 'NN' and not entity_generated:
                self.entity = firstcaps(val)
                self.data = """class {}:\n{}\n""".format(
                    self.entity,
                    '{}# The generated value for {}'.format(
                        ' ' * 4, self.entity))
                self.data += ('\n    def __init__(self, *args, **kwargs):'
                              '\n{}pass\n'.format(indent))
                entity_generated = True
            elif pos in ['VB', 'VBP', 'NNS', 'VBZ']:
                val = stemmer.stem(val.lower())
                self.data += ('\n    def {}(self, *args, **kwargs):\n'
                              '{}pass\n').format(val, indent)
        print('--------- Model ------------\n{}'.format(self.data))
        return self


if DEBUG:
    with Section('Reification - concrete examples'):
        # Most of the examples above can be demonstrated without instantiation,
        # since the idea is simply to show how one can take a concept
        # and convert it into a real assemblage of code.
        print_h2('Reification of processes: A baking recipe')
        # http://m.allrecipes.com/recipe/22850/chewy-sugar-cookies/
        cookies = Recipe([
            ('Preheat oven to 350 degrees F (175 degrees C). In a medium bowl, '
             'stir together the flour, baking soda, and salt; set aside.'),
            ('In a large bowl, cream together the margarine and 2 cups sugar '
             'until light and fluffy. Beat in the eggs one at a time, then the '
             'vanilla. Gradually stir in the dry ingredients until just '
             'blended. Roll the dough into walnut sized balls and roll the '
             'balls in remaining 1/4 cup of sugar. Place cookies 2 inches apart'
             ' onto ungreased cookie sheets and flatten slightly.'),
            ('Bake for 8 to 10 minutes in the preheated oven, until lightly '
             'browned at the edges. Allow cookies to cool on baking sheet for '
             '5 minutes before removing to a wire rack to cool completely.'),
        ])
        cookies.execute()

        print_h2('Dynamic Reification using naive Natural Language Processing')
        reif = NaiveReificationScaffolder()
        text = ('A shark is an animal that hunts in the ocean and swims fast.')
        reif.parse(text).generate()

        text = ('A car is a thing that drives from one place to another. '
                'It can also stop, start, and honk.')
        reif.parse(text).generate()

        text = 'A plane is a transport that can fly in the sky and hold people.'
        reif.parse(text).generate()
