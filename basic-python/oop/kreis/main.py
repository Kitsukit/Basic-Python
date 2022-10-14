class Kreis:
    def __init__(self, name, durchmesser):
        self.name = name
        self.durchmesser = durchmesser

    def fläche(self):
        fläche = (3.141 * self.durchmesser ** 2) / 4
        print("Die Fläche beträgt", fläche, "mm².")

    def umfang(self):
        umfang = 3.141 * self.durchmesser
        print("Der Umfang beträgt", umfang, "mm.")

    def info(self):
        print("Ich bin Kreis", self.name, "mit einem Durchmesser von", self.durchmesser, "mm.")

    def größer(self, zuwachs):
        self.durchmesser = self.durchmesser + zuwachs
        print("Ich bin gewachsen auf", self.durchmesser, "um", zuwachs, "mm.")

    def kleiner(self, schwund):
        if self.durchmesser - schwund <= 0:
            print("Der Durchmesser kann nicht kleiner gleich 0 sein.")
            return

        self.durchmesser = self.durchmesser - schwund
        print("Ich bin geschrumpft auf", self.durchmesser, "um", schwund, "mm.")
