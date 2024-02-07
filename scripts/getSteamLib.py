"""
TODO:
- Get game information (tags, description, etc) from Steam API or elsewhere
- Load data into Mongo
"""

import json
import requests
import os
from html2text import html2text
from modules.convert_date import convert_date_to_iso
from modules.remove_html_parser import remove_html
from pymongo import MongoClient
from time import sleep
from requests.exceptions import HTTPError, Timeout, TooManyRedirects

KEY = os.getenv("STEAM_API_KEY")
USER_ID = os.getenv("STEAM_ID")

def get_games_library():
    """
    Returns:
        data (list): The game library metadata for the supplied user in the following format:
            {'appid': 1361210,
            'playtime_disconnected': 0,
            'playtime_forever': 0,
            'playtime_linux_forever': 0,
            'playtime_mac_forever': 0,
            'playtime_windows_forever': 0,
            'rtime_last_played': 0}
    Raises:
        HTTPError: Raises error if HTTP response not 'good'
        Timeout: Raises error, retries once, and exits if timeout limit reached
        TooManyRedirects: Raises error, exits
    """
    try:
        response = requests.get(f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={KEY}&steamid={USER_ID}&format=json")
        data = response.json()

        if response.status_code != 200:
            raise HTTPError
    except HTTPError as err:
        print(f"HTTP Error {response.status_code}: {response.text}")
        print(err)
    except Timeout:
        print("Timeout received from Steam API, retrying...")
        response = requests.get(f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={KEY}&steamid={USER_ID}&format=json")
        if response.status_code == 200:
            return response
        print("Unable to connect, exiting...")
        raise SystemExit()
    except TooManyRedirects:
        print("You have hit the redirect limit for this resource. This could be to a broken resource or misconfigured client headers.")
        print("exiting")
        raise SystemExit()
    return data['response']['games']

def get_game_info(app_id):
    """
    Args:
        app_id (str): The id key for the game metadata entry
    Returns:
        new_data (str): The game description data stripped of HTML
    Raises:
        HTTPError: Raises error if HTTP response not 'good'
        Timeout: Raises error, retries once, and exits if timeout limit reached
        TooManyRedirects: Raises error, exits
    """
    try:
        response = requests.get(f"https://store.steampowered.com/api/appdetails?appids={app_id}")
        if response.status_code != 200:
            raise HTTPError
    except HTTPError as err:
        print(f"HTTP Error {response.status_code}: {response.text}")
        print(err)
    except Timeout:
        print("Timeout received from Steam API, retrying...")
        response = requests.get(f"https://store.steampowered.com/api/appdetails?appids={app_id}")
        if response.status_code == 200:
            return remove_html(response.json())
        print("Unable to connect, exiting...")
        raise SystemExit()
    except TooManyRedirects:
        print("You have hit the redirect limit for this resource. This could be to a broken resource or misconfigured client headers.")
        print("exiting...")
        raise SystemExit()
    
    data = response.json()
    new_data = remove_html(data)
    return new_data

def load_mongo_db(games_library):
    client = MongoClient('localhost', 27017)
    db = client.Steam
    collection = db.MyGameLibrary
    collection.insert_many(games_library)


def main():
    owned_games = get_games_library()
    load_data = []
    game_data = []
    for game in owned_games:
        detailed_info = get_game_info(game['appid'])
        game_data.append(detailed_info)
        sleep(10)        
    for game in game_data:
        try:
            keys = [x for x in game.keys()]
            game_data = game[keys[0]]
            try:
                game['data']['release_date']['date'] = convert_date_to_iso(game['data']['release_date']['date'])
            load_data.append(game_data)
        except KeyError as err:
            print(f"{err} not found in {game}")
        except IndexError as err:
            print(keys)
            print(game)
    load_mongo_db(load_data)

if __name__ == '__main__':
    main()