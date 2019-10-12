# Twitter-Cycling-Bot

One of the challenges of cyling to work is that the weather in many cities (e.g., London in my case) changes quite dramatically from day to day and the cycling gear and clothes will be completely dependent on these conditions.

This project is a (slightly-overengineered) way to solve the proble, mainly driven by fun. The idea is to create a Twitter bot (that will be hosted probably in AWS Lambda) that will check the weather forecast (using a 3rd party API) every morning and will tweet, based on the weather factors, a recommendation for the clothes to wear that day.