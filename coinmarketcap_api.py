""" CoinMarketCap API Interface """

import json
import os
from dotenv import load_dotenv
from requests import Session

# CoinMarketCap documentation: https://coinmarketcap.com/api/documentation/v1

# Version 1 live end point (deprecated):
# https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest

# Version 1 sandbox (test data) end point (deprecated)
# https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest

# Version 2 end point:
# https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest


class CMC:
    """ Main CoinMarketCap class to access the API """

    def __init__(self):
        load_dotenv()  # load environment variables stored in .env file
        self.api_key = os.environ.get('COINMARKETCAP_API_KEY')
        self.api_url = 'https://pro-api.coinmarketcap.com'
        self.headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': self.api_key
        }
        self.session = Session()
        self.session.headers.update(self.headers)

    def get_all_coins(self):
        """ returns data for all coins """
        url = self.api_url + '/v1/cryptocurrency/map'
        # get response as json
        response_json = self.session.get(url)
        # convert to dictionary
        response_dictionary = json.loads(response_json.text)
        data = response_dictionary['data']
        return data

    def get_price(self, symbol, currency):
        """ returns the price of the given coin in the given currency """
        url = self.api_url + '/v2/cryptocurrency/quotes/latest'
        parameters = {
            'symbol': symbol,
            'convert': currency  # the currency to display the price in
        }
        # get response as json
        response_json = self.session.get(url, params=parameters)
        # convert to dictionary
        response_dictionary = json.loads(response_json.text)
        price = response_dictionary['data'][symbol][0]['quote'][currency]['price']
        return round(price, 2)  # returns the price to two decimal places
