from .credentials import YELP_API_KEY
import requests

def get_restaurant(term,location):
	result = requests.get('https://api.yelp.com/v3/businesses/search?term={}&location={}'.format(term,location), headers={'Authorization': YELP_API_KEY})
	jsonResult = result.json()
	answer = '\n'
	try:
		for x in jsonResult['businesses']:
			answer += (x['name']+'\t'+x['phone']+'\n')
	except KeyError as err:
		answer = "I dont understand"
	return answer
