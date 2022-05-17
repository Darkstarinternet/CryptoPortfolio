""" Crypto Portfolio """

import sys  # Needed to use command line parameters

from PySide2.QtWidgets import QVBoxLayout, QLabel, QApplication, QWidget


class CryptoPortfolio(QWidget):
    """ main Crypto Portfolio window class """
    def __init__(self):
        super().__init__()  # call the parent constructor
        self.init_ui()
        self.show()  # display the Crypto Portfolio window

    def init_ui(self):
        """ initialise the user interface """
        _vertical_layout = QVBoxLayout()
        _title_label = QLabel()
        _title_label.setText("Crypto Portfolio")
        _vertical_layout.addWidget(_title_label)
        self.setLayout(_vertical_layout)


def main():
    """ creates the application """
    _crypto_portfolio_application = QApplication(sys.argv)
    _crypto_portfolio = CryptoPortfolio()
    _crypto_portfolio_application.exec_()  # start the event loop
    sys.exit()


if __name__ == '__main__':
    main()
