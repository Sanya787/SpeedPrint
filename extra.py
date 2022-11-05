"""Launching the extra program window."""

import webbrowser

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QPushButton


class Window(QWidget):
    """Control the window.

    Args:
        - input - Nothing

    Returns:
        - output - Nothing
    """

    def __init__(self):
        """Call the main function.

        Args:
            - input - Nothing

        Returns:
            - output - Nothing
        """
        super().__init__()
        self.initUI()

    def initUI(self):
        """Load the interface and defines the main variables.

        Args:
            - input - Nothing

        Returns:
            - output - Nothing
        """
        uic.loadUi('extra.ui', self)

        self.button_start = self.findChild(QPushButton, 'pushButton_63')
        self.button_start.clicked.connect(self.button_click)

    def button_click(self):
        """Bound to a link button.

        Args:
            - input - Nothing

        Returns:
            - output - Nothing
        """
        webbrowser.open('https://www.ratatype.ua/ru/learn/', new=2)
