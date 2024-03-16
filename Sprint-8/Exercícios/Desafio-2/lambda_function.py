import boto3
import chave_api
import requests
from datetime import datetime
import chaves_aws
import json


def fetch_tmdb_data(api_key, endpoint, params):
    url = f"https://api.themoviedb.org/3/{endpoint}"
    params["api_key"] = api_key

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Falha: {response.status_code}")
        return None


def fetch_war_movies(api_key, current_page=1):
    params = {
        "language": "pt-BR",
        "with_genres": 10752,
        "page": current_page,
    }  # 10752 genre de guerra
    endpoint = "discover/movie"

    return fetch_tmdb_data(api_key, endpoint, params)


def lambda_handler(event, context):
    api_key = chave_api.key
    bucket = "data-lake-aline-sp7"
    total_pages = float("inf")
    current_page = 1
    tmdb_data = []

    while current_page <= total_pages:
        tmdb_response = fetch_war_movies(api_key, current_page)

        if tmdb_response:
            print("OK")
            tmdb_data.extend(tmdb_response["results"])
            total_pages = tmdb_response["total_pages"]
            current_page += 1
        else:
            print("Falha")

    group_data = [tmdb_data[i : i + 100] for i in range(0, len(tmdb_data), 100)]
    current_date = datetime.now().strftime("%Y/%m/%d")

    for index, data_group in enumerate(group_data, start=1):
        upload_to_s3(json.dumps(data_group), bucket, f"tmdb_data_{index}", current_date)

acess_key = chaves_aws.acess_key
secret_key = chaves_aws.secret_key
session_token = chaves_aws.session_token
region_name = "us-east-1"
bucket = chaves_aws.bucket


def upload_to_s3(data, bucket, tipo, current_date):
    s3_key = f"Raw/tmdb/json/{current_date}/{tipo.lower()}.json"
    print(f"Caminho:{s3_key}")

    session = boto3.Session(
        aws_access_key_id=acess_key,
        aws_secret_access_key=secret_key,
        aws_session_token=session_token,
        region_name=region_name,
    )
    s3 = session.client("s3")
    print("Sessão criada")

    s3.put_object(Body=data, Bucket=bucket, Key=s3_key)
    print(f"Dados carregados para S3: s3://{bucket}/{s3_key}")