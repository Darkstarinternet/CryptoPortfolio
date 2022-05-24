""" CoinMarketCap API Interface """

import json
import os
from dotenv import load_dotenv
from requests import Session

# CoinMarketCap documentation: https://coinmarketcap.com/api/documentation/v1

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

    def get_prices(self, symbols_csv_string, currency):
        """
        Returns prices in the given currency for all symbols in the
        given comma separated string
        """
        url = self.api_url + '/v2/cryptocurrency/quotes/latest'
        parameters = {
            'symbol': symbols_csv_string,
            'convert': currency  # the currency to display the price in
        }
        # get response as json
        response_json = self.session.get(url, params=parameters)
        response_dictionary = json.loads(response_json.text)
        return response_dictionary
