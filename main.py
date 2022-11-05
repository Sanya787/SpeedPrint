"""Launching the main program window."""

import random
import sys
import sqlite3
import time

from extra import Window
from PyQt5 import uic
from PyQt5.Qt import Qt
from PyQt5.QtMultimedia import QSound
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel,
    QTextBrowser, QRadioButton, QProgressBar, QColorDialog
)

LIST_WITH_ID = [
    16777216, 16777252, 167, 16777248, 16777250,
    16777251, 16777249, 6777220, 16777219, 16777248
]

LIST_WITH_TEXTS = [
    'label_5', 'label_left', 'label_centre',
    'label_right', 'label_nonename', 'label_mizinec',
    'label_12', 'label_8', 'label_9', 'label_7', 'label_11',
    'label_10',
]

LIST_WITH_RADIO = [
    'radioButton',
    'radioButton_2',
    'radioButton_3'
]

BUTTON_TEXT = [
    'pushButton_65',
    'pushButton_66',
    'pushButton_67',
    'pushButton_62'
]


def get_text(hard=1):
    """Generate text.

    Args:
        - input - Text complexity(1-3)

    Returns:
        - output - Text of a given complexity
    """
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
    """Control the application.

    Args:
        - input - Nothing

    Returns:
        - output - Nothing
    """

    def __init__(self):
        """Call the main function. Defines basic variables.

        Args:
            - input - Nothing

        Returns:
            - output - Nothing
        """
        super().__init__()
        self.load_interface()

        self.flag = False
        sound = 'sounds/myagkoe-spokoynoe-najatie-klavishi.wav'
        self.sound = QSound(sound, self)
        self.error = QSound('sounds/__raclure__wrong.wav', self)

    def keyPressEvent(self, event):
        """Works with pressed keys.

        Args:
            - input - The key that was pressed

        Returns:
            - output - Nothing
        """
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
        """Linked to on/off button.

        Args:
            - input - Nothing

        Returns:
            - output - Nothing
        """
        self.value_on = not self.value_on
        if self.value_on:
            self.value.setIcon(QIcon('images/pngwing.com.png'))
        else:
            self.value.setIcon(QIcon('images/pngwing.png'))

    def size_func(self):
        """Bound to a text resize button.

        Args:
            - input - Nothing

        Returns:
            - output - Nothing
        """
        self.size_on = not self.size_on
        if not self.size_on:
            self.size.setIcon(QIcon('images/Aa.png'))
            self.input.setFont(QFont('.SF NS Text', 15))
            self.browser.setFont(QFont('.SF NS Text', 15))
        else:
            self.size.setIcon(QIcon('images/Aa_big.png'))
            self.input.setFont(QFont('.SF NS Text', 20))
            self.browser.setFont(QFont('.SF NS Text', 20))

    def change_color_bg(self):
        """Change the background color selected by the user.

        Args:
            - input - Nothing

        Returns:
            - output - Nothing
        """
        color = QColorDialog.getColor()
        if color.isValid():
            self.setStyleSheet(f"background-color: {color.name()}")

    def change_color_extra(self):
        """Change the secondary color that the user has selected.

        Args:
            - input - Nothing

        Returns:
            - output - Nothing
        """
        color = QColorDialog.getColor()
        if color.isValid():
            for elem in BUTTON_TEXT:
                style_button = ''
                copy = self.findChild(QPushButton, elem)
                for elemenet in copy.styleSheet().split('\n'):
                    if 'background-color' in elemenet:
                        color_paste = f'{color.name()};'
                        style_button += f'    background-color: {color_paste}\n'
                    else:
                        style_button += f'{elemenet}\n'
                    copy.setStyleSheet(style_button)
            style_bar = f'{self.bar.styleSheet()[:-22]}{color.name()} \n {"}"}'
            self.bar.setStyleSheet(style_bar)

    def change_color_text(self):
        """Change the text color that the user has selected.

        Args:
            - input - Nothing

        Returns:
            - output - Nothing
        """
        color = QColorDialog.getColor()
        if color.isValid():
            for elem in LIST_WITH_TEXTS:
                copy = self.findChild(QLabel, elem)
                copy.setStyleSheet(f"color: {color.name()}")

            for elem in LIST_WITH_RADIO:
                copy = self.findChild(QRadioButton, elem)
                copy.setStyleSheet(f"color: {color.name()}")

            for elem in BUTTON_TEXT:
                style_button = ''
                copy = self.findChild(QPushButton, elem)
                for elemenet in copy.styleSheet().split('\n'):
                    if 'color:' in elemenet and 'back' not in elemenet:
                        style_button += f'     color: {color.name()};\n'
                    else:
                        style_button += f'{elemenet}\n'
                    copy.setStyleSheet(style_button)

            style_bar = ''
            for elem in self.bar.styleSheet().split('\n'):
                if 'color:' in elem and 'back' not in elem:
                    style_bar += f'     color: {color.name()}\n'
                else:
                    style_bar += f"{elem}\n"
            self.bar.setStyleSheet(style_bar)

    def load_interface(self):
        """Get main widget objects and connect the functions to the buttons.

        Args:
            - input - Nothing

        Returns:
            - output - Nothing
        """
        uic.loadUi('project.ui', self)

        self.mark = 0
        self.index = 0
        self.value_on = True
        self.size_on = True

        self.button_start = self.findChild(QPushButton, 'pushButton_62')
        self.value = self.findChild(QPushButton, 'pushButton_63')
        self.size = self.findChild(QPushButton, 'pushButton_64')
        self.color_backround = self.findChild(QPushButton, 'pushButton_65')
        self.extra_color = self.findChild(QPushButton, 'pushButton_66')
        self.text_color = self.findChild(QPushButton, 'pushButton_67')
        self.timer = self.findChild(QLabel, 'label_10')
        self.speed = self.findChild(QLabel, 'label_8')
        self.marks = self.findChild(QLabel, 'label_12')

        self.form = self.findChild(QWidget, 'Form')
        self.bar = self.findChild(QProgressBar, 'progressBar')
        self.input = self.findChild(QTextBrowser, 'textBrowser_2')
        self.browser = self.findChild(QTextBrowser, 'textBrowser')
        self.radio_button_1 = self.findChild(QRadioButton, 'radioButton')
        self.radio_button_2 = self.findChild(QRadioButton, 'radioButton_2')
        self.radio_button_3 = self.findChild(QRadioButton, 'radioButton_3')

        self.size.clicked.connect(self.size_func)
        self.color_backround.clicked.connect(self.change_color_bg)
        self.extra_color.clicked.connect(self.change_color_extra)
        self.text_color.clicked.connect(self.change_color_text)
        self.value.clicked.connect(self.value_func)
        self.button_start.clicked.connect(self.start_button_func)

    def start_button_func(self):
        """Attached to start button.

        Args:
            - input - Nothing

        Returns:
            - output - Nothing
        """
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app2 = QApplication(sys.argv)

    window = App()
    window.show()

    window2 = Window()
    window2.show()

    sys.exit(app2.exec())
    sys.exit(app.exec())
