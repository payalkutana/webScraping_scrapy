# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImdbMysqlItem(scrapy.Item):
    # define the fields for your item here like:
    movie_title = scrapy.Field()
    release_year = scrapy.Field()
    
    
