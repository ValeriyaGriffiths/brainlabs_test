import requests
import random


def get_country_data_from_external_api():
    """Fetches a random country and its capital from https://countriesnow.space/api/v0.1/countries/capital."""
    api_url = 'https://countriesnow.space/api/v0.1/countries/capital'
    response = requests.get(api_url)
    countries = response.json()['data']

    return random.choice(countries)

