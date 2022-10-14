import unittest

from schalttabelle.zwei.main import schalttabelle_ausfüllen


class AusfüllenZweiTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(AusfüllenZweiTest, self).__init__(*args, **kwargs)

    @staticmethod
    def test_1():
        schalttabelle_ausfüllen("not a or not b")

    @staticmethod
    def test_2():
        schalttabelle_ausfüllen("not(a or not b)")
