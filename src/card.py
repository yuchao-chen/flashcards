

class Card:

    def __init__(self):
        self.word = ''
        self.pronunciation = ''
        self.translated_text = ''
        self.examples = []

    @property
    def word(self):
        return self.__word

    @word.setter
    def word(self, word):
        self.__word = word

'''

import sys
from PyQt5 import QtWidgets


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    button = QtWidgets.QPushButton("Hello, PyQt!")
    window.setCentralWidget(button)
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
'''
