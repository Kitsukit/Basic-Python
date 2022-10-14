import unittest

from datenstrukturen.ringspeicher.main import Ringspeicher


class RingspeicherTest(unittest.TestCase):
    def test_1(self):
        ringspeicher = Ringspeicher(4)
        self.assertEqual(ringspeicher.speicher, ["#", "#", "#", "#"])
        self.assertEqual(ringspeicher.ablage_platz, 0)
        self.assertEqual(ringspeicher.länge, 4)

    def test_2(self):
        ringspeicher = Ringspeicher(4)
        ringspeicher.bild_speichern("Bild1")
        ringspeicher.bild_speichern("Bild2")
        ringspeicher.bild_speichern("Bild3")
        self.assertEqual(ringspeicher.speicher, ["Bild1", "Bild2", "Bild3", "#"])
        self.assertEqual(ringspeicher.ablage_platz, 3)

    def test_3(self):
        ringspeicher = Ringspeicher(4)
        ringspeicher.bild_speichern("Bild1")
        ringspeicher.bild_speichern("Bild2")
        ringspeicher.bild_speichern("Bild3")
        ringspeicher.bild_speichern("Bild4")
        ringspeicher.bild_speichern("Bild5")
        ringspeicher.bild_speichern("Bild6")
        self.assertEqual(ringspeicher.speicher, ["Bild5", "Bild6", "Bild3", "Bild4"])
        self.assertEqual(ringspeicher.ablage_platz, 2)

    def test_4(self):
        ringspeicher = Ringspeicher(4)
        ringspeicher.bild_speichern("Bild1")
        ringspeicher.bild_speichern("Bild2")
        ringspeicher.bild_speichern("Bild3")
        ringspeicher.reset()
        self.assertEqual(ringspeicher.speicher, ["#", "#", "#", "#"])
        self.assertEqual(ringspeicher.ablage_platz, 0)
