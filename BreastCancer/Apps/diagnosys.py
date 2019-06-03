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

realValued =['radius','texture','perimeter','area','smoothness','compactness','concavity','concave points','symmetry','fractal dimension']


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

def UnusualValues(data,p):
	dat =  {
	        	"GlobalParameters": {
		}
			}

	body = str.encode(json.dumps(dat))

	OK=True

	try :
		file_Key = open("../SecuAccess/Api_key_stat.txt", "r")
		api_key = file_Key.read()
		file_url = open("../SecuAccess/Web_Service_stat.txt", "r")
		url = file_url.read()
	except FileNotFoundError :
		OK=False
		showerror('Security File not found', 'You probably don\'t have The Security File contact the responsable ')

	if OK :
		headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

		req = urllib.request.Request(url, body, headers) 

		try:
			response = urllib.request.urlopen(req)

		    # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
		    # req = urllib.request.Request(url, body, headers) 
		    # response = urllib.request.urlopen(req)

			result = response.read().decode('utf-8')
			rep = json.loads(result)
			unusual=""
			for i in range(0,10):
				mi = float(rep ['Results']['output1']['value']['Values'][i][0])
				ma = float(rep['Results']['output1']['value']['Values'][i][1])
				ecartType  =float(rep['Results']['output1']['value']['Values'][i][2])

				for j in range(1,3):
					if mi > float(rep['Results']['output1']['value']['Values'][i+(10*j)][0]):
						mi = float(rep['Results']['output1']['value']['Values'][i+(10*j)][0])
					if ma < float(rep['Results']['output1']['value']['Values'][i+(10*j)][1]) :
						ma = float(rep['Results']['output1']['value']['Values'][i+(10*j)][1])
					if ecartType < float(rep['Results']['output1']['value']['Values'][i+(10*j)][2]) :
						ecartType =float(rep['Results']['output1']['value']['Values'][i+(10*j)][2])
				
				for t in range(0,3):
					try :
						if (not(data[i][t].get()<(ma+ecartType) and data[i][t].get()>(mi-ecartType))):
							unusual =unusual+ '\n'+ realValued[i] + "No" + str(t+1) + ","
					except TclError :
						print("problemes de data")

		except urllib.error.HTTPError as error:
		    unusual="error while reading"

		if(len(unusual)>0):
			p.append("UnusualValues at :\n"+ unusual)
	return OK


fenetre = Tk()
fenetre.title("Diagnosys")

menubar = Menu(fenetre)
ExampleMenu = Menu(menubar, tearoff=0)
menubar.add_command(label="Leave", command=fenetre.quit)


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

		unusual = []

		TestSEcuFile=UnusualValues(values2,unusual)
		
		OK=False

		if(len(unusual)==0):
			OK = True
		elif askyesno('Unusual Values detected', 'Are you sure the data are correctly typed?\n'+unusual[0]):
			OK = True
		else :
			Ok = False

		try :
			file_Key = open("../SecuAccess/Api_key.txt", "r")
			api_key = file_Key.read()
			file_url = open("../SecuAccess/Web_Service.txt", "r")
			url = file_url.read()
		except FileNotFoundError :
			OK=False
			if(TestSEcuFile):
				showerror('Security File not found', 'You probably don\'t have The Security File contact the responsable ')

		if(OK):
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

def ExMalignant() :
	valuesField.set('17.99,10.38,122.8,1001,0.1184,0.2776,0.3001,0.1471,0.2419,0.07871,1.095,0.9053,8.589,153.4,0.006399,0.04904,0.05373,0.01587,0.03003,0.006193,25.38,17.33,184.6,2019,0.1622,0.6656,0.7119,0.2654,0.4601,0.1189')
	field()

def ExBegnin() :
	valuesField.set('13.54,14.36,87.46,566.3,0.09779,0.08129,0.06664,0.04781,0.1885,0.05766,0.2699,0.7886,2.058,23.56,0.008462,0.0146,0.02387,0.01315,0.0198,0.0023,15.11,19.26,99.7,711.2,0.144,0.1773,0.239,0.1288,0.2977,0.07259')
	field()

def Help():
	showinfo('Help','######################\nThe App for the diagnosys of Brest Cancer is lunch\npython version : 3\n######################\n\nfew things to know :\n- To run the App successfully you will need the Security file <SecuAccess> \nstore in BreastCancer file.\n\n- On the main page there are some text field, the easiest way to field them,\nis to field the text field that take a list of values and automaticly field \nall the other ones.\n\n- there is a sample of values in the file <wdbc.data> the explications of this\nsample is in the file <wdbc.names>.' )



ExampleMenu.add_command(label="EX.Malignant", command=ExMalignant)
ExampleMenu.add_command(label="EX.Begnin", command=ExBegnin)
menubar.add_command(label="Help", command=Help)
menubar.add_cascade(label="Examples", menu=ExampleMenu)

fenetre.config(menu=menubar)

bouton=Button(FrameField, text="Field",background='ivory',command=field)
bouton.grid(row=2, column=3, pady=5, padx=5)
bouton=Button(FrameField, text="clear",background='ivory',command=clear)
bouton.grid(row=2, column=4, pady=5, padx=5)
bouton=Button(FrameField, text="Valider",background='green',command=calcul)
bouton.grid(row=3, column=4, pady=5, padx=5)



fenetre.mainloop()