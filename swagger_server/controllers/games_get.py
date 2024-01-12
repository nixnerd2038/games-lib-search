import pymongo
from modules.mongo_functions import MongoFunctions
from modules.settings import Settings

def get_games_library():
    # TODO: Pagination?
    """
    Returns the entire library from MongoDB. 
    No args passed.

    Returns:
        games_library (list): The full list of games
    """
    raw_data = []
    response = []
    datamodel = {
        "title": '',
        "genres": [],
        "publishers": '',
        "year_of_publication": '',
        'tags': []
    }
    mongo_conn = MongoFunctions()
    lib = mongo_conn.find_all('MyGameLibrary')
    for game in lib:
        keys = [x for x in game.keys()]
        game_data = game[keys[1]]
        raw_data.append(game_data)
    for entry in raw_data:
        try:
            # TODO: Fix swagger dm 
            
            datamodel['title'] = entry['data']['name']
            datamodel['genres'] = entry['data']['genres']
            datamodel['publishers'] = entry['data']['publishers'] + entry['data']['developers']
            datamodel['year_of_publication'] = entry['data']['release_date']
        except KeyError as err:
            print(f"Key not found {err}")
        response.append(datamodel)
    return response

def get_game(title):
    pass