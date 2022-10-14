import unittest

from schalttabelle.drei.main import schalttabelle_ausfüllen


class AusfüllenDreiTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(AusfüllenDreiTest, self).__init__(*args, **kwargs)

    @staticmethod
    def test_1():
        schalttabelle_ausfüllen("not a or not b and c")

    @staticmethod
    def test_2():
        schalttabelle_ausfüllen("not(a or not b) and c")
