import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QCheckBox, QPlainTextEdit


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def load_interface(self):
        '''This method loads the entire interface into the widget
        Returns nothing'''

        pass

    def append_widget(self, mark):
        '''Displays a pop-up window with the result of the test'''

        if mark == 'good':
            pass
        else:
            pass

    def start_button_func(self):
        '''This method is bound to the "Начать" button.
         Gets the text from the database and passes it to the test_moment method'''
        some_text = 'lallala'

        self.append_widget(self.test_moment(some_text))

    def test_moment(self, some_text):
        '''Returns a good/bad result which is then displayed on the screen.
         Tracks keyboard input, counts time, errors and typing speed'''

        pass

    def initUI(self):
        '''This main func in class App. This method is the binder of all other methods.
        Returns nothing'''

        self.load_interface()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())
