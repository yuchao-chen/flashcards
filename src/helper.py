from os import listdir
from os.path import isfile, join, splitext

#from google.cloud import translate_v2 as translate
#from google.oauth2 import service_account

from src.card_box import CardBox
from src.card import Card


def load_word_list():
    srcdir = '../data/source'
    files = [f for f in listdir(srcdir) if isfile(join(srcdir, f))]
    cards = {}
    for file in files:
        bookname = splitext(file)[0]
        with open(join(srcdir, file), 'r') as reader:
            for line in reader.readlines():
                text = line.strip('\n')
                card = Card()
                card.book = bookname
                card.word = text.lower()
                cards[card.word] = card
    cardbox = CardBox()
    cardbox.cards = cards


#def load_words_from_txt_google_translate():
#    credentials = service_account.Credentials.from_service_account_file(
#        '/Users/yuchaochen/Workspace/src/python/google/flashcards-0042788ac8d4.json'
#    )
#    translate_client = translate.Client(credentials=credentials)
#
#    with open('../words/source/the golden bough.txt', 'r') as reader, open('words/cards/the golden bough.csv', 'w') as writer:
#        for line in reader.readlines():
#            text = line.strip('\n')
#            result = translate_client.translate(
#                text, target_language="zh-CN"
#            )
#            output = '{}'.format(result['input'].lower())
#            output += ',{}'.format(result['translatedText'])
#            writer.write(output + '\n')


if __name__ == '__main__':
    load_word_list()
