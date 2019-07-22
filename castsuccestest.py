# %%
from tkinter import * 
# If you are using Python 3+, import tkinter instead of Tkinter
import urllib
import urllib.request
# import urllib.request
# If you are using Python 3+, import urllib instead of urllib2

import json
#from tkMessageBox import *
#If you are using Python 3+
from tkinter import messagebox
from tkinter.messagebox import *




fenetre = Tk()
fenetre.title("Will the student finish correctly his semester ?!")

label = Label(fenetre, text="Please enter your values : ")
label.grid(row=0, column=0, pady=5, padx=5)

label = Label(fenetre, text="Gender : ")
label.grid(row=0, column=1, pady=5, padx=5)
liste = Listbox(fenetre,selectmode='extended')
liste.insert(1, "M")
liste.insert(2, "F")
liste.grid(row=1,column=1, pady=5, padx=5)

label = Label(fenetre, text="Cast : ")
label.grid(row=0, column=2 , pady=5, padx=5)
liste1 = Listbox(fenetre,exportselection='0')
liste1.insert(3, "G")
liste1.insert(4, "ST")
liste1.insert(5, "SC")
liste1.insert(6, "OBC")
liste1.insert(7, "MOBC")
liste1.grid(row=1,column=2, pady=5, padx=5)

label = Label(fenetre, text="Class X Percentage : ")
label.grid(row=0, column=3 , pady=5, padx=5)
liste2 = Listbox(fenetre,exportselection='0')
liste2.insert(1, "Best")
liste2.insert(2, "Vg")
liste2.insert(3, "Good")
liste2.insert(4, "Pass")
liste2.insert(5, "Fail")
liste2.grid(row=1,column=3, pady=5, padx=5)

label = Label(fenetre, text="Class XII Percentage : ")
label.grid(row=0, column=4 , pady=5, padx=5)
liste3 = Listbox(fenetre,exportselection='0')
liste3.insert(1, "Best")
liste3.insert(2, "Vg")
liste3.insert(3, "Good")
liste3.insert(4, "Pass")
liste3.insert(5, "Fail")
liste3.grid(row=1,column=4, pady=5, padx=5)

label = Label(fenetre, text="Internal Assesment Percentage : ")
label.grid(row=2, column=0 , pady=5, padx=5)
liste4 = Listbox(fenetre,exportselection='0')
liste4.insert(1, "Best")
liste4.insert(2, "Vg")
liste4.insert(3, "Good")
liste4.insert(4, "Pass")
liste4.insert(5, "Fail")
liste4.grid(row=3,column=0, pady=5, padx=5)


label = Label(fenetre, text="Have legal papers : ")
label.grid(row=2, column=1, pady=5, padx=5)
liste5 = Listbox(fenetre,exportselection='0')
liste5.insert(1, "Y")
liste5.insert(2, "N")
liste5.grid(row=3,column=1, pady=5, padx=5)

label = Label(fenetre, text="Lived in town or village ")
label.grid(row=2, column=2, pady=5, padx=5)
liste6 = Listbox(fenetre,exportselection='0')
liste6.insert(1, "T")
liste6.insert(2, "V")
liste6.grid(row=3,column=2, pady=5, padx=5)

label = Label(fenetre, text="Admission category")
label.grid(row=2, column=3, pady=5, padx=5)
liste7 = Listbox(fenetre,exportselection='0')
liste7.insert(1, "Free")
liste7.insert(2, "Paid")
liste7.grid(row=3,column=3, pady=5, padx=5)

label = Label(fenetre, text="Family monthy income in INR")
label.grid(row=2, column=4 , pady=5, padx=5)
liste8 = Listbox(fenetre,exportselection='0')
liste8.insert(1, "Vh")
liste8.insert(2, "High")
liste8.insert(3, "Am")
liste8.insert(4, "Medium")
liste8.insert(5, "Low")
liste8.grid(row=3,column=4, pady=5, padx=5)

label = Label(fenetre, text="Family Size")
label.grid(row=5, column=0, pady=5, padx=5)
liste9 = Listbox(fenetre,exportselection='0')
liste9.insert(1, "Large")
liste9.insert(2, "Average")
liste9.insert(3, "Small")
liste9.grid(row=6,column=0, pady=5, padx=5)

label = Label(fenetre, text="Father Qualification")
label.grid(row=5, column=1, pady=5, padx=5)
liste10 = Listbox(fenetre,exportselection='0')
liste10.insert(1, "Il")
liste10.insert(2, "Um")
liste10.insert(3, "10")
liste10.insert(4, "12")
liste10.insert(5, "Degree")
liste10.insert(6, "Pg")
liste10.grid(row=6,column=1, pady=5, padx=5)

label = Label(fenetre, text="Mother Qualification")
label.grid(row=5, column=2, pady=5, padx=5)
liste11 = Listbox(fenetre,exportselection='0')
liste11.insert(1, "Il")
liste11.insert(2, "Um")
liste11.insert(3, "10")
liste11.insert(4, "12")
liste11.insert(5, "Degree")
liste11.insert(6, "PG")
liste11.grid(row=6,column=2, pady=5, padx=5)

label = Label(fenetre, text="Father Occupation")
label.grid(row=5, column=3, pady=5, padx=5)
liste12 = Listbox(fenetre,exportselection='0')
liste12.insert(1, "Service")
liste12.insert(2, "Business")
liste12.insert(3, "Retired")
liste12.insert(4, "Farmer")
liste12.insert(5, "Others")
liste12.grid(row=6,column=3, pady=5, padx=5)

label = Label(fenetre, text="Number of friends")
label.grid(row=5, column=4, pady=5, padx=5)
liste13 = Listbox(fenetre,exportselection='0')
liste13.insert(1, "Large")
liste13.insert(2, "Average")
liste13.insert(3, "Small")
liste13.grid(row=6,column=4, pady=5, padx=5)

label = Label(fenetre, text="Number of friends")
label.grid(row=7, column=0, pady=5, padx=5)
liste14 = Listbox(fenetre,exportselection='0')
liste14.insert(1, "Good")
liste14.insert(2, "Average")
liste14.insert(3, "Poor")
liste14.grid(row=8,column=0, pady=5, padx=5)

label = Label(fenetre, text="Study Hours")
label.grid(row=7, column=1, pady=5, padx=5)
liste14b = Listbox(fenetre,exportselection='0')
liste14b.insert(1, "Govt")
liste14b.insert(2, "Private")
liste14b.grid(row=8,column=1, pady=5, padx=5)

label = Label(fenetre, text="Medium")
label.grid(row=7, column=2, pady=5, padx=5)
liste15 = Listbox(fenetre,exportselection='0')
liste15.insert(1, "Eng")
liste15.insert(2, "Asm")
liste15.insert(3, "Hin")
liste15.insert(3, "Ben")
liste15.grid(row=8,column=2, pady=5, padx=5)

label = Label(fenetre, text="Travel time to College")
label.grid(row=7, column=3, pady=5, padx=5)
liste16 = Listbox(fenetre,exportselection='0')
liste16.insert(1, "Large")
liste16.insert(2, "Average")
liste16.insert(3, "Small")
liste16.grid(row=8,column=3, pady=5, padx=5)

label = Label(fenetre, text="Number of friends")
label.grid(row=7, column=4, pady=5, padx=5)
liste17 = Listbox(fenetre,exportselection='0')
liste17.insert(1, "Good")
liste17.insert(2, "Average")
liste17.insert(3, "Poor")
liste17.grid(row=8,column=4, pady=5, padx=5)


arrayliste = [liste,liste1,liste2,liste3,liste4,liste5,liste6,liste7,liste8,liste9,liste10,liste11,liste12,liste13,liste14,liste14b,liste15,liste16,liste17]

values= []



##TODO BUTTON SEND HERE


def action():
    for i in arrayliste:    
        tuple = i.curselection()
        values.append(i.get(tuple[0]))
    data =  {

            "Inputs": {

                    "input1":
                    {
                        "ColumnNames": ["ge", "cst", "tnp", "twp", "iap", "arr", "ls", "as", "fmi", "fs", "fq", "mq", "fo", "nf", "sh", "ss", "me", "tt", "atd"],
                        "Values": [ values, ]
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
        resultDecode = json.loads(result)
        res = resultDecode["Results"]["output1"]["value"]["Values"][0][5]
        messagebox.showinfo("Response : ", "The student performance looks like to be " + res)
    except urllib.HTTPError:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())

        print(json.loads(error.read()))                 
    Tk.destroy

bouton=Button(fenetre, text="Valider",command=action)
bouton.grid(row=11, column=1, pady=5, padx=5)
bouton=Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.grid(row=11, column=2, pady=5, padx=5)


fenetre.mainloop()

# %%
