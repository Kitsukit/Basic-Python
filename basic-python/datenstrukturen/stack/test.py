import unittest

from datenstrukturen.stack.main import Stack


class StackTest(unittest.TestCase):
    def test_1(self):
        stack = Stack(3)
        self.assertEqual(stack.speicher, ["#", "#", "#"])
        self.assertEqual(stack.ablage_platz, 0)
        self.assertEqual(stack.länge, 3)

    def test_2(self):
        stack = Stack(3)
        self.assertFalse(stack.get())
        self.assertEqual(stack.ablage_platz, 0)

    def test_3(self):
        stack = Stack(3)
        stack.put(1)
        stack.put(2)
        stack.put(3)
        self.assertFalse(stack.put(4))
        self.assertEqual(stack.ablage_platz, 3)

    def test_4(self):
        stack = Stack(3)
        stack.put(1)
        stack.put(2)
        stack.put(3)
        stack.get()
        stack.get()
        stack.put(4)
        stack.put(5)
        self.assertEqual(stack.speicher, [1, 4, 5])
        self.assertEqual(stack.ablage_platz, 3)
