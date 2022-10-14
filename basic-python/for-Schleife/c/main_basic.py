zeichenkette = input("Gib zufällige Zeichen ein: ")

anzahl = 0
for stelle in range(len(zeichenkette)):
    if zeichenkette[stelle] == "a":
        anzahl = anzahl + 1
        print("a steht an Stelle", stelle)

if anzahl > 0:
    print("Der Buchstabe a kommt", anzahl, "mal in dem String", zeichenkette, "vor")
else:
    print("Der Buchstabe a kommt in dem String", zeichenkette, "nicht vor")
