import json


def convertData(match, stats):
    row = {}

    row["fixture_id"] = match["fixture"]["id"]
    row["season"] = match["league"]["season"]

    if match["teams"]["home"]["id"] == 529:
        # Barcelona jest gospodarzem
        row["is_home"] = True
        row["opp_name"] = match["teams"]["away"]["name"]
    else:
        # Barcelona gra na wyjeździe
        row["opp_name"] = match["teams"]["home"]["name"]
        row["is_home"] = False
