import pymongo
import urllib
from modules.settings import Settings

class MongoFunctions:
    def __init__(self):

        # self.db_user = self.settings.db_user
        # self.db_password = self.settings.db_password
        self.settings = Settings('settings.yml')
        self.db_server = self.settings.db_server
        self.db_port = self.settings.db_port

        self.mongo_uri = "mongodb://" +\
            self.db_server + ":" + self.db_port +\
            "/?directConnection=true"
        mongo_client = pymongo.MongoClient(self.mongo_uri)
        self.steam_db = mongo_client["Steam"]


    def delete_one(self, document, collection):
        response = self.steam_db[collection].delete_one(document)
        return response
    
    def find_all(self, collection):
        response = []
        for _ in self.steam_db[collection].find():
            response.append(_)
        return response

    def find_one(self, collection, search_query):
        response = self.steam_db[collection].find_one(search_query)
        return response

    def update_one(self, collection, document):
        logger.info(f"Upserting {document['name']} into Database") # pylint: disable=line-too-long
        filtr = {
            "name":document['name']
        }
        try:
            mongo_id = self.steam_db[collection].update_one(filtr, {"$set": document},\
                                            upsert=True)
            logger.debug(mongo_id)
        except Exception as error:
            logger.critical("Issue writing to Database: ", error)
