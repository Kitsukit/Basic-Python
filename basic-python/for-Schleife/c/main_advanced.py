zeichenkette = input("Gib zufällige Zeichen ein: ")

anzahl = 0
stellen = []
for stelle in range(len(zeichenkette)):
    if zeichenkette[stelle] == "a":
        anzahl = anzahl + 1
        stellen.append(str(stelle))

if anzahl > 0:
    vorkommen = ""
    if len(stellen) > 1:
        vorkommen = "den Stellen " + ", ".join(stellen[:-1]) + " und " + stellen[-1]
    else:
        vorkommen = "der Stelle " + stellen[-1]
    print("Der Buchstabe a kommt an", vorkommen, "vor")
else:
    print("Der Buchstabe a kommt in dem String", zeichenkette, "nicht vor")
