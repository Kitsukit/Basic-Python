import unittest

from datenstrukturen.queue.main import Queue


class QueueTest(unittest.TestCase):
    def test_1(self):
        queue = Queue(3)
        self.assertEqual(queue.speicher, ["#", "#", "#"])
        self.assertEqual(queue.ablage_platz, 0)
        self.assertEqual(queue.abnahme_platz, 0)
        self.assertEqual(queue.länge, 3)

    def test_2(self):
        queue = Queue(3)
        self.assertFalse(queue.get())
        self.assertEqual(queue.ablage_platz, 0)
        self.assertEqual(queue.abnahme_platz, 0)

    def test_3(self):
        queue = Queue(3)
        queue.put(1)
        queue.put(2)
        queue.put(3)
        self.assertFalse(queue.put(4))
        self.assertEqual(queue.ablage_platz, 0)
        self.assertEqual(queue.abnahme_platz, 0)

    def test_4(self):
        queue = Queue(3)
        queue.put(1)
        queue.put(2)
        queue.get()
        queue.put(3)
        queue.put(4)
        self.assertEqual(queue.get(), 2)
        self.assertEqual(queue.get(), 3)
        self.assertEqual(queue.get(), 4)
        self.assertEqual(queue.ablage_platz, 1)
        self.assertEqual(queue.abnahme_platz, 1)
