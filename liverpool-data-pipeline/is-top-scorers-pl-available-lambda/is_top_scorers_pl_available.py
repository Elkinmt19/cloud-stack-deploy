# Built-in imports
import os
import logging

# External imports
import requests

API_TOKEN = os.environ.get('API_TOKEN')
HEADERS = { 'X-Auth-Token': API_TOKEN }

logging.basicConfig(
    level=logging.INFO,
    format='%(process)d-%(levelname)s-%(message)s'
)

def handler(event, context):
    URI = 'https://api.football-data.org/v4/competitions/PL/scorers/?season=2021'

    logging.info("Starting the task")
    response = requests.get(URI, headers=HEADERS)

    STATUS_CODE = response.status_code

    if (STATUS_CODE == 200):
        logging.info("The task has been completely")
        return STATUS_CODE

    raise Exception(f"The entrypoint is unavailable")
