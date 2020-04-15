from google.cloud import translate_v2 as translate
from google.oauth2 import service_account

from src.dictionary import Cambridge


def load_words_from_txt_google_translate():
    credentials = service_account.Credentials.from_service_account_file(
        '/Users/yuchaochen/Workspace/src/python/google/flashcards-0042788ac8d4.json'
    )
    translate_client = translate.Client(credentials=credentials)

    with open('../words/source/the golden bough.txt', 'r') as reader, open('words/cards/the golden bough.csv', 'w') as writer:
        for line in reader.readlines():
            text = line.strip('\n')
            result = translate_client.translate(
                text, target_language="zh-CN"
            )
            output = '{}'.format(result['input'].lower())
            output += ',{}'.format(result['translatedText'])
            writer.write(output + '\n')


def load_words_from_txt_web_scraper():

    # load word list from words directory, and write translated text into csv file and database
    with open('../words/source/the golden bough.txt', 'r') as reader, open('words/cards/the golden bough.csv', 'w') as writer:
        dictionary = Cambridge()

        for line in reader.readlines():
            text = line.strip('\n')
            pronunciation, translated_text, examples = dictionary.translate(text)
            output = text.lower() + ',"' + ';'.join(pronunciation) + '","' + ';'.join(translated_text) + '","' + ';'.join(examples) + '"\n'
            writer.write(output)


if __name__ == '__main__':
    load_words_from_txt_web_scraper()