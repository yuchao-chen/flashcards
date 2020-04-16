from .recorder import Recorder
from .card import Card


class CardBox:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(CardBox, cls).__new__(cls)
            recorder = Recorder()
            cls.instance._cards = {}
        return cls.instance

    @property
    def cards(self):
        return self.instance._cards

    @cards.setter
    def cards(self, words_list):
        for key in words_list:
            book = key
            for word in words_list[key]:
                new_card = Card()
                new_card.book = book
                new_card.word = word
                self.instance._cards[new_card.word] = new_card
