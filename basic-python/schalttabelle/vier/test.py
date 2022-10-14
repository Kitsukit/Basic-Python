import unittest

from schalttabelle.vier.main import schalttabelle_ausfüllen


class AusfüllenVierTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(AusfüllenVierTest, self).__init__(*args, **kwargs)

    @staticmethod
    def test_1():
        schalttabelle_ausfüllen("not a or not b and c or not d")

    @staticmethod
    def test_2():
        schalttabelle_ausfüllen("not(a or not b) and c or not d")
