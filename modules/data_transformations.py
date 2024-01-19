import re
def transform_game_to_db(game):
    try:
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
        r = re.search('\d\d\d\d', game['data']['release_date']['date'])
        year = r.group(0) if r else ''
        datamodel['year_of_publication'] = year
    except KeyError as err:
        return 400
    return datamodel