# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class CommentCrawlerItem(Item):
    rating = Field()
    comment = Field()
    title = Field()