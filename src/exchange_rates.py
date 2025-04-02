import requests

def get_exchange_rate(currency):
    """
    Hämtar den aktuella valutakursen för given valuta i förhållande till SEK.
    """
    url = f"https://open.er-api.com/v6/latest/SEK"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Kunde inte hämta valutakurs")

    data = response.json()
    try:
        return data["rates"][currency]
    except KeyError:
        raise ValueError("Ogiltig valuta")
