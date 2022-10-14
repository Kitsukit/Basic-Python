from random import randint

länge = int(input("Gebe die länge der Liste ein: "))

liste = []
for i in range(länge):
    liste.append(randint(0, 100))

print("Die Liste enthält diese Werte: ", liste)

maximum = 0
for i in range(länge):
    if liste[i] > maximum:
        maximum = liste[i]

print("Das Maximum der Liste beträgt:", maximum)
