from tkinter import *
from tkinter import messagebox


def nachricht_anzeigen():
    messagebox.showinfo(message="Hallo?")


fenster = Tk()
fenster.title("Guten Tag!")

info = Label(fenster, text="Klick doch mal!")

box_anzeigen_button = Button(fenster, text="Drück mich!",
                             command=nachricht_anzeigen)
schließen_button = Button(fenster, text="Schließen", command=exit)

info.pack()
box_anzeigen_button.pack()
schließen_button.pack()

fenster.mainloop()
