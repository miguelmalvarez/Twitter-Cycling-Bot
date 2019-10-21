from tweepy import OAuthHandler, API

# TODO: Add emojis and pictures
# TODO: Proper logging


def authorise_twitter_api(config):
    auth = OAuthHandler(config['DEFAULT']['consumer_key'],
                        config['DEFAULT']['consumer_secret'])
    auth.set_access_token(config['DEFAULT']['access_token'],
                          config['DEFAULT']['access_secret'])
    return auth


def tweet_recommendation(config, weather_forecast, recommendation):
    # Full emoji list in: http://unicode.org/emoji/charts/full-emoji-list.html
    bike_emoji = u'\U0001F6B4'

    auth = authorise_twitter_api(config)
    api = API(auth, wait_on_rate_limit=True)

    meteorology_codes = (weather_forecast['morning']['meteorology_code'],
                         weather_forecast['afternoon']['meteorology_code'])

    # TODO: Extend to more codes
    image = ''
    if 300 <= meteorology_codes[0] < 600 or 300 <= meteorology_codes[1] < 600:
        image = './images/rain.jpg'
    elif meteorology_codes[0] >= 800 or meteorology_codes[1] >= 800:
        image = './images/clear.jpg'

    message = '{} Weather for {} in London '.format(bike_emoji,
                                                    weather_forecast['morning']['dt'].strftime("%A %d"))
    message += '\nMorning: {} | {} °C. {} kph wind. '.format(weather_forecast['morning']['meteorology'],
                                                             weather_forecast['morning']['min_temperature'],
                                                             weather_forecast['morning']['wind'])
    message += '\nAfternoon: {} | {} °C. {} kph wind.\n'.format(weather_forecast['afternoon']['meteorology'],
                                                                weather_forecast['afternoon']['min_temperature'],
                                                                weather_forecast['afternoon']['wind'])

    message += recommendation
    print(message)

    if image == '':
        return api.update_status(message)
    else:
        return api.update_with_media(image, message)
