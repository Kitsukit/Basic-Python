import unittest

from oop.kreis.main import Kreis


class KreisTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(KreisTest, self).__init__(*args, **kwargs)

        self.kreis = Kreis("Klaus", 33)

    def test_info(self):
        self.kreis.info()

    def test_fläche(self):
        self.kreis.fläche()

    def test_größer(self):
        self.kreis.größer(11)

    def test_umfang(self):
        self.kreis.umfang()
