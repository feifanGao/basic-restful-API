from .credentials import WEATHER_API_KEY
import requests

def get_weather_forecast(location):
	result = requests.get('https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(location,WEATHER_API_KEY))
	jsonResult = result.json()
	try:
		weather = jsonResult['weather'][0]['description']
		temp = jsonResult['main']['temp'] - 273.15
		temp = int(temp)
		answer = "We have {} in {}, the temperature is {}'C.".format(weather,location,temp)
	except KeyError as err:
		answer = "I dont understand"
	return answer