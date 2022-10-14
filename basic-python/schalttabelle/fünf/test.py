import unittest

from schalttabelle.fünf.main import schalttabelle_ausfüllen


class AusfüllenFünfTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(AusfüllenFünfTest, self).__init__(*args, **kwargs)

    @staticmethod
    def test_1():
        schalttabelle_ausfüllen("not a or not b", 2)

    @staticmethod
    def test_2():
        schalttabelle_ausfüllen("not(a or not b)", 2)

    @staticmethod
    def test_3():
        schalttabelle_ausfüllen("not a or not b and c", 3)

    @staticmethod
    def test_4():
        schalttabelle_ausfüllen("not(a or not b) and c", 3)

    @staticmethod
    def test_5():
        schalttabelle_ausfüllen("not a or not b and c or not d", 4)

    @staticmethod
    def test_6():
        schalttabelle_ausfüllen("not(a or not b) and c or not d", 4)
