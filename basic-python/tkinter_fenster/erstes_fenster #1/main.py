from tkinter import *

fenster = Tk()
fenster.title("Hallo!")

info = Label(fenster, text="Kannst mich gleich wieder schließen!")

schließen_button = Button(fenster, text="Schließen", command=exit)

info.pack()
schließen_button.pack()

fenster.mainloop()
