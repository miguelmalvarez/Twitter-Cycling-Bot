import configparser
from weather import weather_data
from clothes import gear_recommendation
from twitter import tweet_recommendation

# TODO: Add logs
# TODO: Add debugging flag with no tweeting


def main(event=None, context=None):
    # Intitialisation
    config = configparser.ConfigParser()
    config.read('config.cfg')

    weather_forecast = weather_data(config)
    clothes = gear_recommendation(weather_forecast)
    tweet_recommendation(config, weather_forecast, clothes)


if __name__=='__main__':
    main()