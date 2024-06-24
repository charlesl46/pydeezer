from pydeezer.request import get

def country_infos():
    endpoint = "infos"
    json = get(endpoint)
    return json
