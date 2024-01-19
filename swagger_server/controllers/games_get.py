import pymongo
from modules.data_transformations import transform_game_to_db
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
    return response

def get_game(title):
    mongo_conn = MongoFunctions()
    response = mongo_conn.find_one('MyGameLibrary', {'data.name': title})
    datamodel = transform_game_to_db(response)
    return datamodel
