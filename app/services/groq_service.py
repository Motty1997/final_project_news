from app.groq_api.message import process_content
from app.repository.api_repo import fetch_articles
from app.settings.groq_config import groq_client
from app.utils.groq_utils import convert_groq_to_dict
from geopy import Photon



def get_lat_lon(city, country_name):
    geolocator = Photon(user_agent="geoapiExercises")
    try:
        location = geolocator.geocode(city)
        return {"lat":location.latitude, "lon":location.longitude}
    except:
        location = geolocator.geocode(country_name)
        return {"lat":location.latitude, "lon":location.longitude}


def get_all_news_obj(batch):
    events = []
    for event in batch:
        selected_data = {
            'date': event['date'],
            'dataType': event['dataType'],
            'body': event['body']
        }
        try:
            srt_res = process_content(selected_data, groq_client)
            dict_res = convert_groq_to_dict(srt_res)
        except (Exception, TypeError):
            continue
        event_data = {**selected_data, **dict_res}
        events.append(event_data)

    return events
