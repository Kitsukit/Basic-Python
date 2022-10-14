from turtle import *


def tortendiagramm(werte):
    t = Turtle()

    # Generelle Einstellungen
    t.speed(0)
    t.pensize(2)

    # Zuerst den vollen Kreis zeichnen
    t.penup()
    t.goto(0, -300)
    t.pendown()
    t.circle(300)

    # In die Mitte des Kreises bewegen
    t.penup()
    t.goto(0, 0)

    summe = 0
    for (_, wert) in werte:
        summe = summe + wert

    for (name, wert) in werte:
        winkel = (wert / summe) * 360

        # Die erste Linie zeichnen
        t.pendown()
        t.fd(300)

        # Zurück in die Mitte des Kreises bewegen und sich um die Hälfte des
        # ausgerechneten Winkels drehen.
        t.penup()
        t.goto(0, 0)
        t.left(winkel / 2)

        # Auf halber Strecke den Namen für den Wert zeichnen
        t.fd(360)
        t.write(name, align="center", font=("Arial", 18, "bold"))

        # Nochmals in die Mitte des Kreises bewegen und sich um die Hälfte des
        # ausgerechneten Winkels drehen, sodass der volle Winkel zurückgelegt wurde
        t.goto(0, 0)
        t.left(winkel / 2)

    t.hideturtle()
    t.screen.mainloop()


tortendiagramm([["SPD\n26,4%", 26.4], ["CDU\n22,5%", 22.5], ["AfD\n10,eins%", 10.1],
                ["FDP\n8,7%", 8.7], ["LINKE\n5,0%", 5.0], ["GRÜNE\n14,0%", 14.0],
                ["CSU\n6,0%", 6.0], ["Sonstige\n7,3%", 7.3]])
