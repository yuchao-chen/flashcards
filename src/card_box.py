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
    def cards(self, cards0):
        self.instance._cards = cards0
        print(self.instance._cards)
