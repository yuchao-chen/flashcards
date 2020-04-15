def scrape():
    import requests
    from lxml import html

    page = requests.get('https://dictionary.cambridge.org/dictionary/english-chinese-traditional/jeopardy')
    tree = html.fromstring(page.content)
    print(tree.xpath('//span[@class="trans dtrans dtrans-se "]/text()'))
    #print(tree.xpath('//span[@class="eg deg"]/text()'))
    examples = tree.xpath('//span[@class="eg deg"]')
    sss = []
    for e in examples:
        sss.append(e.text_content())
    print(sss)

if __name__ == '__main__':
    scrape()