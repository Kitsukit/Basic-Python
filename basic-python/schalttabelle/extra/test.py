import unittest

from schalttabelle.extra.main import schalttabelle_ausfüllen


class AusfüllenExtraTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(AusfüllenExtraTest, self).__init__(*args, **kwargs)

    def test_1(self):
        term_lang = schalttabelle_ausfüllen("not(not a and (b or not b) or b and a)")
        term_kurz = schalttabelle_ausfüllen("a and not b")
        self.assertEqual(term_lang, term_kurz)
        self.assertEqual(term_kurz, [
            [0, 0, 0],
            [0, 1, 0],
            [1, 0, 1],
            [1, 1, 0]
        ])
