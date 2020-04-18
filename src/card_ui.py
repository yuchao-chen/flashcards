import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from src.helper import load_word_list
from src.card_box import CardBox
from src.card import Card


class CardUI(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        # load word lists from source file and database
        load_word_list()
        # load the UI of flash card
        self.create_word_layout()

        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.draw_card()

    def create_word_layout(self):
        self._word_layout = QtWidgets.QVBoxLayout()
        self._word = QtWidgets.QLabel('Word')
        self._word.setAlignment(QtCore.Qt.AlignCenter)
        font = self._word.font()
        font.setBold(True)
        font.setPointSize(38)
        self._word.setFont(font)
        self._ipa = QtWidgets.QLabel('IPA')
        self._ipa.setAlignment(QtCore.Qt.AlignCenter)
        self._def = QtWidgets.QLabel('DEF')
        self._def.setWordWrap(True)
        self._trans = QtWidgets.QLabel('trans')
        self._trans.setWordWrap(True)
        self._examples = QtWidgets.QLabel('examples')
        self._examples.setWordWrap(True)

        for widget in [self._word, self._ipa, self._def, self._trans, self._examples]:
            self._word_layout.addWidget(widget)

        self.setLayout(self._word_layout)

        self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.setMinimumSize(256, 256)
        self.show_labels()

    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent) -> None:
        if not self._word.isHidden():
            self.show_labels(False, False, True, False, False)
        elif not self._def.isHidden():
            self.show_labels(False, False, False, True, False)
        elif not self._trans.isHidden():
            self.show_labels(False, False, False, False, True)
        else:
            self.show_labels(True, True, False, False, False)
        self.update()
        super(CardUI, self).mouseReleaseEvent(a0)

    def show_labels(self, word=True, ipa=True, defs=False, trans=False, examples=False):
        if word:
            self._word.show()
        else:
            self._word.hide()
        if ipa:
            self._ipa.show()
        else:
            self._ipa.hide()
        if defs:
            self._def.show()
        else:
            self._def.hide()
        if trans:
            self._trans.show()
        else:
            self._trans.hide()
        if examples:
            self._examples.show()
        else:
            self._examples.hide()

    def draw_card(self, reverse=False):
        cardbox = CardBox()
        card = cardbox.draw(reverse)
        if card is None:
            return

        self._word.setText(card.word)
        #self._ipa.setText('| ' + card.ipa.replace(';', ' | | ') + ' |')
        self._ipa.setText(card.ipa)
        self._def.setText(card.definition.replace(';', '.\n'))
        self._trans.setText(card.translation)
        self.update()

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        if a0.key() in [QtCore.Qt.Key_Left, QtCore.Qt.Key_Up]:
            self.draw_card(reverse=True)
        elif a0.key() in [QtCore.Qt.Key_Right, QtCore.Qt.Key_Down]:
            self.draw_card()
        else:
            super().keyPressEvent(a0)


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
