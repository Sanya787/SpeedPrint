import sys

from extra import Window
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QTextBrowser


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.click_button = 0
        self.initUI()

    def append_widget(self, mark):
        '''Displays a pop-up window with the result of the test'''

        if mark == 'good':
            pass
        else:
            pass

    def load_interface(self):
        '''This method loads the entire interface into the widget
        Returns nothing'''

        uic.loadUi('project.ui', self)
        self.button_start = self.findChild(QPushButton, 'pushButton_62')
        self.button_start.clicked.connect(self.start_button_func)
        self.timer = self.findChild(QLabel, 'label_10')
        self.browser = self.findChild(QTextBrowser, 'textBrowser')

    def start_button_func(self):
        '''This method is bound to the "Начать" button.
         Gets the text from the database and passes it to the test_moment method'''
        self.browser.setText("Какой-то текст из базы данных")
        pass

    def initUI(self):
        '''This main func in class App. This method is the binder of all other methods.
        Returns nothing'''
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
