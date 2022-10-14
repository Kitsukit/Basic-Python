import unittest

from schalttabelle.eins.main import binärliste


class BinärlisteTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(BinärlisteTest, self).__init__(*args, **kwargs)

    def test_1(self):
        ergebnis = binärliste(1)
        print(ergebnis)
        self.assertEqual(ergebnis, ["0", "eins"])

    def test_2(self):
        ergebnis = binärliste(2)
        print(ergebnis)
        self.assertEqual(ergebnis, ["00", "01", "10", "11"])

    def test_3(self):
        ergebnis = binärliste(3)
        print(ergebnis)
        self.assertEqual(ergebnis, ["000", "001", "010", "011", "100", "101", "110",
                                    "111"])
