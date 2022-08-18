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
    liverpool_players = pd.read_csv(
        s3_client.get_object(
            Bucket=AWS_S3_BUCKET,
            Key="liverpool_players.csv"
        )
    )
    top_scorers_pl = pd.read_csv(
        s3_client.get_object(
            Bucket=AWS_S3_BUCKET,
            Key="top_scorers.csv"
        )
    )

    top_liverpool_scorers = pd.merge(liverpool_players, top_scorers_pl, on="id", how="inner")[[
        "id","name_y","firstName","lastName","dateOfBirth_y","nationality_y","position_y"
    ]].rename(columns={
        "name_y":"name","dateOfBirth_y":"dateOfBirth","nationality_y":"nationality","position_y":"position"
    })

    with io.StringIO() as csv_buffer:
        top_liverpool_scorers.to_html(csv_buffer, index=False)

        response = s3_client.put_object(
            Bucket=AWS_S3_BUCKET, Key="top_liverpool_scorers.html", Body=csv_buffer.getvalue()
        )

        status = response.get("ResponseMetadata", {}).get("HTTPStatusCode")

        if (status == 200):
            logging.info(f"Successful S3 get_object response. Status - {status}")
            return f"top_liverpool_scorers: {top_liverpool_scorers.to_dict()}"
        else:
            raise Exception(f"Unsuccessful S3 get_object response.")