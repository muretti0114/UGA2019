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


def isConnected():
    try :
        stri = "https://www.google.co.in"
        data = urllib.request.urlopen(stri)
        return True
    except urllib.request.URLError:
        return False

def allValuesPositiv(data):
	for i in range(0,3):
			for j in range(0,10):
				try :
					if(data[j][i].get()<0.):
						return False
				except TclError :
					x=1
	return True

def allValuesDouble(data):
	for i in range(0,3):
			for j in range(0,10):
				try :
					data[j][i].get()
				except TclError :
					return False
	return True

realValued =['radius','texture','perimeter','area','smoothness','compactness','concavity','concave points','symmetry','fractal dimension']
fenetre = Tk()
fenetre.title("Diagnosys")

FrameCells = Frame(fenetre, borderwidth=2, relief=GROOVE)
FrameCells.grid(row=1, column=1, pady=5, padx=5)

FrameField = Frame(fenetre, borderwidth=2, relief=GROOVE)
FrameField.grid(row=2, column=1, pady=5, padx=5)


label = Label(FrameCells, text="Enter the values:")
label.grid(row=0, columnspan=2, pady=8)

compteur = 1

values = []
values2 = []

for i in range(0,10):
	values.append([])
	values2.append([])
	for j in range(0,6):
		if j%2==0 :
			label = Label(FrameCells, text=realValued[i])
			label.grid(row=i+1, column=j, pady=5, padx=5)
			compteur+=1
		else :
			values2[i].append(DoubleVar())
			values2[i][len(values2[i])-1].set(0.)
			values[i].append(Entry(FrameCells,textvariable=values2[i][len(values2[i])-1], width=10))
			values[i][len(values2[i])-1].grid(row=i+1, column=j, pady=5, padx=5)

def calcul():

	def runningTest():
		p =[]
		if(not(isConnected())):
			p.append('-Web Connection')

		if(not(allValuesPositiv(values2))):
			p.append('-Negatives Values')

		if(not(allValuesDouble(values2))):
			p.append('-Unespected Values (Only Double)')
		return p

	errors = runningTest()
	if(len(errors) == 0):
		val=[]

		for i in range(0,3):
			for j in range(0,10):
				val.append(values2[j][i].get())

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

		file_Key = open("../SecuAccess/Api_key.txt", "r")
		file_url = open("../SecuAccess/Web_Service.txt", "r")

		url = file_url.read()
		api_key = file_Key.read()
		headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

		req = urllib.request.Request(url, body, headers) 

		try:
		    response = urllib.request.urlopen(req)

		    # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
		    # req = urllib.request.Request(url, body, headers) 
		    # response = urllib.request.urlopen(req)

		    result = response.read().decode('utf-8')
		    rep = json.loads(result)
		    #1 malign else begnin

		    if(rep['Results']['output1']['value']['Values'][0][0]=="0"):
		    	showinfo('Result', 'The result says that it\'s Benign\n')
		    else :
		    	showinfo('Result', 'The result says that it\'s Malignant\n')

		except urllib.error.HTTPError as error:
			showerror('The request failed with status code:' + str(error.code), json.loads(error.read()))
		    # print("The request failed with status code: " + str(error.code))

		    # # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
		    # print(error.info())

		    # print(json.loads(error.read()))
	else:
		prob = ""
		for i in range(0, len(errors)):
			prob=prob+'\n'+errors[i]
		showerror('error','Problems detected :\n'+prob)

	Tk.destroy
valuesField = StringVar()
label = Label(FrameField, text="field values from a list (val1 ,..., Val30) : ")
label.grid(row=1, column=1, pady=5, padx=5)
valuesField.set("0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
entree=Entry(FrameField,textvariable=valuesField, width=60)
entree.grid(row=2, column=1, pady=5, padx=5)

def field() :
	f = valuesField.get()
	fieldingValues = f.split(",")
	i=0
	j=0
	for w in range(0,len(fieldingValues)):
		if w<30 :
			values2[j][i].set(fieldingValues[w])
			if j==9 :
				i=(i+1)%3
			j=(j+1)%10

def clear() :
	f = valuesField.get()
	fieldingValues = f.split(",")
	valuesField.set('')
	i=0
	j=0
	for w in range(0,len(fieldingValues)):
		if w<30 :
			values2[j][i].set('0.0')
			if j==9 :
				i=(i+1)%3
			j=(j+1)%10


bouton=Button(FrameField, text="Field",background='ivory',command=field)
bouton.grid(row=2, column=3, pady=5, padx=5)
bouton=Button(FrameField, text="clear",background='ivory',command=clear)
bouton.grid(row=2, column=4, pady=5, padx=5)
bouton=Button(FrameField, text="Valider",background='green',command=calcul)
bouton.grid(row=3, column=4, pady=5, padx=5)
bouton=Button(FrameField, text="Fermer", background='red',command=fenetre.quit)
bouton.grid(row=3, column=1, pady=5, padx=5)



fenetre.mainloop()