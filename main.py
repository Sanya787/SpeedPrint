import sys
import time

from extra import Window
from PyQt5 import uic
from PyQt5.QtMultimedia import QSound
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QTextBrowser, QRadioButton
)

ignor_list = [
    16777216, 16777252, 167, 16777248, 16777250,
    16777251, 16777249, 6777220, 16777219, 16777248
]

hard_text = [
    'В четверг четвёртого числа в четыре с четвертью часа лигурийский',
    'регулировщик регулировал в Лигурии,',
    'но тридцать три корабля лавировали, лавировали, да так',
    'и не вылавировали. А потом протокол',
    'про протокол протоколом запротоколировал. Как интервьюером',
    'интервьюируемый лигурийский регулировщик речисто,',
    'да не чисто рапортовал, да не дорапортовал дорапортовывал,',
    'да так зарапортовался про размокропогодившуюся',
    'погоду что, дабы инцидент не стал претендентом на судебный',
    'прецедент, лигурийский регулировщик'
]
middle_text = [
    'Человек должен быть интеллигентен! А если у',
    'него профессия не требует интеллигентности?',
    'А если он не смог получить образования: так сложились',
    'обстоятельства? А если интеллигентность сделает',
    'его “белой вороной” среди его сослуживцев, друзей, родных?',
    'Нет, нет и нет! Интеллигентность нужна при всех обстоятельствах.',
    'Она нужна и для окружающих, и для самого человека'
]

easy_text = [
    'Фокус зрения читателя зависит от того, на сколько знаком ему текст.',
    'Чем более незнаком текст, тем фокус зрения уже.',
    'Незнакомое слово будет читаться по буквам.',
    'Чем более знаком текст, тем фокус зрения шире - в этом случае, даже,',
    'нетренированный читатель воспринимает текст как единую картинку.',
    'То есть невозможно, читать любой текст с одинаково широким углом зрения.',
]


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.flag = False
        self.initUI()
        self.sound = QSound('myagkoe-spokoynoe-najatie-klavishi.wav', self)
        self.error = QSound('__raclure__wrong.wav', self)

    def keyPressEvent(self, event):
        if self.flag:
            time_now = time.time() - self.time_start
            second = round(time_now % 60)
            minute = round(time_now // 60)
            if minute == 0:
                minute = '00'
            elif minute < 10:
                minute = '0' + str(minute)
            if second == 0:
                second = '00'
            elif second < 10:
                second = '0' + str(second)
            self.timer.setText(f'{minute}:{second}')
            speed = (self.index / round(time_now)) * 60
            self.speed.setText(str(round(speed)))
            if self.text[self.index] == event.text() != ' ':
                self.input.setText(self.input.toPlainText() + event.text())
                self.sound.play()
                if not self.index + 1 == len(self.text):
                    self.index += 1
                else:
                    self.flag = False
                if self.text[self.index] == ' ':
                    self.sound.play()
                    self.input.setText(self.input.toPlainText() + ' ')
                    self.index += 1
            else:
                if event.key() not in ignor_list:
                    self.mark += 1
                    self.error.play()
                    self.marks.setText(str(self.mark))

    def load_interface(self):
        self.mark = 0
        self.index = 0
        uic.loadUi('project.ui', self)
        self.button_start = self.findChild(QPushButton, 'pushButton_62')
        self.button_start.clicked.connect(self.start_button_func)
        self.timer = self.findChild(QLabel, 'label_10')
        self.speed = self.findChild(QLabel, 'label_8')
        self.marks = self.findChild(QLabel, 'label_12')
        self.input = self.findChild(QTextBrowser, 'textBrowser_2')
        self.browser = self.findChild(QTextBrowser, 'textBrowser')
        self.radio_button_1 = self.findChild(QRadioButton, 'radioButton_1')
        self.radio_button_2 = self.findChild(QRadioButton, 'radioButton_2')
        self.radio_button_3 = self.findChild(QRadioButton, 'radioButton_3')

    def start_button_func(self):
        self.timer.setText('00:00')
        self.time_start = time.time()
        self.mark = 0
        self.index = 0
        self.speed.setText('0')
        self.flag = True
        self.input.setText('')
        self.marks.setText('0')
        if self.radio_button_3.isChecked():
            self.text = ' '.join(hard_text)
        elif self.radio_button_2.isChecked():
            self.text = ' '.join(middle_text)
        else:
            self.text = ' '.join(easy_text)
        self.browser.setText(self.text)

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
