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
