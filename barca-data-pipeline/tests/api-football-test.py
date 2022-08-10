import requests
import json
import os

import pandas as pd

from dotenv import (
    load_dotenv, find_dotenv
)

_ = load_dotenv(find_dotenv())

API_TOKEN = os.environ.get('API_TOKEN')
HEADERS = { 'X-Auth-Token': API_TOKEN }


def _fetch_top_scores_premier_league() -> pd.DataFrame:
    URI = 'https://api.football-data.org/v4/competitions/PL/scorers/?season=2021'

    response = requests.get(URI, headers=HEADERS)

    top_scorers_json = []

    for scorer in response.json()["scorers"]:
        top_scorers_json.append(scorer["player"])

    top_scores = pd.DataFrame(top_scorers_json)

    return top_scores

def _fetch_liverpool_players() -> pd.DataFrame:
    URI = 'https://api.football-data.org/v4/teams/64/?season=2021'

    response = requests.get(URI, headers=HEADERS)

    liverpool_players_json = response.json()["squad"]

    liverpool_players = pd.DataFrame(liverpool_players_json)

    return liverpool_players

def main():
    top_pl_scorers = _fetch_top_scores_premier_league()
    print(top_pl_scorers)

    liverpool_players = _fetch_liverpool_players()
    print(liverpool_players)


if __name__=="__main__":
    main()