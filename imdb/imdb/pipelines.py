# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3
from itemadapter import ItemAdapter

class ImdbPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect('imdb.db')
        self.curr = self.conn.cursor()


    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS indian_movies""")

        self.curr.execute("""create table indian_movies(
                movie_title text,
                movie_imglink text,
                release_year text,
                rating text
                )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self,item):

        for i in range(len(item['rating'])):
            self.curr.execute("""insert into indian_movies values(?,?,?,?)""",(
                    item['movie_title'][i],
                    item['movie_imglink'][i],
                    item['release_year'][i],
                    item['rating'][i]
            ))
            self.conn.commit()