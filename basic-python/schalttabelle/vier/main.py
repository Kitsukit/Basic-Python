from schalttabelle.eins.main import binärliste


def schalttabelle_ausfüllen(logischer_term):
    testdaten = binärliste(4)
    for zeile in range(2 ** 4):
        a = int(testdaten[zeile][0])
        b = int(testdaten[zeile][1])
        c = int(testdaten[zeile][2])
        d = int(testdaten[zeile][3])
        q = int(eval(logischer_term))
        print(a, b, c, d, "gibt", q)
