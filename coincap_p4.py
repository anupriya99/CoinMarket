import math
import json
import locale
import requests
from prettytable import PrettyTable

locale.setlocale(locale.LC_ALL, ('de', 'utf-8'))

global_url = 'https://api.coinmarketcap.com/v2/global'
ticker_url = 'https://api.coinmarketcap.com/v2/ticker/?structure=array'

request = requests.get(global_url)
results = request.json()
data = results['data']

global_cap = int(data['quotes']['USD']['total_market_cap'])

table = PrettyTable(['Name' , 'Ticker', '% of total global cap', 'Current', '7.7T (Gold)', '36.8T (Narrow Money)', '73T (World Stock Money)', '90.4T (Broad Money)','217T (Real Estate)','544T (Derivatives)'])
request = requests.get(ticker_url)
results = request.json()
data = results['data']

for currency in data:
    name = currency['name']
    ticker = currency['symbol']
    percentage_of_global_cap = float(currency['quotes']['USD']['market_cap'])/ float(global_cap)

    current_price = round(float(currency['quotes']['USD']['price']),2)
    available_supply = float(currency['total_supply'])

    trilion7price = round(77000000000000 * percentage_of_global_cap / available_supply , 2)
    trilion36price = round(360000000000000 * percentage_of_global_cap / available_supply , 2)

    trilion73price = round(73000000000000 * percentage_of_global_cap / available_supply , 2)

    trilion90price = round(904000000000000 * percentage_of_global_cap / available_supply , 2)

    trilion217price = round(217000000000000 * percentage_of_global_cap / available_supply , 2)
    trilion544price = round(544000000000000 * percentage_of_global_cap / available_supply , 2)

    percentage_of_global_cap_string = str(round(percentage_of_global_cap*100,2)) + '%'
    current_price_string = '$' + str(current_price)
    trilion7price_string = '$' + local.format('%.2f',trilion7price,True)
    trilion36price_string = '$' + local.format('%.2f',trilion36price,True)
    trilion73price_string = '$' + local.format('%.2f',trilion73price,True)
    trilion90price_string = '$' + local.format('%.2f',trilion90price,True)
    trilion217price_string = '$' + local.format('%.2f',trilion217price,True)
    trilion544price_string = '$' + local.format('%.2f',trilion544price,True)

    table.add_row([name,
                    ticker,
                    percentage_of_global_cap_string,
                    current_price_string,
                    trilion7price_string,
                    trilion36price_string,
                    trilion73price_string,
                    trilion90price_string,
                    trilion217price_string,
                    trilion544price_string])

print()
print(table)
print()
