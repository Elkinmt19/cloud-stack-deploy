# Built-in imports
import io
import os
import logging

# External imports
import boto3
import requests
import pandas as pd

API_TOKEN = os.environ.get('API_TOKEN')
HEADERS = { 'X-Auth-Token': API_TOKEN }
AWS_S3_BUCKET = os.environ.get('AWS_S3_BUCKET')

s3_client = boto3.client("s3")

logging.basicConfig(
    level=logging.INFO,
    format='%(process)d-%(levelname)s-%(message)s'
)

def handler(event, context):
    URI = 'https://api.football-data.org/v4/teams/64/?season=2021'

    response = requests.get(URI, headers=HEADERS)

    STATUS_CODE = response.status_code

    liverpool_players_json = response.json()["squad"]

    liverpool_players = pd.DataFrame(liverpool_players_json)

    with io.StringIO() as csv_buffer:
        liverpool_players.to_csv(csv_buffer, index=False)

        response = s3_client.put_object(
            Bucket=AWS_S3_BUCKET, Key="liverpool_players.csv", Body=csv_buffer.getvalue()
        )

        status = response.get("ResponseMetadata", {}).get("HTTPStatusCode")

        if ((STATUS_CODE == 200) and (status == 200)):
            logging.info(f"Successful S3 get_object response. Status - {status}")
            return f"liverpool_players: {liverpool_players.to_dict()}"
        else:
            raise Exception(f"Unsuccessful S3 get_object response.")