# import urllib2
import urllib
import urllib.request
import urllib.error
# If you are using Python 3+, import urllib instead of urllib2

import json

# checking internet connection
def isConnected():
    try :
        stri = "https://www.google.co.in"
        data = urllib.request.urlopen(stri)
        return True
    except urllib.request.URLError:
        return False

# Season conversion
def parseSeason(seasonNb):
    switcher = {
        1: -1,
        2: -0.33,
        3: 0.33,
        4: 1,
    }
    return switcher.get(seasonNb, -2)

# Alcohol consumption conversion
def parseAlcoholConsumption(alcohol):
    switcher = {
        1: 0,
        2: 0.2,
        3: 0.6,
        4: 0.8,
        5: 1,
    }
    return switcher.get(alcohol, -1)

print("--------------------------------------------------------------")
print("This test is for men fertility between 18 and 36 years old.")
print("--------------------------------------------------------------")
fileMissing=False
try :
    with open('url.txt','r') as file:
        url = file.read().replace('\n','')
    with open('api_key.txt','r') as file:
        api_key = file.read().replace('\n','')
except FileNotFoundError:
    fileMissing = True

if(not fileMissing):
    # Getting season
    seasonParsed = -2
    while(seasonParsed == -2):
        season = input("Please enter the actual season \n1:winter\n2:spring\n3:summer\n4:fall\n")
        try:
            season = int(season)
        except ValueError:
            print("Wrong entry")
        seasonParsed = parseSeason(season)

    print("--------------------------------------------------------------")

    # Getting age then converting it to be in [0,1]
    age = 0
    while(age < 18 or age >36):
        entry = input("Please enter your age (must be between 18 and 36) : \n")
        try:
            age = int(entry)
        except ValueError:
            print("Wrong entry")
    age = (age-18)/18.

    print("--------------------------------------------------------------")

    # Getting informations about childish diseases
    childishDiseases = -1
    while(childishDiseases != 0 and childishDiseases != 1):
        entry = input("Did you had childish diseases (for instance chicken pox, measles, mumps, polio ..)?\n0:yes\n1:no\n")
        try:
            childishDiseases = int(entry)
        except ValueError:
            print("Wrong entry")

    print("--------------------------------------------------------------")

    # Getting informations about accident or serious trauma
    trauma = -1
    while(trauma != 0 and trauma != 1):
        entry = input("Did you had any accident or serious trauma ?\n0:yes\n1:no\n")
        try:
            trauma = int(entry)
        except ValueError:
            print("Wrong entry")

    print("--------------------------------------------------------------")

    # Getting informations about surgical intervention
    surgical = -1
    while(surgical != 0 and surgical != 1):
        entry = input("Did you had any surgical intervention ?\n0:yes\n1:no\n")
        try:
            surgical = int(entry)
        except ValueError:
            print("Wrong entry")

    print("--------------------------------------------------------------")

    #Getting informations about potential high fever in the past year
    fever = -2
    while(fever != -1 and fever != 0 and fever != 1):
        entry = input("Did you had high fever during last year?\n-1:less than three months ago\n 0:more than tree months ago\n 1:no\n")
        try:
            fever = int(entry)
        except ValueError:
            print("Wrong entry")

    print("--------------------------------------------------------------")

    #Getting informations about frequency of alcool consumption
    alcohol = -1
    while(alcohol == -1):
        alcoholInfo = input("What's your alcohol consumption frequency ?\n1:several times a day\n2:every day\n3:several times a week\n4:once a week\n5:hardly ever or never\n")
        try:
            alcoholInfo = int(alcoholInfo)
            alcohol = parseAlcoholConsumption(alcoholInfo)
        except ValueError:
            print("Wrong entry")

    print("--------------------------------------------------------------")

    #Getting informations about smoking habit
    smoking = -2
    while(smoking != -1 and smoking != 0 and smoking != 1):
        entry = input("Are you smoking?\n-1:never\n 0:occasionnally\n 1:daily\n")
        try:
            smoking = int(entry)
        except ValueError:
            print("Wrong entry")

    print("--------------------------------------------------------------")

    #Getting informations about time spent sit in a day
    hoursSit = -1
    while(hoursSit < 0 or hoursSit > 24):
        entry = input("How much time do you spend sit per day?\n")
        try:
            hoursSit = int(entry)
        except ValueError:
            print("Wrong entry")
    hoursSit = hoursSit/24.

    print("--------------------------------------------------------------")

    data =  {

            "Inputs": {

                    "input1":
                    {
                        "ColumnNames": ["Season", "Age", "Childish diseases", "Accident or serious trauma", "Surgical intervention", "High fevers in the last year", "Frequency of alcohol consumption", "Smoking habit", "Number of hours spent sitting per day"],
                        "Values": [ [ str(seasonParsed), str(age), str(childishDiseases), str(trauma), str(surgical), str(fever), str(alcohol), str(smoking), str(hoursSit) ], ]
                    },        },
                "GlobalParameters": {
    }
        }

    body = str.encode(json.dumps(data))
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    if(isConnected()):

        # req = urllib2.Request(url, body, headers)
        req = urllib.request.Request(url, body, headers)

        try:
            # response = urllib2.urlopen(req)
            response = urllib.request.urlopen(req)
            # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
            # req = urllib.request.Request(url, body, headers)
            # response = urllib.request.urlopen(req)

            result = response.read().decode('utf-8')
            # Uncomment the line bellow to see the full json of the answer
            # print(result)
            resultParsed = json.loads(result)
            if(resultParsed["Results"]["output1"]["value"]["Values"][0][0] == 'N'):
                print("It's the good time to have a baby !")
            else:
                print("Your fertility seems altered.")
                print("The best season for fertility is winter")
                if(childishDiseases == 0 or surgical == 0 or trauma == 0):
                    print("You should go for a check")
                if(fever == -1 or fever == 0):
                    print("You should wait for few month")
                if(smoking >= 0 or alcohol <= 3):
                    print("Maybe you should try to change your habbits (less drinking or smoking for example)")

            response2 = urllib.request.urlopen(req)
            result2 = response2.read().decode('utf-8')
            if(result != result2):
                print("Your result seems to be altered, don't take it as true")

        except urllib.error.HTTPError as error:
            print("The request failed with status code: " + str(error.code))

            # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
            print(error.info())

            print(json.loads(error.read().decode('utf-8')))
    else:
        print("No internet connection, try again with internet connected")
else:
    print("You miss api or url file. Please contact dev to get them")
