""" Crypto Portfolio - Rich """
import sys

# add parent directory to path to enable command line imports
sys.path.append("..")

from forex_python.converter import CurrencyRates
from rich import box
from rich.panel import Panel
from rich.console import Console
from rich.table import Table
from coinmarketcap_api import CMC


class CryptoPortfolioRich:
    """ Prints Crypto Portfolio valuations to the terminal using Rich """

    holdings_dictionary = {
        'AAVE':  '1.202',
        'ADA':   '4946.116682',
        'BNB':   '1.0903',
        'BTC':   '0.4018',
        'DOT':   '30.192',
        'EGLD':  '3.6244',
        'ETH':   '10.782',
        'LINK':  '80.1',
        'MATIC': '1197.1916',
        'SFM':   '110959.28',
        'SOL':   '82.631414',
        'VET':   '28456.97',
        'VTHO':  '2913.97',
        'WEYU':  '115996.79584337',
        'XLM':   '48.2625393',
        'XRP':   '5006.00',
        'ZIL':   '13095.8387'
    }

    portfolio_data_dictionary = {}

    def __init__(self):
        self.cmc = CMC()
        self.console = Console()
        self.create_portfolio_dictionary()
        self.print_portfolio_table()

    def create_portfolio_dictionary(self):
        """ Creates the portfolio data structure """
        # create comma seperated string of holdings symbols
        symbols_csv_string = ",".join(self.holdings_dictionary.keys())

        # get prices for all crypto holdings
        response_dictionary = self.cmc.get_prices(symbols_csv_string, 'USD')

        currency_rates = CurrencyRates()
        # get the current USD/GBP rate
        usd_gbp_rate = currency_rates.get_rate('USD', 'GBP')

        btc_price = response_dictionary['data']['BTC'][0]['quote']['USD']['price']

        for key in self.holdings_dictionary:
            crypto_name = response_dictionary['data'][key][0]['name']
            crypto_price_float = response_dictionary['data'][key][0]['quote']['USD']['price']
            try:
                holding_amount_float = float(self.holdings_dictionary.get(key))
            except ValueError:
                self.console.print(f"Error in create_crypto_dictionary(): Invalid value in holdings_dictionary for key: {key}")
                sys.exit()


            holding_usd_value_float = holding_amount_float * crypto_price_float
            holding_usd_value_string = "%.2f" % holding_usd_value_float
            holding_gbp_value_string = "%.2f" % ((holding_amount_float * crypto_price_float) * usd_gbp_rate)
            holding_btc_value_string = "%.6f" % (holding_usd_value_float / btc_price)
            self.portfolio_data_dictionary[key] = {
                "Amount": holding_amount_float,
                "Name": crypto_name,
                "Current Price": crypto_price_float,
                "USD Value": holding_usd_value_string,
                "GBP Value": holding_gbp_value_string,
                "BTC Value": holding_btc_value_string
            }

    def print_portfolio_table(self):
        """ Prints the portfolio table """

        usd_total_float = 0
        btc_total_float = 0

        for key, value in self.portfolio_data_dictionary.items():
            usd_total_float += float(value['USD Value'])
            btc_total_float += float(value['BTC Value'])

        usd_total_string = str("%.2f" % usd_total_float)
        btc_total_string = (str("%.6f" % btc_total_float))

        currency_rates = CurrencyRates()
        usd_gbp_rate = currency_rates.get_rate('USD', 'GBP')
        gbp_total_float = usd_total_float * usd_gbp_rate
        gbp_total_string = str("%.2f" % gbp_total_float)

        portfolio_table = Table(title="Crypto Portfolio",
                                show_footer=True,
                                box=box.ROUNDED)
        portfolio_table.add_column('Name',
                                   style="cyan")
        portfolio_table.add_column('Symbol',
                                   style="white")
        portfolio_table.add_column('Amount',
                                   justify="right",
                                   style="magenta",)
        portfolio_table.add_column('Current Price',
                                   justify="right",
                                   style="blue")
        portfolio_table.add_column('USD Value',
                                   justify="right",
                                   style="green",
                                   footer="$ " + usd_total_string)
        portfolio_table.add_column('GBP Value',
                                   justify="right",
                                   style="green",
                                   footer="£ " + gbp_total_string)
        portfolio_table.add_column('BTC Value',
                                   justify="right",
                                   style="gold3",
                                   footer="BTC " + btc_total_string)

        for key, value in self.portfolio_data_dictionary.items():
            name_string = value['Name']
            symbol_string = key
            amount_string = str("%.6f" % value['Amount'])
            price_string = str("%.6f" % value['Current Price'])
            usd_value_string = str(value['USD Value'])
            gbp_value_string = str(value['GBP Value'])
            btc_value_string = str(value['BTC Value'])
            portfolio_table.add_row(name_string,
                                    symbol_string,
                                    amount_string,
                                    price_string,
                                    "$ " + usd_value_string,
                                    "£ " + gbp_value_string,
                                    "BTC " + btc_value_string)

        self.console.print(portfolio_table)

def main():
    """ main function - creates the application object """
    CryptoPortfolioRich()


if __name__ == '__main__':
    main()
