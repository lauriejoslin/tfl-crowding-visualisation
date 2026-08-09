import requests
import os
from dotenv import load_dotenv

URL_TEXT = 'https://api.tfl.gov.uk/crowding/{Naptan}/{DayOfWeek}'
# Need to issue auth token?

def get_app_key():
    load_dotenv()

    primary_key = os.getenv('PRIMARY_KEY')
    secondary_key = os.getenv('SECONDARY_KEY')

    # Via https://techforum.tfl.gov.uk/t/application-id-and-key/3595 - add either into query_string
    return primary_key

def get_crowding(naptan: str, dow: str):

    app_key = get_app_key()

    url = URL_TEXT.format(Naptan=naptan, DayOfWeek=dow)
    data = requests.get(url, params=app_key)

    if data.status_code != requests.codes.ok:
        return "ERROR: Failed to fetch data, check query"

    return data

