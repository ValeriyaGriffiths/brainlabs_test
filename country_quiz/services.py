import requests
import random


def get_country_data_from_external_api():
    """Fetches countries and capitals from https://countriesnow.space/api/v0.1/countries/capital.
    #TODO shuffle"""
    api_url = 'https://countriesnow.space/api/v0.1/countries/capital'
    response = requests.get(api_url)
    countries = response.json()['data']

    random.shuffle(countries)

    return countries

