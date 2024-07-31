import requests
from PIL import ImageTk

ENDPOINT = 'https://api.weather.yandex.ru/graphql/query'
API_TOKEN = 'your_api_token'

HEADERS = {

    'X-Yandex-Weather-Key': API_TOKEN
}


WEATHER_CONDITION = {
    'CLEAR': 'clear',
    'PARTLY_CLOUDY': 'cloudy',
    'CLOUDY': 'cloudy',
    'OVERCAST': 'overcast',
    'LIGHT_RAIN': 'rain',
    'RAIN': 'rain',
    'HEAVY_RAIN': 'rain',
    'SHOWERS': 'rain',
    'SLEET': 'snow',
    'LIGHT_SNOW': 'snow',
    'SNOW': 'snow',
    'SNOWFALL': 'snow',
    'HAIL': 'rain',
    'THUNDERSTORM': 'rain',
    'THUNDERSTORM_WITH_RAIN': 'rain',
    'THUNDERSTORM_WITH_HAIL': 'rain',
}


def get_weather(lat, lon):
    query = '''{
    weatherByPoint(request: { lat: %g, lon: %g }) {
        now {
        temperature
        humidity
        precType
        windSpeed
        windDirection
        cloudiness
        condition
        }
    }
    }''' % (lat, lon)

    response = requests.post(ENDPOINT, headers=HEADERS, json={'query': query})
    weather = response.json()
    return weather['data']['weatherByPoint']['now']


def get_pictures(weather):
    condition = WEATHER_CONDITION[weather['condition']]
    bg = ImageTk.PhotoImage(file='assets/backgrounds/'+condition+'.jpg')
    weather_cond = ImageTk.PhotoImage(
        file='assets/weather_cond/'+condition+'.jpg')
    return bg, weather_cond
