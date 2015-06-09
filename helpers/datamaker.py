from random import randrange as rr
from random import choice
from string import ascii_uppercase


def random_dag():
    max = 10
    letters = [choice(ascii_uppercase) for _ in range(max)]
    dag = {}
    nums = range(max)
    for k, letter in enumerate(letters):
        dag[k] = {
            'edges': [choice(nums) for _ in range(rr(0, max))],
            'val': choice(letter)
        }
    return dag
