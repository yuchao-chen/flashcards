import sqlite3


class Recorder:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Recorder, cls).__new__(cls)
            cls.instance.conn = None
            cls.instance.cursor = None
            cls.instance.connect('data/cardbox')
            cls.instance.create_record_tables()
        return cls.instance

    def connect(self, dbname):
        try:
            if self.instance.conn:
                self.instance.conn.close()
            self.instance.conn = sqlite3.connect(dbname)
            self.instance.cursor = self.instance.conn.cursor()
            print(sqlite3.version)
        except sqlite3.Error as e:
            raise Exception('SQLITE FAIL TO CONNECT ' + dbname + '{}'.format(e))

    def create_record_tables(self):
        book_sql = '''
            CREATE TABLE IF NOT EXISTS book (
                _id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            );
        '''
        card_sql = '''
            CREATE TABLE IF NOT EXISTS card (
                _id INTEGER PRIMARY KEY AUTOINCREMENT,
                book_id INTEGER,
                word TEXT NOT NULL UNIQUE,
                ipa TEXT,
                def TEXT,
                trans TEXT,
                FOREIGN KEY (book_id) REFERENCES book(_id)
            );
        '''
        example_sql = '''
            CREATE TABLE IF NOT EXISTS example (
                _id INTEGER PRIMARY KEY AUTOINCREMENT,
                card_id INTEGER,
                sentence TEXT NOT NULL,
                trans TEXT,
                FOREIGN KEY (card_id) REFERENCES card (_id)
                    ON DELETE CASCADE 
                    ON UPDATE NO ACTION 
            );
        '''
        self.create_table(book_sql)
        self.create_table(card_sql)
        self.create_table(example_sql)

    def create_table(self, sql):
        try:
            self.instance.cursor.execute(sql)
            self.instance.conn.commit()
        except sqlite3.Error as e:
            raise Exception('SQLITE FAIL TO CREATE TABLES {}'.format(e))

    def check_exists_in_record(self, table, param, value):
        ck_sql = '''
            SELECT EXISTS (SELECT 1 FROM {} WHERE {} = "{}" LIMIT 1);
        '''.format(table, param, value)
        result = self.instance.query_one(ck_sql)
        if result is not None and result[0] == 1:
            return True
        return False

    def save_book(self, bookname):
        insert_sql = '''
            INSERT INTO book (name) VALUES ("{}");
        '''.format(bookname)
        return self.instance.execute(insert_sql)

    def query_book_id(self, bookname):
        sql = '''
            SELECT _id FROM book WHERE name = "{}" LIMIT 1;
        '''.format(bookname)
        result = self.query_one(sql)
        if result is not None:
            return result[0]
        return None

    def save_card(self, word, book_id, ipa, defs, trans):
        card_sql = '''
            INSERT INTO card (word, book_id, ipa, def, trans) VALUES ("{}", "{}", "{}", "{}", "{}");
        '''.format(word, book_id, ipa, defs, trans)
        return self.instance.execute(card_sql)

    def query_card_id(self, wordname):
        sql = '''
            SELECT _id FROM card WHERE word = "{}" LIMIT 1;
        '''.format(wordname)
        result = self.query_one(sql)
        if result is not None:
            return result[0]
        return None

    def save_examples(self, examples, card_id):
        example_sql = '''
            INSERT INTO example (card_id, sentence, trans) VALUES ({}, ?, ?);
        '''.format(card_id)
        try:
            self.instance.cursor.executemany(example_sql, examples)
            self.instance.conn.commit()
        except sqlite3.Error as e:
            raise Exception('Fail to save examples: ' + example_sql + '{}'.format(e))

    def query_one(self, sql):
        try:
            self.instance.cursor.execute(sql)
            return self.instance.cursor.fetchone()
        except sqlite3.Error as e:
            raise Exception('Fail to query: ' + sql + '{}'.format(e))

    def execute(self, sql):
        try:
            self.instance.cursor.execute(sql)
            self.instance.conn.commit()
            return self.instance.cursor.lastrowid
        except sqlite3.Error as e:
            raise Exception('Fail to execute: ' + sql + '{}'.format(e))