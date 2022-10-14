x = int(input("x: "))

liste_1 = []
liste_2 = []
liste_3 = []
liste_4 = []
for i in range(x):
    liste_1.append(x - i)
    liste_2.append(i)
    liste_3.append(i - x)
    liste_4.append(x)

print(liste_1)
print(liste_2)
print(liste_3)
print(liste_4)
