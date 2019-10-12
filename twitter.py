from tweepy import OAuthHandler, API

# TODO: Add emojis and pictures


def authorise_twitter_api(config):
    auth = OAuthHandler(config['DEFAULT']['consumer_key'],
                        config['DEFAULT']['consumer_secret'])
    auth.set_access_token(config['DEFAULT']['access_token'],
                          config['DEFAULT']['access_secret'])
    return auth


def tweet_recommendation(config, weather_forecast, recommendation):
    auth = authorise_twitter_api(config)
    api = API(auth, wait_on_rate_limit=True)
    message = 'Weather for {} in London\n'.format(weather_forecast['morning']['dt'].strftime("%A %d"))
    message += 'Morning - {} degrees (C) with {} kph wind. '.format(weather_forecast['morning']['min_temperature'],
                                                                    weather_forecast['morning']['wind'])
    message += 'Afternoon - {} degrees with {} kph wind.\n'.format(weather_forecast['afternoon']['min_temperature'],
                                                                   weather_forecast['afternoon']['wind'])

    message += recommendation
    return api.update_status(message)