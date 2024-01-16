
def transform_game_to_db(game):
    datamodel = {
        "title": '',
        "genres": [],
        "publishers": '',
        "year_of_publication": '',
        'tags': []
    }
    datamodel['title'] = game['data']['name']
    datamodel['genres'] = [x['description'] for x in game['data']['genres']]
    datamodel['publishers'] = game['data']['publishers']
    datamodel['year_of_publication'] = game['data']['release_date']['date']
    return datamodel