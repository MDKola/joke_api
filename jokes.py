import requests

def make_me_laugh():

	url = 'http://api.icndb.com/jokes/random'

	response = requests.get(url)
	data = response.json()

	
	return data['value']['joke']
print('')
print(make_me_laugh())



