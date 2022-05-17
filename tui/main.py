""" Crypto Portfolio Command Line Main File """
import sys
# add parent directory to path to enable command line imports
sys.path.append("..")

from rich import box
from rich.console import Console
from rich.table import Table
from coinmarketcap_api import CMC


class CryptoPortfolioTerminal:
    """ Prints Crypto Portfolio valuations to the terminal """

    btc_amount = 1.00
    eth_amount = 1.00
    sol_amount = 1.00
    ada_amount = 1.00
    xrp_amount = 1.00
    vet_amount = 1.00
    matic_amount = 1.00
    link_amount = 1.00
    zil_amount = 1.00
    dot_amount = 1.00
    bnb_amount = 1.00
    egld_amount = 1.00
    aave_amount = 1.00
    weyu_amount = 1.00
    sfm_amount = 1.00


    def __init__(self):
        self.cmc = CMC()
        self.console = Console()
        self.crypto_dictionary = {}
        self.create_crypto_dictionary()

    def create_crypto_dictionary(self):
        self.crypto_dictionary['BTC'] = {
            'Name': 'Bitcoin',
            'Amount': self.btc_amount
        }
        self.crypto_dictionary['ETH'] = {
            'Name': 'Ethereum',
            'Amount': self.eth_amount
        }
        self.crypto_dictionary['SOL'] = {
            'Name': 'Solana',
            'Amount': self.sol_amount
        }
        self.crypto_dictionary['ADA'] = {
            'Name': 'Cardano',
            'Amount': self.ada_amount
        }
        self.crypto_dictionary['XRP'] = {
            'Name': 'XRP',
            'Amount': self.xrp_amount
        }
        self.crypto_dictionary['VET'] = {
            'Name': 'VeChain',
            'Amount': self.vet_amount
        }
        self.crypto_dictionary['MATIC'] = {
            'Name': 'Polygon',
            'Amount': self.matic_amount
        }
        self.crypto_dictionary['LINK'] = {
            'Name': 'ChainLink',
            'Amount': self.link_amount
        }
        self.crypto_dictionary['ZIL'] = {
            'Name': 'Zilliqa',
            'Amount': self.zil_amount
        }
        self.crypto_dictionary['DOT'] = {
            'Name': 'Polygon',
            'Amount': self.dot_amount
        }
        self.crypto_dictionary['BND'] = {
            'Name': 'Binance',
            'Amount': self.bnb_amount
        }
        self.crypto_dictionary['EGLD'] = {
            'Name': 'EGold',
            'Amount': self.egld_amount
        }
        self.crypto_dictionary['AAVE'] = {
            'Name': 'AAVE',
            'Amount': self.aave_amount
        }
        self.crypto_dictionary['WEYU'] = {
            'Name': 'Weyu',
            'Amount': self.weyu_amount
        }
        self.crypto_dictionary['SFM'] = {
            'Name': 'Safemoon',
            'Amount': self.sfm_amount
        }

    def print_portfolio_table(self):
        """ Prints the tables """

        portfolio_table = Table(title="Crypto Portfolio", box=box.ROUNDED)

        portfolio_table.add_column('Name', style="cyan")
        portfolio_table.add_column('Symbol', style="yellow")
        portfolio_table.add_column('Price', justify="right", style="cyan")
        portfolio_table.add_column('Amount', justify="right", style="magenta")
        portfolio_table.add_column('USD Value', justify="right", style="green")

        for key, value in self.crypto_dictionary.items():
            crypto_name = value['Name']
            crypto_symbol = key
            crypto_amount = value['Amount']
            crypto_price = self.cmc.get_price(crypto_symbol, 'USD')
            crypto_usd_value = format((crypto_price * crypto_amount), '.2f')

            portfolio_table.add_row(crypto_name, crypto_symbol,
                                    str(crypto_price), str(crypto_amount),
                                    str(crypto_usd_value))

        self.console.print(portfolio_table)

    def print_totals_table(self):
        totals_table = Table(title="Total Value", box=box.ROUNDED)
        totals_table.add_column("Units", style="cyan")
        totals_table.add_column("Value", justify="right", style="green")

        usd_total = 0
        gbp_total = 0
        btc_total = 0
        eth_total = 0

        for key, value in self.crypto_dictionary.items():
            crypto_amount = value['Amount']
            crypto_symbol = key
            crypto_price = self.cmc.get_price(crypto_symbol, 'USD')
            crypto_usd_value = crypto_price * crypto_amount
            usd_total += crypto_usd_value

        totals_table.add_row("USD ($)", str(usd_total))
        totals_table.add_row("GBP (£)", "1")
        totals_table.add_row("BTC", "1")
        totals_table.add_row("ETH", "1")

        self.console.print(totals_table)


crypto_portfolio_terminal = CryptoPortfolioTerminal()
crypto_portfolio_terminal.print_portfolio_table()
crypto_portfolio_terminal.print_totals_table()
