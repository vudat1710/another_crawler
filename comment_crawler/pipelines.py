# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json, codecs


class CommentCrawlerPipeline:
    def __init__(self):
        self.items = []
        self.file = open('comment_crawler/data/comments.json', 'w') # open('items.json', 'w')

    def close_spider(self, spider):
        json.dump(self.items, self.file)
        self.file.close()

    def process_item(self, item, spider):            
        self.items.append(dict(item))
        return item
