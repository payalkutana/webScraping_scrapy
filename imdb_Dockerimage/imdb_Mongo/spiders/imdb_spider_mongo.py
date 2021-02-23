import scrapy
from ..items import ImdbMongoItem
class ImdbSpider(scrapy.Spider):
    name='imdb'
    start_urls=[
        'https://www.imdb.com/india/top-rated-indian-movies/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=461131e5-5af0-4e50-bee2-223fad1e00ca&pf_rd_r=RAZY3GF7R4WXSXM4F7JM&pf_rd_s=center-1&pf_rd_t=60601&pf_rd_i=india.toprated&ref_=fea_india_ss_toprated_india_tr_india250_sm'
    ]


    def parse(self,response):
        
        movies = ImdbMongoItem()

        movie_imglink = response.css('img::attr(src)').extract()
        movie_title = response.css('.titleColumn a').css('::text').extract()
        release_year = response.css('span.secondaryInfo').css('::text').extract()
        rating = response.css('strong::text').extract()

        for i in range(len(rating)):
            movies['movie_title'] = movie_title[i]
            movies['movie_imglink'] = movie_imglink[i]
            movies['release_year'] = release_year[i]
            movies['rating'] = rating[i]

            yield movies