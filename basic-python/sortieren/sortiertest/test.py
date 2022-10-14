import unittest
from random import randint

from sortieren.sortiertest.main import sortiertest


def generate_ascending():
    return sorted([randint(0, 1000) for x in range(1000)])


def generate_descending():
    return sorted([randint(0, 1000) for x in range(1000)], reverse=True)


def generate_same():
    return [randint(0, 1000)] * 1000


class SortierTest(unittest.TestCase):
    def test_ascending(self):
        for i in range(1000):
            self.assertEqual(1, sortiertest(generate_ascending()))

    def test_descending(self):
        for i in range(1000):
            self.assertEqual(2, sortiertest(generate_descending()))

    def test_same(self):
        for i in range(1000):
            self.assertEqual(3, sortiertest(generate_same()))
