class Konto:
    def __init__(self, name, kontostand):
        self.name = name
        self.kontostand = kontostand

    def info(self):
        print("Ich das Konto von", self.name, "mit", self.kontostand, "Euro.")

    def einzahlen(self, betrag):
        self.kontostand = self.kontostand + betrag
        print("Ich bin gewachsen auf", self.kontostand, "um", betrag, "Euro.")

    def abheben(self, betrag):
        if self.kontostand - betrag < 0:
            print("Du kannst dein Konto nicht überziehen.")
            return

        self.kontostand = self.kontostand - betrag
        print("Ich bin geschrumpft auf", self.kontostand, "um", betrag, "Euro.")
