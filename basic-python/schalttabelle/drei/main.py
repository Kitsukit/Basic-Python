from schalttabelle.eins.main import binärliste


def schalttabelle_ausfüllen(logischer_term):
    testdaten = binärliste(3)
    for zeile in range(2 ** 3):
        a = int(testdaten[zeile][0])
        b = int(testdaten[zeile][1])
        c = int(testdaten[zeile][2])
        q = int(eval(logischer_term))
        print(a, b, c, "gibt", q)
