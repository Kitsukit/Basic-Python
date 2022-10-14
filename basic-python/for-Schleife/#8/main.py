zeichenkette = input("Gib zufällige Zeichen ein: ")
suchzeichen = input("Gib ein Zeichen ein:")

anzahl = 0
for stelle in range(len(zeichenkette)):
    if suchzeichen == zeichenkette[stelle]:
        anzahl = anzahl + 1
        print(suchzeichen, "steht an Stelle", stelle)

print("Es kommt", anzahl, "mal vor")
