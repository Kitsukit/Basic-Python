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

minimum = 100
for i in range(länge):
    if liste[i] < minimum:
        minimum = liste[i]

print("Das Minimum der Liste beträgt:", minimum)

mittelwert = 0
for i in range(länge):
    mittelwert = mittelwert + liste[i]
mittelwert = mittelwert / länge

print("Der Mittelwert der Liste beträgt:", mittelwert)

