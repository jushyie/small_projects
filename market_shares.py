import requests

key = "32ed8a8b76c97e4981a86e0c2c87b762"
url = "http://api.marketstack.com/v1/eod"

def get_stock():
    params = {
        "access_key": key,
        "symbols": "AAPL",
    }
    response = requests.get(url, params = params)

    if response.status_code == 200:
        data = response.json()
        if "data" in data and len(data["data"]) > 0:
            latest = data["data"][0]
            symbol = latest["symbol"]
            date = latest["date"]
            close_price = latest["close"]
            print(f"Symbol: {symbol}")
            print(f"Date: {date}")
            print(f"Closing Price: {close_price}")
        else:
            print("No data.")
    else:
        print(f"Error {response.status_code}")
get_stock()