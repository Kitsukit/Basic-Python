class Queue:
    def __init__(self, länge):
        self.länge = länge

        # Initialisiert eine Liste der Länge "self.länge", die mit "#" aufgefüllt wird.
        self.speicher = []
        for i in range(self.länge):
            self.speicher.append("#")

        # Da der erste Ablageplatz auf Index 0 sein soll, wird dieser hier gesetzt.
        self.ablage_platz = 0
        # Am Anfang stimmt der Abnehmeplatz mit dem Ablageplatz überein.
        self.abnahme_platz = 0

    def put(self, daten):
        """
        Mit dem Aufrufen dieser Methode werden die angegebenen Daten an dem derzeitgen
        Ablageplatz abgespeichert. Falls der Speicher voll ist, wird eine
        Fehlernachricht ausgegeben. Überschreitet der Ablageplatz die Länge der Liste,
        wird dieser wieder auf "0" gesetzt.
        """

        # Sind an dem derzeitigen Ablageplatz Daten vorhanden, also kein "#", ist der
        # Speicher voll und eine Fehlernachricht wird ausgegeben. Zudem wird "False"
        # zurückgegeben für den späteren Verlauf.
        if self.speicher[self.ablage_platz] != "#":
            print("Der Speicher ist voll.")
            return False

        # An dem derzeitigen Ablageplatz werden die Daten abgelegt.
        self.speicher[self.ablage_platz] = daten
        # Der Ablageplatz erhöht sich um eins.
        self.ablage_platz = self.ablage_platz + 1
        # Falls der Ablageplatz die Länge der Liste überschreitet, wird dieser wieder
        # an den Anfang, also "0", gesetzt.
        if self.ablage_platz == self.länge:
            self.ablage_platz = 0

    def get(self):
        """
        Diese Methode wird benutzt, um das erste Element des Speichers auszugeben. Das
        erste Element ist hierbei der Älteste, welches je hinzugefügt wurde. Ist der
        Speicher leer, wird eine Fehlernachricht ausgegeben. Überschreitet der
        Abnahmeplatz die Länge der Liste, wird dieser wieder auf "0" gesetzt.
        """

        # Wenn an dem derzeitigen Abnahmeplatz ein "#" vorgefunden wird, ist der
        # Speicher leer. Somit wird eine Fehlernachricht ausgegeben und "False" für den
        # späteren Verlauf zurückgegeben.
        if self.speicher[self.abnahme_platz] == "#":
            print("Der Speicher ist leer.")
            return False

        # Speichert die Daten an dem derzeitigen Abnahmeplatz in die Variable "daten" ab.
        daten = self.speicher[self.abnahme_platz]
        # Überschreibt die Daten an dem derzeitigen Abnahmeplatz mit einem "#".
        self.speicher[self.abnahme_platz] = "#"
        # Erhöht den Abnahmeplatz um eins.
        self.abnahme_platz = self.abnahme_platz + 1
        # Falls der Abnahmeplatz die Länge der Liste überschreitet, wird dieser wieder
        # an den Anfang, also "0", gesetzt.
        if self.abnahme_platz == self.länge:
            self.abnahme_platz = 0

        # Die Daten werden schlussendlich zurückgegeben.
        return daten
