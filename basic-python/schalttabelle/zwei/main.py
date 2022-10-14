from schalttabelle.eins.main import binärliste


def schalttabelle_ausfüllen(logischer_term):
    # Gibt den Term nochmals aus.
    print(logischer_term)
    # Erstellt die testdaten für 2bit.
    testdaten = binärliste(2)
    # Durchläuft diese Schleife 4x.
    for zeile in range(4):
        # Speichert den ersten boolschen Wert der Testdaten an der Stelle "zeile" in die
        # Variable "a" ab.
        a = int(testdaten[zeile][0])
        # Speichert den zweiten boolschen Wert der Testdaten an der Stelle "zeile" in die
        # Variable "b" ab.
        b = int(testdaten[zeile][1])
        # Die Funktion eval(term) führt einen angegebenen Term aus. Da dieser die
        # Variablen "a" und "b" enthält, werden die Variablen, welche zuvor erstellt
        # wurden, benutzt. Das Ergebnis des Terms wird dann in die Variable "q"
        # abgespeichert.
        q = int(eval(logischer_term))
        # Gibt das Ergebnis aus.
        print(a, b, "gibt", q)
