from schalttabelle.eins.main import binärliste
import re


def schalttabelle_ausfüllen(logischer_term):
    # Löscht alle Leerzeichen, "and", "not", "or", "(" oder ")".
    # Das einzige was übrig bleibt sind nun die Variablen.
    # So wird aus "not(b and a or c)" -> "bac".
    term_sauber = re.sub(r"and|not|or|\s|\(|\)", "", logischer_term)
    # Löscht alle Duplikate und ordnet den String.
    # So wird aus "baacd" -> "abcd".
    term_sauber = "".join(dict.fromkeys(term_sauber))
    # Die Anzahl der Variablen wird durch die Länge des sauberen Terms ermittelt.
    variablen_anzahl = len(term_sauber)
    # Die Zeilenanzahl entspricht 2^n.
    # n ist hierbei die Anzahl der Variablen.
    zeilenanzahl = 2 ** variablen_anzahl

    # Die Testdaten mit der Anzahl an Variablen wird erstellt.
    testdaten = binärliste(variablen_anzahl)

    # Speichert die Ergebnise aller Zeilen.
    schalttabelle = []

    # Geht durch alle Zeilen durch.
    for zeile in range(zeilenanzahl):
        # Speichert alle Variablen und das Ergebnis einer Spalte.
        spalten_ergebnis = []
        # Speichert alle Namen und Werte der Variablen um diese nachher auszugeben.
        variablen_ausgabe = ""
        # Speichert die Variablen in einem Dictionary, da dies benötigt wird für die
        # "eval" Funktion.
        variablen = {}
        # Geht alle Variablen durch.
        for variable in range(variablen_anzahl):
            # Bekommt den Namen der Variable aus dem sauberen Term.
            variablen_name = term_sauber[variable]
            # Speichert den Wert der Variable ab, welcher durch die testdaten in der
            # derzeitigen Zeile befindet.
            variablen_wert = int(testdaten[zeile][variable])
            # Speichert den Wert mit dem Variablennamen in das Dictionary.
            variablen[variablen_name] = bool(variablen_wert)
            # Der Wert der Variable wird in die Spalte abgespeichert.
            spalten_ergebnis.append(variablen_wert)
            # Fügt die Variable mit seinem Wert in den String für die Ausgabe.
            variablen_ausgabe = "{0} {1}: {2}".format(variablen_ausgabe, variablen_name,
                                                      variablen_wert)

        # Führt den Term mit den Variablen aus und speichert den Integer-Wert danach
        # in die Variable "ergebnis".
        ergebnis = int(eval(logischer_term, variablen))
        # Zuletzt wird das Ergebnis der Spalte hinzugefügt.
        spalten_ergebnis.append(ergebnis)
        # Die Spalte wird der Schalttablle hinzugefügt.
        schalttabelle.append(spalten_ergebnis)

    # Gibt die Schalttabelle zurück.
    return schalttabelle
