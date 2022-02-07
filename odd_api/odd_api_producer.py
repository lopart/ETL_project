import requests
import json

API_KEY = 'YOUR_API_KEY'
SPORT = 'basketball_nba'
REGIONS = 'eu'
MARKETS = 'h2h'
ODDS_FORMAT = 'decimal'
DATE_FORMAT = 'iso'

odds_response = requests.get(
	f'https://api.the-odds-api.com/v4/sports/{SPORT}/odds',
	params={
		'api_key': API_KEY,
		'regions': REGIONS,
		'markets': MARKETS,
		'oddFormat': ODDS_FORMAT,
		'dateFormat': DATE_FORMAT,
	}
)

if odds_response.status_code != 200:
    print(f'Failed to get odds: status_code {odds_response.status_code}, response body {odds_response.text}')

else:
    odds_json = odds_response.json()
    output_file = open("input_file.json", "w")
    json.dump(odds_json, output_file, indent = 2)
    output_file.close()
    print('Number of events:', len(odds_json))
    print(odds_json)

    print('Remaining requests', odds_response.headers['x-requests-remaining'])
    print('Used requests', odds_response.headers['x-requests-used'])
