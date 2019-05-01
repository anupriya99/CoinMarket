import json
import requests
from datetime import datetime

currency = 'INR'

global_url='https://api.coinmarketcap.com/v2/global/?convert=' + currency

request = requests.get(global_url)
results = request.json()

print(json.dumps(results,sort_keys=True,indent=4))


active_currencies = results['data']['active_cryptocurrencies']
active_markets = results['data']['active_markets']
bitcoin_percentage = results['data']['bitcoin_percentage_of_market_cap']
last_updated = results['data']['last_updated']
global_cap = int(results['data']['quotes'][currency]['total_market_cap'])
global_volume = int(results['data']['quotes'][currency]['total_volume_24h'])


active_currencies_string='{:,}'.format(active_currencies)
active_markets_strings = '{:,}'.format(active_markets)
global_cap_strings = '{:,}'.format(global_cap)
global_volume_strings = '{:,}'.format(global_volume)
last_updated_strings = datetime.fromtimestamp(last_updated).strftime('%B %d,%Y at %I:%M%p')

print()
print('there are currently ' +str(active_currencies_string) +'active_cryptocurrencies and' +str(active_markets_strings)+ 'active_markets')
print('global cap of all crypto is ' + str(global_cap_strings) + ' and 24h global vloume is' +str(global_volume_strings)+ '.')
print('Bitcoin\'s total percentage of global cap is ' +str(bitcoin_percentage)+ '%.')
print('last updated on' +str(last_updated_strings)+ '.')
