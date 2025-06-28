import requests

key = "fef210d136fc4aff06262618ac321c92"
url= "http://data.fixer.io/api/latest"

def exchange(*target):
    params = {
        "access_key": key,
        "symbols": ",".join(target)
    }

    response = requests.get(url, params = params)

    if response.status_code == 200:
        data = response.json()
        print(data)
        for c in data["rates"]:
            print(data["base"], "to", c, "=", data["rates"][c])
        
    else:
        print(response.status_code)

exchange("USD", "JPY", "AUD", "CZK", "PLN")