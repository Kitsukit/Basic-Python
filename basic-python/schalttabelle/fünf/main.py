from schalttabelle.eins.main import binärliste


def schalttabelle_ausfüllen(logischer_term, eingänge):
    if eingänge != 2 and eingänge != 3 and eingänge != 4:
        print("Die Eingänge können nur 2, 3 oder 4 betragen.")
        return

    testdaten = binärliste(eingänge)
    for zeile in range(2 ** eingänge):
        if eingänge == 2:
            a = int(testdaten[zeile][0])
            b = int(testdaten[zeile][1])
            q = int(eval(logischer_term))
            print(a, b, "gibt", q)
        elif eingänge == 3:
            a = int(testdaten[zeile][0])
            b = int(testdaten[zeile][1])
            c = int(testdaten[zeile][2])
            q = int(eval(logischer_term))
            print(a, b, c, "gibt", q)
        elif eingänge == 4:
            a = int(testdaten[zeile][0])
            b = int(testdaten[zeile][1])
            c = int(testdaten[zeile][2])
            d = int(testdaten[zeile][3])
            q = int(eval(logischer_term))
            print(a, b, c, d, "gibt", q)
