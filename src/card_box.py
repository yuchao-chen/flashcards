import sqlite3
from .card import Card


class CardBox:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(CardBox, cls).__new__(cls)
            cls.instance.conn = None
            cls.instance.cursor = None
        return cls.instance

    def __init__(self):
        if not self.instance.conn:
            self.connect('../data/cardbox')

    def connect(self, dbname):
        try:
            if self.instance.conn:
                self.instance.conn.close()
            self.instance.conn = sqlite3.connect(dbname)
            self.instance.cursor = self.instance.conn.cursor()
            print(sqlite3.version)
        except sqlite3.Error as e:
            raise Exception('SQLITE FAIL TO CONNECT ' + dbname + '{}'.format(e))

    def create_tables(self):
        try:
            self.instance.cursor.execute('''
                CREATE TABLE IF NOT EXISTS card (
                    _id INTEGER PRIMARY KEY AUTOINCREMENT,
                    word TEXT NOT NULL UNIQUE,
                    translated TEXT
                );
            ''')
            self.instance.conn.commit()
            self.instance.cursor.execute('''
                CREATE TABLE IF NOT EXISTS example (
                    _id INTEGER PRIMARY KEY AUTOINCREMENT,
                    card_id INTEGER,
                    sentence TEXT NOT NULL,
                    translate TEXT,
                    FOREIGN KEY (card_id) REFERENCES card (_id)
                    ON DELETE CASCADE 
                    ON UPDATE NO ACTION 
                );
            ''')
            self.instance.conn.commit()
        except sqlite3.Error as e:
            raise Exception('SQLITE FAIL TO CREATE TABLES {}'.format(e))

    def add_card(self, cards):
        pass