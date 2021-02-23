from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from imdb_Mongo.spiders.imdb_spider_mongo import ImdbSpider
 
 
process = CrawlerProcess(get_project_settings())
process.crawl(ImdbSpider)
process.start()