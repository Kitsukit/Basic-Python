import pickle

from random import randint


def schreiben(dateiname, daten):
    datei = open(dateiname, "bw")
    pickle.dump(daten, datei)
    datei.close()


def lesen(dateiname):
    datei = open(dateiname, "rb")
    daten = pickle.load(datei)
    return daten


def zufällige_liste(anzahl):
    liste = []
    for i in range(anzahl):
        liste.append(randint(0, anzahl))
    return liste


def listen_maximum(liste):
    maximum = 0
    for i in range(len(liste)):
        wert = liste[i]
        if wert > maximum:
            maximum = wert
    return maximum


def zufall_maximum():
    liste_generiert = zufällige_liste(10)
    schreiben("zufall.txt", liste_generiert)

    liste_ausgelesen = lesen("zufall.txt")
    maximum = listen_maximum(liste_ausgelesen)

    return maximum
