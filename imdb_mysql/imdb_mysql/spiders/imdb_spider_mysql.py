import scrapy
from ..items import ImdbMysqlItem

class ImdbSpider(scrapy.Spider):
    name='imdb'
    start_urls=[
        'https://www.imdb.com/name/nm0000821/?ref_=fn_nm_nm_1#actor/'
    ]

    def parse(self,response):
        
        movies = ImdbMysqlItem()

        #all_response = response.css('div.filmo-category-section')
        #all_response1 = all_response.css('div.filmo-row odd')
        
        #for row in all_response1:
        movie_title = response.css('b a').css('::text').extract()
        release_year = response.css('.year_column').css('::text').extract()
        

        movies['movie_title'] = movie_title
        movies['release_year'] = release_year
        #print("len:: ",len(release_year))
        #print(release_year)
        #print("len ::" ,len(movies['movie_title']))
        
        
        yield movies