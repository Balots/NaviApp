import requests
from app.config import YANDEX_MAPS_API_KEY

search_url = "https://search-maps.yandex.ru/v1/"

def search_places(query, ll="60.604135,56.838664", spn="0.5,0.5", lang="ru_RU"):
    params = {
        "apikey": YANDEX_MAPS_API_KEY,
        "text": query,
        "ll": ll,  # Координаты центра Екатеринбурга
        "spn": spn,  # Масштаб поиска
        "lang": lang
    }
    response = requests.get(search_url, params=params)
    return response.json()

def extract_places(data):
    places = []
    for feature in data.get("features", []):
        place = {
            "name": feature["properties"].get("name"),
            "address": feature["properties"].get("description"),
            "category": feature["properties"].get("companyMetaData", {}).get("Categories", [{}])[0].get("name"),
            "coordinates": feature["geometry"]["coordinates"]
        }
        places.append(place)
    return places
