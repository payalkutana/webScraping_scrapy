import scrapy
from ..items import QuoteItem

class QuoteSpider(scrapy.Spider):
    name='quotes3'
    start_urls=[
        'http://quotes.toscrape.com/'
    ]

    def parse(self,response):

        items = QuoteItem()

        all_div_quotes = response.css('div.quote')

        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag

            yield items
            

    #Use Following Command to store data in files
    #scrapy crawl quotes3 -o items.json
    #scrapy crawl quotes3 -o items.xml
    #scrapy crawl quotes3 -o items.csv
