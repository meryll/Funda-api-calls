import requests

API_KEY = 'ac1b0b1572524640a0ecc54de453ea9f'
WITH_GARDEN = 'tuin/'
BASE_URL = 'http://partnerapi.funda.nl/feeds/Aanbod.svc/{}/?type=koop&zo=/amsterdam/sorteer-datum-op/{}&page={}&pagesize=25'


def get(page_number, if_garden):
    if if_garden:
        garden = WITH_GARDEN
    else:
        garden = ''

    response = requests.get(BASE_URL.format(API_KEY, garden, page_number))

    if response.status_code == 401:
        print("Max number of requests reached.")

    if response.status_code != 200:
        raise Exception(str(response.content))

    return response.content