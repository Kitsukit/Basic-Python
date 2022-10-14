class Ringspeicher:
    def __init__(self, länge):
        self.länge = länge

        # Initialisiert eine Liste der Länge "self.länge", die mit "#" aufgefüllt wird.
        self.speicher = []
        for i in range(self.länge):
            self.speicher.append("#")

        # Da das erste Element auf dem ersten Index abgespeichert werden soll,
        # wird diese Variable auf "0" gesetzt.
        self.ablage_platz = 0

    def bild_speichern(self, daten):
        """
        Mit dieser Methode können Daten abgespeichert werden. Liegen auf dem derzeitigen
        Ablageplatz bereits Daten vor, werden diese überschrieben.
        """

        # Speichert die angegebenen Daten auf dem derzeitigen Ablageplatz.
        self.speicher[self.ablage_platz] = daten
        # Erhöht den Ablageplatz um eins.
        self.ablage_platz = self.ablage_platz + 1
        # Falls der Ablageplatz die Länge der Liste überschreitet, wird dieser wieder
        # an den Anfang, also "0", gesetzt.
        if self.ablage_platz == self.länge:
            self.ablage_platz = 0

    def bilder_zeigen(self):
        """
        Diese Methode zeigt uns alle Daten an, welche wir gespeichert haben. Dabei
        werden die ältesten als erstes ausgegeben und die neueren zuletzt.
        """
        # Da wir zuerst die ältesten Daten ausgeben müssen, besteht die Range aus dem
        # Anfang "Ablageplatz" und dem Ende "Länge". Dies ergibt sich dadurch, dass der
        # derzeitige Ablageplatz die ältesten Daten besitzt, da wir diese ja überschreiben
        # wollen.
        # Zusätzlich prüfen wir, ob an dem Index überhaupt Daten vorliegen. Dies ist
        # nicht der Fall, falls "daten" ein "#" ist.
        for i in range(self.ablage_platz, self.länge):
            daten = self.speicher[i]
            if not daten == "#":
                print(daten)

        # Die neusten Daten werden nun mithilfe der Range aus dem Anfang von "0" und
        # dem Ende "Ablageplatz" ausgegeben. Da wir in der vorherigen Schleife alle
        # Elemente bis zum Ende der Liste ausgegeben haben, ist der Anfang nun der
        # Index "0". Die Schleife geht dann alle Indizes bis zum Ablageplatz durch.
        # Somit werden auch die letzten Elemente der Liste ausgegeben.
        # Wie auch in der Schleife zuvor wird geschaut, ob auch Daten hinterlegt sind.
        for i in range(0, self.ablage_platz):
            daten = self.speicher[i]
            if not daten == "#":
                print(daten)

    def reset(self):
        """
        Setzt den Speicher zurück und somit auch die Variablen auf den Anfangszustand.
        Der Speicher wird komplett überschrieben und der Ablageplatz wieder auf 0
        gesetzt.
        """
        # Erstellt eine Liste der Länge "self.länge", die mit "#" aufgefüllt wird.
        self.speicher = []
        for i in range(self.länge):
            self.speicher.append("#")

        # Da das erste Element auf dem ersten Index abgespeichert werden soll,
        # wird diese Variable auf "0" gesetzt.
        self.ablage_platz = 0
