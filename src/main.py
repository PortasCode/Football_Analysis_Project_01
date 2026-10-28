import json
from extract import getStats
from transform import convertData


def main():
    """
    Głowna funkcja systemu ETL
    """
    with open("Barcelona_fixtures_2022.json", "r") as f:
        data = json.load(f)
        matches = data["response"]

        for match in matches:
            fixture_id = int(match["fixture"]["id"])

            specificStats = getStats(fixture_id)

            row = convertData(match, specificStats)


if __name__ == "__main__":
    main()
