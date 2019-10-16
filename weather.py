import requests
from datetime import datetime, timedelta

# TODO: Find rain probability


def time_slot_datapoint(openweather_response, day_to_predict, starting_timings):
    for datapoint in openweather_response['list']:
        if datetime.fromtimestamp(datapoint['dt']).date() == day_to_predict and datetime.fromtimestamp(
                datapoint['dt']).hour in starting_timings:
            return datapoint


def time_datapoint(openweather_response, day_to_predict, time):
    # The  best (3 hr) window of time to define our targeet timing will start at t-1, t or t+1
    return time_slot_datapoint(openweather_response, day_to_predict, [time-1, time, time+1])


def extract_timeslot_weather_data(datapoint):
    return {'dt': datetime.fromtimestamp(datapoint['dt']),
            'min_temperature': datapoint['main']['temp_min'],
            'max_temperature': datapoint['main']['temp_max'],
            'humidity': datapoint['main']['humidity'],
            'wind': datapoint['wind']['speed'],
            'meteorology': datapoint["weather"][0]['description'],
            # TODO: Look to use "Main" rather than id
            'meteorology_code': datapoint["weather"][0]['id']}


# It returns weather forecast data for today (if ran before 7am) or for tomorrow otherwise
# List of weather conditions: https://openweathermap.org/weather-conditions
def weather_data(config, morning_time=7, afternoon_time=18):
    weather_api_key = config['DEFAULT']['open_weather_key']

    # Sunrise / Sunset data (note: these times are computed for the day when the call is made)
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    city = 'London,uk'
    request = base_url + '?q={}&appid={}&units=metric'.format(city, weather_api_key)
    data = requests.get(request).json()
    day_weather = {'sunrise': datetime.fromtimestamp(data['sys']['sunrise']),
                   'sunset': datetime.fromtimestamp(data['sys']['sunset'])}

    # Forecast 3-hour windows data
    base_url = 'http://api.openweathermap.org/data/2.5/forecast'
    city = 'London,uk'
    request = base_url + '?q={}&appid={}&units=metric'.format(city, weather_api_key)
    data = requests.get(request).json()

    now = datetime.now()
    # If we run this after the morning time, we will predict for tomorrow
    if now.hour > morning_time:
        day_to_predict = (now + timedelta(days=1)).date()
    else:
        day_to_predict = now.date()

    weather = {'morning': {'sunrise': day_weather['sunrise']},
               'afternoon': {'sunset': day_weather['sunset']}}

    weather['morning'].update(extract_timeslot_weather_data(time_datapoint(data, day_to_predict, morning_time)))
    weather['afternoon'].update(extract_timeslot_weather_data(time_datapoint(data, day_to_predict, afternoon_time)))

    return weather
