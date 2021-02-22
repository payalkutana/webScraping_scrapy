import scrapy
from ..items import WikipediaWebsItem

class WikiSpider(scrapy.Spider):
    name='wiki'
    start_urls=[
        'https://en.wikipedia.org/wiki/Tesla%2C_Inc',
        'https://en.wikipedia.org/wiki/Apple_Inc.',        
        'https://en.wikipedia.org/wiki/BMW',
        'https://en.wikipedia.org/wiki/Google',
        'https://en.wikipedia.org/wiki/Oracle_Corporation'

    ]

    def parse(self,response):
        
        company_details = WikipediaWebsItem()

        name = response.css('.org').css('::text').extract()
        types = response.css('.category > a').css('::text').extract() 
        founded = response.css('tr:nth-child(8) td , #mf-section-0 .noprint').css('::text').extract_first()
        founded += response.css('tr:nth-child(8) td , #mf-section-0 .noprint').css('::text')[1].extract()
        #founded = response.xpath('//tr[(((count(preceding-sibling::*) + 1) = 8) and parent::*)]//td | //*[contains(concat( " ", @class, " " ), concat( " ", "noprint", " " ))]').extract()
        founders = response.css('.agent li > a:nth-child(1)').css('::text').extract()

        company_details['name'] = name
        company_details['types'] = types
        company_details['founded'] = founded
        company_details['founders'] = founders

        yield company_details
