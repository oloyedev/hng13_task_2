import requests
from ..config import settings

def fetch_countries():
    try:
        response = requests.get(settings.COUNTRY_API_URL, timeout=15)
        response.raise_for_status()
        countries = response.json()
    except requests.RequestException as e:
        raise ConnectionError(f"Could not fetch data from REST Countries API: {e}")

    result = []
    for country in countries:
        name = country.get("name")
        capital = country.get("capital")
        region = country.get("region")
        population = country.get("population") or 0
        flag_url = country.get("flag") 

 
        currencies = country.get("currencies") or []
        currency_code = None
        if isinstance(currencies, list) and len(currencies) > 0:
            first_currency = currencies[0]
            currency_code = first_currency.get("code")

        result.append({
            "name": name,
            "capital": capital,
            "region": region,
            "population": population,
            "flag_url": flag_url,    
            "currency_code": currency_code
        })

    return result
