import pymongo
from modules.data_transformation import transform_game_to_db
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
    mongo_conn = MongoFunctions()
    lib = mongo_conn.find_all('MyGameLibrary')

    for game in lib:
        datamodel = transform_game_to_db(game)
        response.append(datamodel)
        print(f"Key not found {err}")
    return response

def get_game(title):
    mongo_conn = MongoFunctions()
    response = mongo_conn.find_one('MyGameLibrary', {'data.name': title})
    datamodel = {
        "title": '',
        "genres": [],
        "publishers": '',
        "year_of_publication": '',
        'tags': []
    }
    datamodel['title'] = response['data']['name']
    datamodel['genres'] = [x['description'] for x in response['data']['genres']]
    datamodel['publishers'] = response['data']['publishers']
    datamodel['year_of_publication'] = response['data']['release_date']['date']
    return datamodel