class Stack:
    def __init__(self, länge):
        self.länge = länge

        # Initialisiert eine Liste der Länge "self.länge", die mit "#" aufgefüllt wird.
        self.speicher = []
        for i in range(self.länge):
            self.speicher.append("#")

        # Da der erste Ablageplatz auf Index 0 sein soll, wird dieser hier gesetzt.
        self.ablage_platz = 0

    def put(self, daten):
        """
        Beim Aufrufen dieser Methode werden die angegebenen Daten in den Stack
        abgespeichert. Falls dieser voll ist, wird eine Fehlernachricht ausgegeben.
        """

        # Ist der Ablageplatz genauso groß wie die Größe der Liste, ist der Speicher
        # voll und es wird eine Fehlernachricht ausgegeben. Außerdem wird "False"
        # zurückgegeben.
        if self.ablage_platz == self.länge:
            print("Der Speicher ist voll.")
            return False

        # Die Daten werden an dem derzeitigen Ablageplatz abgespeichert.
        self.speicher[self.ablage_platz] = daten
        # Der Ablageplatz wird um eins erhöht, da die Daten auf dem derzeitigen Platz
        # geschrieben wurden.
        self.ablage_platz = self.ablage_platz + 1

    def get(self):
        """
        Diese Methode gibt das zuletzt hinzugefügte Element zurück, falls der Speicher
        nicht leer ist. Die derzeitigen Daten werden außerdem zurückgegeben und diese an
        dem Platz in der Liste mit einem "#" überschrieben.
        """

        # Ist der Ablageplatz gleich 0, ist die Liste leer und eine Fehlernachricht
        # wird ausgegeben. Außerdem wird für den späteren Verlauf noch "False"
        # zurückgegeben.
        if self.ablage_platz == 0:
            print("Der Speicher ist leer.")
            return False

        # Der Ablageplatz wird um eins verringert, da sich dort nicht die letzten Daten
        # befinden.
        self.ablage_platz = self.ablage_platz - 1
        # Die abgespeicherten Daten werden ausgelesen und in der Variable "daten"
        # abgespeichert.
        daten = self.speicher[self.ablage_platz]
        # An dem derzeitigen Ablageplatz werden die Daten mit einem "#" überschrieben.
        self.speicher[self.ablage_platz] = "#"

        # Die Daten werden schlussendlich zurückgegeben.
        return daten
