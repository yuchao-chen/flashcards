import requests
from lxml import html


class Dictionary:
    pass


class Cambridge(Dictionary):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Cambridge, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.base_url = 'https://dictionary.cambridge.org/dictionary/english-chinese-traditional/'

    def lookup(self, word):
        page = requests.get(self.base_url + word.lower())
        tree = html.fromstring(page.content)

        pronunciation = tree.xpath('//span[@class="ipa dipa lpr-2 lpl-1"]/text()')

        definition_contents = tree.xpath('//div[@class="def ddef_d db"]')
        definition = []
        for content in definition_contents:
            definition.append(content.text_content())

        translated_text = tree.xpath('//span[@class="trans dtrans dtrans-se "]/text()')

        examples = []
        example_contents = tree.xpath('//span[@class="eg deg"]')
        for content in example_contents:
            examples.append(content.text_content())

        translated_examples = tree.xpath('//span[@class="trans dtrans dtrans-se hdb"]/text()')
        return ';'.join(pronunciation), ';'.join(definition), ';'.join(translated_text), zip(examples, translated_examples)
