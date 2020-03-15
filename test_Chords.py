from unittest import TestCase
from ChordId import get_interval


class TestChords(TestCase):
    def test_get_interval(self):
        all_interval_pairs = {('db', 'd'): 'b2', ('db', 'eb'): '2', ('db', 'e'): 'b3', ('db', 'f'): '3',
                              ('db', 'gb'): '4', ('db', 'g'): 'b5', ('db', 'ab'): '5', ('db', 'a'): 'b6',
                              ('db', 'bb'): '6', ('db', 'b'): 'b7', ('db', 'c'): '7', ('d', 'eb'): 'b2',
                              ('d', 'e'): '2', ('d', 'f'): 'b3', ('d', 'gb'): '3', ('d', 'g'): '4', ('d', 'ab'): 'b5',
                              ('d', 'a'): '5', ('d', 'bb'): 'b6', ('d', 'b'): '6', ('d', 'c'): 'b7', ('d', 'db'): '7',
                              ('eb', 'e'): 'b2', ('eb', 'f'): '2', ('eb', 'gb'): 'b3', ('eb', 'g'): '3',
                              ('eb', 'ab'): '4', ('eb', 'a'): 'b5', ('eb', 'bb'): '5', ('eb', 'b'): 'b6',
                              ('eb', 'c'): '6', ('eb', 'db'): 'b7', ('eb', 'd'): '7', ('e', 'f'): 'b2',
                              ('e', 'gb'): '2', ('e', 'g'): 'b3', ('e', 'ab'): '3', ('e', 'a'): '4', ('e', 'bb'): 'b5',
                              ('e', 'b'): '5', ('e', 'c'): 'b6', ('e', 'db'): '6', ('e', 'd'): 'b7', ('e', 'eb'): '7',
                              ('f', 'gb'): 'b2', ('f', 'g'): '2', ('f', 'ab'): 'b3', ('f', 'a'): '3', ('f', 'bb'): '4',
                              ('f', 'b'): 'b5', ('f', 'c'): '5', ('f', 'db'): 'b6', ('f', 'd'): '6', ('f', 'eb'): 'b7',
                              ('f', 'e'): '7', ('gb', 'g'): 'b2', ('gb', 'ab'): '2', ('gb', 'a'): 'b3',
                              ('gb', 'bb'): '3', ('gb', 'b'): '4', ('gb', 'c'): 'b5', ('gb', 'db'): '5',
                              ('gb', 'd'): 'b6', ('gb', 'eb'): '6', ('gb', 'e'): 'b7', ('gb', 'f'): '7',
                              ('g', 'ab'): 'b2', ('g', 'a'): '2', ('g', 'bb'): 'b3', ('g', 'b'): '3', ('g', 'c'): '4',
                              ('g', 'db'): 'b5', ('g', 'd'): '5', ('g', 'eb'): 'b6', ('g', 'e'): '6', ('g', 'f'): 'b7',
                              ('g', 'gb'): '7', ('ab', 'a'): 'b2', ('ab', 'bb'): '2', ('ab', 'b'): 'b3',
                              ('ab', 'c'): '3', ('ab', 'db'): '4', ('ab', 'd'): 'b5', ('ab', 'eb'): '5',
                              ('ab', 'e'): 'b6', ('ab', 'f'): '6', ('ab', 'gb'): 'b7', ('ab', 'g'): '7',
                              ('a', 'bb'): 'b2', ('a', 'b'): '2', ('a', 'c'): 'b3', ('a', 'db'): '3', ('a', 'd'): '4',
                              ('a', 'eb'): 'b5', ('a', 'e'): '5', ('a', 'f'): 'b6', ('a', 'gb'): '6', ('a', 'g'): 'b7',
                              ('a', 'ab'): '7', ('bb', 'b'): 'b2', ('bb', 'c'): '2', ('bb', 'db'): 'b3',
                              ('bb', 'd'): '3', ('bb', 'eb'): '4', ('bb', 'e'): 'b5', ('bb', 'f'): '5',
                              ('bb', 'gb'): 'b6', ('bb', 'g'): '6', ('bb', 'ab'): 'b7', ('bb', 'a'): '7',
                              ('b', 'c'): 'b2', ('b', 'db'): '2', ('b', 'd'): 'b3', ('b', 'eb'): '3', ('b', 'e'): '4',
                              ('b', 'f'): 'b5', ('b', 'gb'): '5', ('b', 'g'): 'b6', ('b', 'ab'): '6', ('b', 'a'): 'b7',
                              ('b', 'bb'): '7', ('c', 'db'): 'b2', ('c', 'd'): '2', ('c', 'eb'): 'b3', ('c', 'e'): '3',
                              ('c', 'f'): '4', ('c', 'gb'): 'b5', ('c', 'g'): '5', ('c', 'ab'): 'b6', ('c', 'a'): '6',
                              ('c', 'bb'): 'b7', ('c', 'b'): '7'}
        for key, val in all_interval_pairs.items():
            print(key, val)
            self.assertEqual(val, get_interval(key[0], key[1]))


# generate all interval pairs
all_interval_pairs = {}
notes = ['c', 'db', 'd', 'eb', 'e', 'f', 'gb', 'g', 'ab', 'a', 'bb', 'b']
intervals = {1: 'b2', 2: '2', 3: 'b3', 4: '3',
             5: '4', 6: 'b5', 7: '5', 8: 'b6',
             9: '6', 10: 'b7', 11: '7', }

for i in range(12):
    notes = notes[1:] + notes[:1]  # rotate 1 position to the left
    for j in range(1, len(notes)):
        all_interval_pairs[(notes[0], notes[j])] = intervals[j]
print(all_interval_pairs)
