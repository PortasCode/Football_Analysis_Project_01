from dotenv import load_dotenv
import os
import json
import requests

load_dotenv()


def get_match_log():
    """
    Funkcja pobiera z API wszystkie mecze rozegrane przez FC Barcelone w sezonie 2022/2023
    """
    api_token = os.getenv("API_FOOTBALL")
    url = "https://v3.football.api-sports.io/fixtures"
    headers = {"x-apisports-key": api_token}
    params = {"season": 2022, "status": "FT-AET-PEN", "team": 529}

    response = requests.get(url, headers=headers, params=params)

    if not (response.status_code == 200 or response.status_code == 204):
        raise ConnectionError(
            f"Nie udało się pobrać danych z API (status {response.status_code})"
        )

    with open("Barcelona_fixtures_2022.json", "w") as f:
        json.dump(response.json(), f, indent=4)


def getStats(id_match: int):
    api_token = os.getenv("API_FOOTBALL")
    url = "https://v3.football.api-sports.io/fixtures/statistics"
    headers = {"x-apisports-key": api_token}
    params = {"fixture": id_match}

    response = requests.get(url, headers=headers, params=params)

    if not (response.status_code == 200 or response.status_code == 204):
        raise ConnectionError(
            f"Nie udało się pobrać danych z API (status {response.status_code})"
        )

    return response.json()["response"]
