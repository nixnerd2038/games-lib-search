import pymongo
from modules.data_transformations import transform_game_to_db
from modules.mongo_functions import MongoFunctions
from modules.settings import Settings

# def search_game_title(title):
#     return None


def search_game_genres(genres):
    import ipdb; ipdb.set_trace()
    mongo_conn = MongoFunctions()
    response = []
    for genre in genres:
        lib = mongo_conn.find_one(collection='MyGameLibrary',
                                  search_query={"data.genres": {"$elemMatch":{"description":[genre]}}})
        for game in lib:
            datamodel = transform_game_to_db(game)
            response.append(datamodel)
    return response

# def search_game_date(date):
#     import ipdb; ipdb.set_trace()

#     return None

# def search_game_date_range(date_range):
#     import ipdb; ipdb.set_trace()

#     return None

# def search_game_publisher(publisher):
#     import ipdb; ipdb.set_trace()

#     return None