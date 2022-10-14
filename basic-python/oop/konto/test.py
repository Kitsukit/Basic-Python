import unittest

from oop.konto.main import Konto


class KontoTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(KontoTest, self).__init__(*args, **kwargs)

        self.konto = Konto("Kevin", 200)

    def test_info(self):
        self.konto.info()

    def test_einzahlen(self):
        self.konto.einzahlen(20)

    def test_abheben(self):
        self.konto.abheben(200)

    def test_abheben_error(self):
        self.konto.abheben(210)
