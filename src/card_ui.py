import sys
from PyQt5 import QtWidgets
from src.helper import load_word_list
from src.card_box import CardBox
from src.card import Card


class CardUI(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        # load word lists from source file and database
        load_word_list()
        # load the UI of flash card
        self.create_ui()
        self.load_test_card()

    def create_ui(self):
        layout = QtWidgets.QVBoxLayout()
        self._word = QtWidgets.QLabel('Word')
        self._ipa = QtWidgets.QLabel('IPA')
        self._def = QtWidgets.QLabel('DEF')
        self._trans = QtWidgets.QLabel('trans')

        for widget in [self._word, self._ipa, self._def, self._trans]:
            layout.addWidget(widget)
        self.setLayout(layout)

    def load_test_card(self):
        cardbox = CardBox()
        card = cardbox.draw()
        self._word.setText(card.word)
        self._ipa.setText(card.ipa)
        self._def.setText(card.definition)
        self._trans.setText(card.translation)
        pass


class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = CardUI()
        self.setCentralWidget(self.ui)


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName('Flash Cards')
    window = Window()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
