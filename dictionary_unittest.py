import unittest
import dictionary
from google.cloud import translate_v2 as translate
from google.oauth2 import service_account


class DictionaryTestCase(unittest.TestCase):

    def test_google_translate_api(self):
        credentials = service_account.Credentials.from_service_account_file(
            '/Users/yuchaochen/Workspace/src/python/google/flashcards-0042788ac8d4.json'
        )
        translate_client = translate.Client(credentials=credentials)
        text = 'pious'
        result = translate_client.translate(
            text, target_language="zh-CN"
        )
        print(u"Text: {}".format(result['input']))
        print(u'Translation: {}'.format(result['translatedText']))

    def test_web_scraper(self):
        import requests
        from lxml import html
        page = requests.get('https://dictionary.cambridge.org/dictionary/english-chinese-traditional/jeopardy')
        tree = html.fromstring(page.content)
        print(tree)
if __name__ == '__main__':
    unittest.main()
