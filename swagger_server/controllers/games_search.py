import pymongo
from modules.data_transformations import transform_game_to_db
from modules.mongo_functions import MongoFunctions
from modules.settings import Settings

def search_game_title(title):
    mongo_conn = MongoFunctions()
    response = []
    lib = mongo_conn.find_all(collection='MyGameLibrary',
                                search_query={"data.name": {"$regex": title}})
    for game in lib:
        datamodel = transform_game_to_db(game)
        if datamodel not in response:
            response.append(datamodel) 
    return response

def search_game_year(year):
    mongo_conn = MongoFunctions()
    response = []
    lib = mongo_conn.find_all(collection='MyGameLibrary',
                                search_query={"data.release_date.date": {"$regex": year}})
    for game in lib:
        datamodel = transform_game_to_db(game)
        if datamodel not in response:
            response.append(datamodel) 
    return response

def search_game_genres(genres):
    # TODO: OR, AND, or both search operands??
    mongo_conn = MongoFunctions()
    response = []
    for genre in genres:
        lib = mongo_conn.find_all(collection='MyGameLibrary',
                                  search_query={"data.genres": {"$elemMatch":{'description': genre}}})
        for game in lib:
            datamodel = transform_game_to_db(game)
            if datamodel not in response:
                response.append(datamodel)
    return response


def search_game_date_range(date_range):
    mongo_conn = MongoFunctions()
    response = []
    lib = mongo_conn.find_all(collection='MyGameLibrary',
                                search_query={"data.release_date.date": {"$regex": year}})
    for game in lib:
        datamodel = transform_game_to_db(game)
        if datamodel not in response:
            response.append(datamodel) 
    return None

def search_game_publisher(publisher):
    mongo_conn = MongoFunctions()
    response = []
    lib = mongo_conn.find_all(collection='MyGameLibrary',
                                search_query={"data.publishers": {"$regex": title}})
    for game in lib:
        datamodel = transform_game_to_db(game)
        if datamodel not in response:
            response.append(datamodel) 
    return response