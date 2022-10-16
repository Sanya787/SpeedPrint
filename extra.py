import sys
import time
import webbrowser

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('extra.ui', self)
        self.button_start = self.findChild(QPushButton, 'pushButton_63')
        self.button_start.clicked.connect(self.button_click)

    def button_click(self):
        webbrowser.open('https://www.ratatype.ua/ru/learn/', new=2)