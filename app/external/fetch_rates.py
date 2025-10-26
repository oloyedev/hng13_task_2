import requests
from ..config import settings

def fetch_exchange_rates():
    try:
        response = requests.get(settings.EXCHANGE_RATE_API_URL, timeout=15)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        raise ConnectionError(f"Could not fetch data from Exchange Rate API: {e}")

    return data.get("rates", {})
