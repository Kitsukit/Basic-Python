from tkinter import *

fenster = Tk()
fenster.title("Hallo!")

info = Label(fenster, text="Kannst mich gleich wieder schließen!")
warten = Label(fenster, text="Warte doch noch ein wenig..")

schließen_button = Button(fenster, text="Schließen", command=exit)

info.pack()
schließen_button.pack()
warten.pack()

fenster.mainloop()
