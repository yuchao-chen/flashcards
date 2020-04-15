import unittest
from src.card_box import CardBox


class CardBoxTestCase(unittest.TestCase):

    def test_db_create(self):
        cardbox = CardBox()
        cardbox.create_tables()


if __name__ == '__main__':
    unittest.main()
