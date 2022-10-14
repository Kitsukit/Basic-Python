def binärliste(bit):
    # Erstellt eine leere Liste.
    liste_mit_binärzahlen = []
    # Die Berechnung 2^bit ergibt die größte Zahl einer bestimmten Bitanzahl.
    # Hierbei würden 4 bit z.B. 16 ergeben.
    zeilenanzahl = 2 ** bit
    # Die Funktion bin(x) gibt die binäre Representation einer Zahl mit dem Präfix "0b"
    # zurück. Da wir von 0 anfangen zu zählen, wie z.B. von 0 bis 15, müssen wir eins
    # von der "zeilenanzahl" abziehen. Da wir das Präfix nicht benötigen, ziehen wir
    # außerdem zwei Stellen von dem Resultat ab.
    zeichenanzahl = len(bin(zeilenanzahl - 1)) - 2

    # Geht alle Zahlen bis zu dem Maximum "zeilenanzahl" durch.
    for i in range(zeilenanzahl):
        # Speichert die binäre Representation der Zahl in die Variable "binärzahl".
        binärzahl = bin(i)
        # Da wir das Präfix nicht benötigen, "schneiden" wir die ersten zwei Zeichen des
        # Strings ab.
        binärzahl_sauber = binärzahl[2:]
        # Da vorangestellte Nullen nicht ausgegeben werden, wird die Differenz unserer
        # "zeichenanzahl" und der Länge von "binärzahl_sauber" berechnet. So ergibt
        # sich die Differenz der Nullen. Z.B. "zeichenanzahl" -> 3, "binärzahl_sauber"
        # -> "01" (len = 2), ergibt eine Differenz von 1.
        anzahl_fehlender_nullen = zeichenanzahl - len(binärzahl_sauber)
        # Die fehlenden Nullen werden an den Anfang des String angehängt.
        binärzahl_mit_nullen = ("0" * anzahl_fehlender_nullen) + binärzahl_sauber
        # Das Resultat wird in der Liste abgespeichert.
        liste_mit_binärzahlen.append(binärzahl_mit_nullen)

    # Die Liste aller Binärzahlen wird zurückgegeben.
    return liste_mit_binärzahlen
