import requests
import urllib
import json

nasa_url_iss_position = 'http://api.open-notify.org/iss-now.json'
raw_request = requests.get(nasa_url_iss_position)
#get the raw json information
print(raw_request.text)

iss_json = raw_request.json()
print('This is the current timestamp: ', iss_json['timestamp'])
print('Latitude: ', iss_json['iss_position']['latitude'])
print('Longitude: ', iss_json['iss_position']['longitude'])
