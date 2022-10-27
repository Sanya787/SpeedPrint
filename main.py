import sys
import time
import random
import sqlite3

from extra import Window
from PyQt5 import uic
from PyQt5.Qt import Qt
from PyQt5.QtMultimedia import QSound
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel,
    QTextBrowser, QRadioButton, QProgressBar
)

LIST_WITH_ID = [
    16777216, 16777252, 167, 16777248, 16777250,
    16777251, 16777249, 6777220, 16777219, 16777248
]


def get_text(hard=1):
    hard_dictionary = {
        1: '< 30',
        2: '> 30 AND hard < 60',
        3: '> 60',
    }
    connection = sqlite3.connect('base_texts.db')
    cursor = connection.cursor()

    query = f'''
    SELECT text FROM texts
    WHERE hard {hard_dictionary[hard]}'''

    cursor.execute(query)
    connection.commit()
    answer = random.choice(cursor.fetchall())[0]
    connection.close()
    return answer


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        self.flag = False
        sound = 'sounds/myagkoe-spokoynoe-najatie-klavishi.wav'
        self.sound = QSound(sound, self)
        self.error = QSound('sounds/__raclure__wrong.wav', self)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            print('d')
        if self.flag:
            time_now = time.time() - self.time_start
            minute = f'{round(time_now // 60):02}'
            second = f'{round(time_now % 60):02}'

            self.timer.setText(f'{minute}:{second}')
            if time_now < 1:
                time_now = 1
            speed = (self.index / round(time_now)) * 60
            self.speed.setText(str(round(speed)))
            if len(self.input.toPlainText()) != 0:
                value = len(self.input.toPlainText()) / len(self.text) * 100
                self.bar.setValue(round(value))

            if self.text[self.index] == event.text() != ' ':
                self.input.setText(self.input.toPlainText() + event.text())
                if self.value_on:
                    self.sound.play()
                if not self.index + 1 == len(self.text):
                    self.index += 1
                else:
                    self.flag = False
                if self.text[self.index] == ' ':
                    self.input.setText(self.input.toPlainText() + ' ')
                    if self.value_on:
                        self.sound.play()
                    self.index += 1
            else:
                if event.key() not in LIST_WITH_ID:
                    self.marks.setText(str(self.mark))
                    if self.value_on:
                        self.error.play()
                    self.mark += 1

    def value_func(self):
        self.value_on = not self.value_on
        if self.value_on:
            self.value.setIcon(QIcon('images/pngwing.com.png'))
        else:
            self.value.setIcon(QIcon('images/pngwing.png'))

    def size_func(self):
        self.size_on = not self.size_on
        if not self.size_on:
            self.size.setIcon(QIcon('images/Aa.png'))
            self.input.setFont(QFont('.SF NS Text', 15))
            self.browser.setFont(QFont('.SF NS Text', 15))
        else:
            self.size.setIcon(QIcon('images/Aa_big.png'))
            self.input.setFont(QFont('.SF NS Text', 20))
            self.browser.setFont(QFont('.SF NS Text', 20))

    def load_interface(self):
        uic.loadUi('project.ui', self)

        self.mark = 0
        self.index = 0
        self.value_on = True
        self.size_on = True

        self.button_start = self.findChild(QPushButton, 'pushButton_62')
        self.value = self.findChild(QPushButton, 'pushButton_63')
        self.size = self.findChild(QPushButton, 'pushButton_64')
        self.timer = self.findChild(QLabel, 'label_10')
        self.speed = self.findChild(QLabel, 'label_8')
        self.marks = self.findChild(QLabel, 'label_12')
        self.bar = self.findChild(QProgressBar, 'progressBar')
        self.input = self.findChild(QTextBrowser, 'textBrowser_2')
        self.browser = self.findChild(QTextBrowser, 'textBrowser')
        self.radio_button_1 = self.findChild(QRadioButton, 'radioButton_1')
        self.radio_button_2 = self.findChild(QRadioButton, 'radioButton_2')
        self.radio_button_3 = self.findChild(QRadioButton, 'radioButton_3')

        self.size.clicked.connect(self.size_func)
        self.value.clicked.connect(self.value_func)
        self.button_start.clicked.connect(self.start_button_func)

    def start_button_func(self):
        self.timer.setText('00:00')
        self.speed.setText('0')
        self.bar.setValue(0)
        self.input.setText('')
        self.marks.setText('0')

        self.time_start = time.time()
        self.flag = True
        self.mark = 0
        self.index = 0

        if self.radio_button_3.isChecked():
            self.text = get_text(3)
        elif self.radio_button_2.isChecked():
            self.text = get_text(2)
        else:
            self.text = get_text(1)
        self.browser.setText(self.text)

    def initUI(self):
        self.load_interface()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app2 = QApplication(sys.argv)

    window = App()
    window.show()

    window2 = Window()
    window2.show()

    sys.exit(app2.exec())
    sys.exit(app.exec())
    
