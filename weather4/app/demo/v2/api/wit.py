from .openweathermap import get_weather_forecast
from .yelp import get_restaurant
from .credentials import WIT_TOKEN
import requests

def ask_wit(expression):
	result = requests.get('https://api.wit.ai/message?v=20201026&q={}'.format(expression), headers={'Authorization': WIT_TOKEN})
	jsonResult = result.json()
	try:
		if jsonResult['intents'][0]['name'] == "GetWeatherInformation":
			location = jsonResult['entities']['wit$location:location'][0]['resolved']['values'][0]['name']
			answer = get_weather_forecast(location)
		elif jsonResult['intents'][0]['name'] == "FindRestaurant":
			location = jsonResult['entities']['wit$location:location'][0]['resolved']['values'][0]['name'] 
			term = jsonResult['entities']['wit$local_search_query:local_search_query'][0]['value']
			answer = get_restaurant(term,location)
	except KeyError as err:
		answer = "I dont understand"
	return answer