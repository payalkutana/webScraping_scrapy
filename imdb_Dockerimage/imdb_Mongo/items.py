# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImdbMongoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movie_imglink = scrapy.Field()
    release_year = scrapy.Field()
    movie_title = scrapy.Field()
    rating = scrapy.Field()
    
