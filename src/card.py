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
    def card_id(self):
        return self._card_id

    @card_id.setter
    def card_id(self, id):
        self._card_id = id

    @property
    def ipa(self):
        return self._ipa

    @ipa.setter
    def ipa(self, ipa0):
        self._ipa = ipa0

    @property
    def definition(self):
        return self._def

    @definition.setter
    def definition(self, defs):
        self._def = defs

    @property
    def translation(self):
        return self._trans

    @translation.setter
    def translation(self, trans):
        self._trans = trans

    @property
    def examples(self):
        return self._examples

    @examples.setter
    def examples(self, egs):
        self._examples = egs

    @property
    def word(self):
        return self._word

    @word.setter
    def word(self, wordname):
        self._word = wordname
        record = Recorder()
        # check if word exists in recordings
        if record.check_exists_in_record('card', 'word', wordname):
            self.card_id, self.ipa, self.definition, self.translation = record.query_card(wordname)
            self.examples = record.query_examples(self.card_id)
        else:
            # if not found in the record, lookup the dictionary
            dictionary = Cambridge()
            self.ipa, self.definition, self.translation, self.examples = dictionary.lookup(self._word)
            # store the data in the record
            self.card_id = record.save_card(self.word, self.book_id, self.ipa, self.definition, self.translation)
            record.save_examples(self.examples, self.card_id)

