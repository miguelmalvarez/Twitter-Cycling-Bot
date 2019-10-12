import configparser
from weather import weather_data
from clothes import gear_recommendation
from twitter import tweet_recommendation

def main():
    ## Intitialisation
    config = configparser.ConfigParser()
    config.read('config.cfg')

    ## Weather
    weather_forecast = weather_data(config)

    ## Recommendation
    clothes = gear_recommendation(weather_forecast)

    ## Tweet
    tweet_recommendation(config, weather_forecast, clothes)

if __name__=='__main__':
    main()