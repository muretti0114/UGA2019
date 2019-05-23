# %%
from tkinter import * 
# If you are using Python 3+, import tkinter instead of Tkinter
import urllib
import urllib.request
# If you are using Python 3+, import urllib instead of urllib2

import json
#from tkMessageBox import *
#If you are using Python 3+
from tkinter.messagebox import *



fenetre = Tk()
fenetre.title("Diagnosys")

label = Label(fenetre, text="Enter the values (val1,...,VAl30):")
label.grid(row=0, columnspan=2, pady=8)

compteur = 1

values = StringVar()

label = Label(fenetre, text="Values : ")
label.grid(row=1, column=1, pady=5, padx=5)
values.set("  M ,  G ,  Best ,  Best ,  Best ,  Y ,  Married ,  T ,  Free ,  Vh ,  Large ,  Il ,  Il ,  Service ,  Service ,  Large ,  Good ,  Govt ,  Eng ,  Large ,  Good  ")
entree=Entry(fenetre,textvariable=values, width=10)
entree.grid(row=1, column=2, pady=5, padx=5)
def calcul():
    val=values.get().split(',')

data =  {

        "Inputs": {

                "input1":
                {
                    "ColumnNames": ["ge", "cst", "tnp", "twp", "iap", "arr", "ls", "as", "fmi", "fs", "fq", "mq", "fo", "nf", "sh", "ss", "me", "tt", "atd"],
                    "Values": [ [ "M", "G", "Best", "Best", "Best", "Y", "T", "Free", "Vh", "Large", "Il", "Il", "Service", "Large", "Good", "Govt", "Eng", "Large", "Good" ], [ "M", "G", "Best", "Best", "Best", "Y", "T", "Free", "Vh", "Large", "Il", "Il", "Service", "Large", "Good", "Govt", "Eng", "Large", "Good" ], ]
                },        },
            "GlobalParameters": {
}
    }

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/87d2ece9e93242a7a220085604a6c314/services/17d7543088f649c1b141ff92e2a3e8db/execute?api-version=2.0&details=true'
api_key = 'hrdhObKQj2d5WJk6LCiqTL3oFfoQymQR/BkXsd//lsEuVj6OnpEI9+3z/zP5dUNuWdXY8sNYXYJU4Bw4VZYwWw=='
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers) 
try:
    response = urllib.request.urlopen(req)

    # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
    # req = urllib.request.Request(url, body, headers) 
    # response = urllib.request.urlopen(req)

    result = response.read()
    print(result) 
except urllib.HTTPError:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())

    print(json.loads(error.read()))                 
Tk.destroy

bouton=Button(fenetre, text="Valider",command=calcul)
bouton.grid(row=11, column=4, pady=5, padx=5)
bouton=Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.grid(row=11, column=1, pady=5, padx=5)


fenetre.mainloop()

# %%
