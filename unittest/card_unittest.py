import unittest
from src.card import Card


class CardBoxTestCase(unittest.TestCase):

    def test_create_card(self):
        book = 'the golden bough'
        with open('../data/source/the golden bough.txt', 'r') as reader:
            for line in reader.readlines():
                text = line.strip('\n')
                card = Card()
                card.book = book
                card.word = text.lower()


if __name__ == '__main__':
    unittest.main()
