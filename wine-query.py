import urllib.request
import json

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
                [
                    "8.0",
                    "0.26",
                    "0.4",
                    "7",
                    "0.033",
                    "41",
                    "99",
                    "0.9912",
                    "3.17",
                    "0.4",
                    "10.8",
                    "0"
                ],
                [
                    "6.9",
                    "0.2",
                    "0.31",
                    "1.2",
                    "0.068",
                    "21",
                    "160",
                    "0.991",
                    "3.3",
                    "0.5",
                    "8.9",
                    "0"
                ]
            ]
        },
    },
    "GlobalParameters": {}
}

price = {1: 15, 2: 11}

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

def main():
    quality = {}
    get_query_results(data, quality)
    best_wine = get_best_quality(quality)
    print("Best wine (quality): " + str(best_wine[0]) + " ; quality = " + str(best_wine[1]))
    best_wine = get_best_wine(quality, price)
    print("Best wine (overall): " + str(best_wine[0]) + " ; ratio = " + str(best_wine[1]))

main()