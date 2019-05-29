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

label = Label(fenetre, text="Enter the values (val1,...,VAl30):")
label.grid(row=0, columnspan=2, pady=8)

compteur = 1

values = StringVar()

label = Label(fenetre, text="Values : ")
label.grid(row=1, column=1, pady=5, padx=5)
values.set("0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
entree=Entry(fenetre,textvariable=values, width=10)
entree.grid(row=1, column=2, pady=5, padx=5)
def calcul():
    val=values.get().split(',')

    data =  {

        "Inputs": {

                "lol":
                {
                    "ColumnNames": ["real-valued(1)", "real-valued(2)", "real-valued(3)", "real-valued(4)", "real-valued(5)", "real-valued(6)", "real-valued(7)", "real-valued(8)", "real-valued(9)", "real-valued(10)", "real-valued(11)", "real-valued(12)", "real-valued(13)", "real-valued(14)", "real-valued(15)", "real-valued(16)", "real-valued(17)", "real-valued(18)", "real-valued(19)", "real-valued(20)", "real-valued(21)", "real-valued(22)", "real-valued(23)", "real-valued(24)", "real-valued(25)", "real-valued(26)", "real-valued(27)", "real-valued(28)", "real-valued(29)", "real-valued(30)"],
                    "Values": [val,]
                },        },
            "GlobalParameters": {
    }
        }

    body = str.encode(json.dumps(data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/b0469c7e953f4bc992e2134488dec084/services/a218f94199bb496d9fc01b7307c3ce8c/execute?api-version=2.0&details=true'
    api_key = 'qW8bgwscpGsUz6nNLUYp95Ot1Kk5sx6m2byWd9Ja8SRw5e30ubrRpPNJeM8xftry6fWXvXVBexC9NEt+I/nhiQ=='
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib.request.Request(url, body, headers) 

    try:
        response = urllib.request.urlopen(req)

        # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
        # req = urllib.request.Request(url, body, headers) 
        # response = urllib.request.urlopen(req)

        result = response.read()
        #1 malign else begnin
        diagnosys = result[147]
        
        proba = result[151:(len(result)-7)]

        if(diagnosys=="0"):
            showinfo('Result', 'The result says that it\'s Benign\n')
        else :
            showinfo('Result', 'The result says that it\'s Malignant\n')

    except urllib.error.HTTPError as error:
        # print("The request failed with status code: " + str(error.code))
        showerror('The request failed with status code:' + str(error.code), json.loads(error.read()))
        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        # print(error.info())

        # print(json.loads(error.read()))
    Tk.destroy

bouton=Button(fenetre, text="Valider",command=calcul)
bouton.grid(row=11, column=4, pady=5, padx=5)
bouton=Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.grid(row=11, column=1, pady=5, padx=5)


fenetre.mainloop()