import urllib2
# If you are using Python 3+, import urllib instead of urllib2

import json

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

# Getting season
seasonParsed = -2
while(seasonParsed == -2):
    season = input("Please enter the actual season \n1:winter\n2:spring\n3:summer\n4:fall\n")
    seasonParsed = parseSeason(season)

print("--------------------------------------------------------------")

# Getting age then converting it to be in [0,1]
age = 0
while(age < 18 or age >36):
    age = input("Please enter your age (must be between 18 and 36) : ")
age = (age-18)/18.

print("--------------------------------------------------------------")
# Getting informations about childish diseases

childishDiseases = -1
while(childishDiseases != 0 and childishDiseases != 1):
    childishDiseases = input("Did you had childish diseases (for instance chicken pox, measles, mumps, polio ..)?\n0:yes\n1:no\n")

print("--------------------------------------------------------------")

# Getting informations about accident or serious trauma
trauma = -1
while(trauma != 0 and trauma != 1):
    trauma = input("Did you had any accident or serious trauma ?\n0:yes\n1:no\n")

print("--------------------------------------------------------------")

# Getting informations about surgical intervention
surgical = -1
while(surgical != 0 and surgical != 1):
    surgical = input("Did you had any surgical intervention ?\n0:yes\n1:no\n")

print("--------------------------------------------------------------")

#Getting informations about potential high fever in the past year
fever = -2
while(fever != -1 and fever != 0 and fever != 1):
    fever = input("Did you had high fever during last year?\n-1:less than three months ago\n 0:more than 3 months ago\n 1:no\n")

print("--------------------------------------------------------------")

#Getting informations about frequency of alcool consumption
alcohol = -1
while(alcohol == -1):
    alcoholInfo = input("What's your alcohol consumption frequency ?\n1:several times a day\n2:every day\n3:several times a week\n4:once a week\n5:hardly ever or never\n")
    alcohol = parseAlcoholConsumption(alcoholInfo)

print("--------------------------------------------------------------")

#Getting informations about smoking habit
smoking = -2
while(smoking != -1 and smoking != 0 and smoking != 1):
    smoking = input("Are you smoking?\n-1:never\n 0:occasionnally\n 1:daily\n")

print("--------------------------------------------------------------")

#Getting informations about time spent sit in a day
hoursSit = -1
while(hoursSit < 0 or hoursSit > 24):
    hoursSit = input("How much do you spend sit per day?\n")
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

url = 'https://ussouthcentral.services.azureml.net/workspaces/958400274ab54dac8d87114c07515abb/services/fa83783ce736417f94d3864ecf63b461/execute?api-version=2.0&details=true'
api_key = 'noMUJzdsos/oKEH5XyMGVRESg9Z6V/lirKtaz6oE5O1t79NirCLVi4jUuuoK3FJxRVvY43Ii+cMMlulb0DkpPw=='
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib2.Request(url, body, headers)

try:
    response = urllib2.urlopen(req)
    # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
    # req = urllib.request.Request(url, body, headers)
    # response = urllib.request.urlopen(req)

    result = response.read()
    # Uncomment the line bellow to see the full json of the answer
    # print(result)
    resultParsed = json.loads(result)
    if(resultParsed["Results"]["output1"]["value"]["Values"][0][0] == 'N'):
        print("It's the good time to have a baby !")
    else:
        print("Your fertility seems altered.")
except urllib2.HTTPError, error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())

    print(json.loads(error.read()))
