from .recorder import Recorder


class CircularList:

    def __init__(self):
        self._buf = []
        self._count = 0

    @property
    def next(self):
        if self._buf is None:
            return None
        self._count = (self._count + 1) % len(self._buf)
        return self._buf[self._count]

    @property
    def prev(self):
        if self._buf is None:
            return None
        if self._count == 0:
            self._count = len(self._buf) - 1
        else:
            self._count -= 1
        return self._buf[self._count]

    def append(self, o):
        self._buf.append(o)

    def pop(self):
        self.pop()


class CardBox:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(CardBox, cls).__new__(cls)
            cls.instance._cards = {}
            cls.instance._keys = CircularList()
        return cls.instance

    @property
    def cards(self):
        return self.instance._cards

    @cards.setter
    def cards(self, cards0):
        self.instance._cards = cards0
        for key in cards0:
            self.instance._keys.append(key)

    def draw(self, reverse=False):
        key = None
        if reverse:
            key = self.instance._keys.prev
        else:
            key = self.instance._keys.next

        if key is not None:
            return self.instance._cards[key]
        return None
