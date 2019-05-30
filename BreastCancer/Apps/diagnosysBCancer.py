from tkinter import * 
# If you are using Python 3+, import tkinter instead of Tkinter
import urllib
import urllib.request
import urllib.error
# If you are using Python 3+, import urllib instead of urllib2

import json
# from tkMessageBox import *
#If you are using Python 3+
from tkinter.messagebox import *



fenetre = Tk()
fenetre.title("Diagnosys")


def alert():
    showinfo("alerte", "Bravo!")

menubar = Menu(fenetre)

menubar.add_command(label="EX.Malignant", command=alert)
menubar.add_command(label="EX.Begnin", command=alert)
menubar.add_command(label="Leave", command=fenetre.quit)

fenetre.config(menu=menubar)

bouton=Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.grid(row=11, column=1, pady=5, padx=5)


fenetre.mainloop()