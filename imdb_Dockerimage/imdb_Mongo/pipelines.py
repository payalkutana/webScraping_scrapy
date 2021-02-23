# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo

class ImdbMongoPipeline:

    def __init__(self):
        self.conn = pymongo.MongoClient(
            'ec2-107-20-75-255.compute-1.amazonaws.com',
            27017,
            username='root',
            password='password'

        )
        db = self.conn['imdb_db']
        self.collection = db['Indian_movies']

    def process_item(self, item, spider):
        
        self.collection.insert(dict(item))
        return item
