""" Crypto Portfolio """

import sys  # Needed to use command line parameters

from PySide2.QtWidgets import QApplication, QMainWindow


class CryptoPortfolio(QMainWindow):
    """ main Crypto Portfolio window class """
    def __init__(self):
        super().__init__()  # call the parent constructor
        self.show()  # display the BattleTask window


def main():
    """ creates the application """
    _crypto_portfolio_application = QApplication(sys.argv)
    _crypto_portfolio = CryptoPortfolio()
    _crypto_portfolio_application.exec_()  # start the event loop
    sys.exit()


if __name__ == '__main__':
    main()
