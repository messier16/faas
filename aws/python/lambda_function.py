import requests
import json
import os
from twython import Twython


def lambda_handler(event, context):
    pokemon_id = event["pokemon_id"]
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/")
    pokemon =  json.loads(response.text)
    tweeted = tweet(pokemon)
    return { 
        "message": f"It is {pokemon['species']['name']}!", 
        "tweeted": tweeted 
    }

def tweet(pokemon):
    variables = [
        "API_KEY",
        "API_SECRET_KEY",
        "ACCESS_TOKEN", 
        "ACCESS_TOKEN_SECRET"
    ]
    if all(var in os.environ for var in variables):
        twitter = Twython(
            os.environ["API_KEY"],
            os.environ["API_SECRET_KEY"],
            os.environ["ACCESS_TOKEN"], 
            os.environ["ACCESS_TOKEN_SECRET"]
        )
        twitter.update_status(status=f"It is {pokemon['species']['name']}!")
        return True
    return False