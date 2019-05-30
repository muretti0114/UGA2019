import urllib.request
import json

from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

data = {
    "Inputs": {
        "input1": {
            "ColumnNames": [
                "fixed acidity",
                "volatile acidity",
                "citric acid",
                "residual sugar",
                "chlorides",
                "free sulfur dioxide",
                "total sulfur dioxide",
                "density",
                "pH",
                "sulphates",
                "alcohol",
                "quality"
            ],
            "Values": [
            ]
        },
    },
    "GlobalParameters": {}
}

# dataset data
metadata = {}
fiability = 10/100  # coefficient of fiability of input data compared to dataset data

# result variables
prices = {}
qualities = {}


def get_dataset_summary(data_summary):
    # web API
    placeholder_data = {
        "GlobalParameters": {
        }
    }
    body = str.encode(json.dumps(placeholder_data))
    url = 'https://ussouthcentral.services.azureml.net/workspaces/82c5bb7ddffd42caa5864158ef8523f8/services/4fd0abcedae8409f9676cf60e6a7f5ba/execute?api-version=2.0&details=true'
    api_key = 'Xpn8o+++l3odBNtuVG+xBNUNoS9LSsRC0eZmQejdtgIby0tW32xX62WlLJnWu0bW45cxvujpQyOV5fYc1iEzMw=='
    headers = {'Content-Type': 'application/json',
               'Authorization': ('Bearer ' + api_key)}
    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)
        result = json.loads(response.read())
        result = result['Results']['output1']['value']['Values']
        for v in result:
            metadata[v[0]] = [float(v[1]), float(v[2])]
    except urllib.request.HTTPError as error:
        print("The request failed with status code: " + str(error.code))
        print(error.info())
        print(json.loads(error.read()))


def get_query_results(request_data, result_storage):
    # web API
    body = str.encode(json.dumps(request_data))
    url = 'https://ussouthcentral.services.azureml.net/workspaces/82c5bb7ddffd42caa5864158ef8523f8/services/ee897c9726c14d8b8eea41ea2f6778ee/execute?api-version=2.0&details=true'
    api_key = 'uIemc6Mt+ED0qSubag0ABB197ri0q9K/VkrymacG6gsQBH/zUIhb7gTxUheRzqfI3kb7JFx5BdVtPYPXZP9InA=='
    headers = {'Content-Type': 'application/json',
               'Authorization': ('Bearer ' + api_key)}

    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)
        result = json.loads(response.read())
        i = 1
        for wine in result['Results']['output1']['value']['Values']:
            result_storage[int(i)] = float(wine[-1])
            i = i + 1
    except urllib.request.HTTPError as error:
        print("The request failed with status code: " + str(error.code))
        print(error.info())
        print(json.loads(error.read()))


def get_best_quality(result_storage):
    best = ('output0', 0)
    for wine in result_storage:
        if (result_storage[wine] > best[1]):
            best = (wine, result_storage[wine])
    return best


def get_best_wine(result_storage, price_table):
    best = ('output0', 0)
    for wine in result_storage:
        if (result_storage[wine] / price_table[wine] > best[1]):
            best = (wine, result_storage[wine] / price_table[wine])
    return best


def add_wine(dataset, price_table, feature_list):
    new_wine = []
    for v in feature_list:
        if v != "price":
            if feature_list[v].get() < 0.0:
                print("Error: " + v + " < 0")
                return
            else:
                if feature_list[v].get() < metadata[v][0] or feature_list[v].get() > metadata[v][1]:
                    print("Error: " + v + " out of range. Allowed interval: [" + str(
                        metadata[v][0]) + ", " + str(metadata[v][1]) + "]")
                    return
                else:
                    new_wine.append(str(feature_list[v].get()))
    new_wine.append(0)  # quality placeholder
    dataset["Inputs"]["input1"]["Values"].append(new_wine)
    price_table[len(price_table) + 1] = feature_list["price"].get()


def reset_data(dataset, result_storage, price_table):
    dataset["Inputs"]["input1"]["Values"] = []
    result_storage.clear()
    price_table.clear()
    print("Wine data successfully reset")


def main():
    get_query_results(data, qualities)
    best_wine = get_best_quality(qualities)
    print("Best wine (quality): " +
          str(best_wine[0]) + " ; quality = " + str(best_wine[1]))
    best_wine = get_best_wine(qualities, prices)
    print("Best wine (overall): " +
          str(best_wine[0]) + " ; ratio = " + str(best_wine[1]))
    return


#Computing dataset statistics
get_dataset_summary(metadata)

#UI
root = Tk()
root.title("White wine quality prediction")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

fixed_acidity = DoubleVar()
volatile_acidity = DoubleVar()
citric_acid = DoubleVar()
residual_sugar = DoubleVar()
chlorides = DoubleVar()
free_sulfur_dioxide = DoubleVar()
total_sulfur_dioxide = DoubleVar()
density = DoubleVar()
pH = DoubleVar()
sulphates = DoubleVar()
alcohol = DoubleVar()
price = DoubleVar()
quality = DoubleVar()

var_list = {"fixed acidity": fixed_acidity, "volatile acidity": volatile_acidity, "citric acid": citric_acid, "residual sugar": residual_sugar, "chlorides": chlorides,
            "free sulfur dioxide": free_sulfur_dioxide, "total sulfur dioxide": total_sulfur_dioxide, "density": density, "pH": pH, "sulphates": sulphates, "alcohol": alcohol, "price": price}

ttk.Label(mainframe, text="Fixed acidity").grid(column=1, row=1, sticky=E)
fixed_acidity_entry = ttk.Entry(
    mainframe, width=10, textvariable=fixed_acidity)
fixed_acidity_entry.grid(column=2, row=1, padx=5, pady=5, sticky=(W, E))

ttk.Label(mainframe, text="Volatile Acidity").grid(column=1, row=2, sticky=E)
volatile_acidity_entry = ttk.Entry(
    mainframe, width=10, textvariable=volatile_acidity)
volatile_acidity_entry.grid(column=2, row=2, padx=5, pady=5, sticky=(W, E))

ttk.Label(mainframe, text="Citric Acid").grid(column=1, row=3, sticky=E)
citric_acid_entry = ttk.Entry(mainframe, width=10, textvariable=citric_acid)
citric_acid_entry.grid(column=2, row=3, padx=5, pady=5, sticky=(W, E))

ttk.Label(mainframe, text="Residual Sugar").grid(column=1, row=4, sticky=E)
residual_sugar_entry = ttk.Entry(
    mainframe, width=10, textvariable=residual_sugar)
residual_sugar_entry.grid(column=2, row=4, padx=5, pady=5, sticky=(E))

ttk.Label(mainframe, text="Chlorides").grid(column=1, row=5, sticky=E)
chlorids_entry = ttk.Entry(mainframe, width=10, textvariable=chlorides)
chlorids_entry.grid(column=2, row=5, padx=5, pady=5, sticky=(E))

ttk.Label(mainframe, text="Free Sulfur Dioxide").grid(
    column=1, row=6, sticky=E)
free_sulfur_dioxide_entry = ttk.Entry(
    mainframe, width=10, textvariable=free_sulfur_dioxide)
free_sulfur_dioxide_entry.grid(column=2, row=6, padx=5, pady=5, sticky=(E))

ttk.Label(mainframe, text="Total Sulfur Dioxide").grid(
    column=1, row=7, sticky=E)
total_sulfur_dioxide_entry = ttk.Entry(
    mainframe, width=10, textvariable=total_sulfur_dioxide)
total_sulfur_dioxide_entry.grid(column=2, row=7, padx=5, pady=5, sticky=(E))

ttk.Label(mainframe, text="Density").grid(column=1, row=8, sticky=E)
density_entry = ttk.Entry(mainframe, width=10, textvariable=density)
density_entry.grid(column=2, row=8, padx=5, pady=5, sticky=(E))

ttk.Label(mainframe, text="pH").grid(column=1, row=9, sticky=E)
pH_entry = ttk.Entry(mainframe, width=10, textvariable=pH)
pH_entry.grid(column=2, row=9, padx=5, pady=5, sticky=(E))

ttk.Label(mainframe, text="Sulphates").grid(column=1, row=10, sticky=E)
sulphates_entry = ttk.Entry(mainframe, width=10, textvariable=sulphates)
sulphates_entry.grid(column=2, row=10, padx=5, pady=5, sticky=(E))

ttk.Label(mainframe, text="Alcohol").grid(column=1, row=11, sticky=E)
alcohol_entry = ttk.Entry(mainframe, width=10, textvariable=alcohol)
alcohol_entry.grid(column=2, row=11, padx=5, pady=5, sticky=(E))

ttk.Label(mainframe, text="Price").grid(column=1, row=12, sticky=E)
price_entry = ttk.Entry(mainframe, width=10, textvariable=price)
price_entry.grid(column=2, row=12, padx=5, pady=5, sticky=(E))

ttk.Button(mainframe, text="Add", command=lambda: add_wine(
    data, prices, var_list)).grid(column=1, row=13, sticky=(W))
ttk.Button(mainframe, text="Reset", command=lambda: reset_data(
    data, qualities, prices)).grid(column=2, row=13, sticky=(W))
ttk.Button(mainframe, text="Run experiment", command=main).grid(
    column=1, row=14, columnspan=2, sticky=(W, E))

root.mainloop()
