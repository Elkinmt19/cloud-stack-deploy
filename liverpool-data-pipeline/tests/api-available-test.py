import requests
import os

from dotenv import (
    load_dotenv, find_dotenv
)

_ = load_dotenv(find_dotenv())

API_TOKEN = os.environ.get('API_TOKEN')
HEADERS = { 'X-Auth-Token': API_TOKEN }


def _is_available_top_scorers_premier_league():
    URI = 'https://api.football-data.org/v4/competitions/PL/scorers/?season=2021'

    response = requests.get(URI, headers=HEADERS)

    STATUS_CODE = response.status_code

    if (STATUS_CODE == 200):
        return STATUS_CODE

    raise Exception("The entrypoint is unavailable")

def _is_available_liverpool_players():
    URI = 'https://api.football-data.org/v4/teams/64/?season=2021'

    response = requests.get(URI, headers=HEADERS)

    STATUS_CODE = response.status_code

    if (STATUS_CODE == 200):
        return STATUS_CODE

    raise Exception("The entrypoint is unavailable")

def main():
    top_pl_scorers = _is_available_top_scorers_premier_league()
    print(top_pl_scorers)

    liverpool_players = _is_available_liverpool_players()
    print(liverpool_players)


if __name__=="__main__":
    main()