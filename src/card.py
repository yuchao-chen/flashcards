from .recorder import Recorder
from .dictionary import Cambridge


class Card:

    def __init__(self):
        self._word = ''
        self._card_id = ''
        self._ipa = ''
        self._def = ''
        self._trans = ''
        self._examples = []
        self._book_id = None

    @property
    def book(self):
        return self._book_id

    @book.setter
    def book(self, bookname):
        record = Recorder()
        # if the book name is found
        if record.check_exists_in_record('book', 'name', bookname):
            self._book_id = record.query_book_id(bookname)
        else:
            self._book_id = record.save_book(bookname)

    @property
    def word(self):
        return self._word

    @word.setter
    def word(self, wordname):
        record = Recorder()
        # check if word exists in recordings
        if record.check_exists_in_record('card', 'word', wordname):
            self._word = wordname
            self._card_id = record.query_card_id(wordname)
        else:
            # if not found in the record, lookup the dictionary
            self._word = wordname
            dictionary = Cambridge()
            self._ipa, self._def, self._trans, self._examples = dictionary.lookup(self._word)
            # store the data in the record
            self._card_id = record.save_card(self._word, self._book_id, self._ipa, self._def, self._trans)
            record.save_examples(self._examples, self._card_id)


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
