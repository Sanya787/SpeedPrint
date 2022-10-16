import sys

from extra import Window
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.click_button = 0
        self.initUI()

    def load_interface(self):
        uic.loadUi('project.ui', self)
        self.button_start = self.findChild(QPushButton, 'pushButton_62')
        self.button_start.clicked.connect(self.start_button_func)
        self.timer = self.findChild(QLabel, 'label_10')

    def start_button_func(self):
        pass

    def initUI(self):
        self.load_interface()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()

    app2 = QApplication(sys.argv)
    window2 = Window()
    window2.show()
    sys.exit(app2.exec())
    sys.exit(app.exec())
