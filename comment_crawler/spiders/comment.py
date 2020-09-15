from scrapy import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from comment_crawler.items import CommentCrawlerItem
from scrapy_splash import SplashRequest
import logging
from comment_crawler.spiders.lua_script import click_script, scroll_script

class CommentCrawlerSpider(CrawlSpider):
    name = 'comment_crawler'
    allowed_domains = ['foody.vn']
    start_urls = []

    def __init__(self, *a, **kw):
        super(CommentCrawlerSpider, self).__init__(*a, **kw)
        with open('comment_crawler/data/start_urls.txt') as f:
            for line in f.readlines():
                self.start_urls.append(line.strip())
    
    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse_foodshop, endpoint='execute',
                args={'lua_source': click_script, 'num_clicks': 15, 'click_delay': 1, 
                'is_crawling_comment': "ask", 'wait': 3})
    
    def parse_foodshop(self, response):
        urls = response.xpath('//div[@class="ldc-item-img"]/a/@href').extract()
        for url in urls:
            full_url = response.urljoin(url)
            yield Request(full_url, callback=self.parse_lua, dont_filter=True)
    
    def parse_lua(self, response):
        yield SplashRequest(response.url, self.parse_item, endpoint='execute', 
            args={'lua_source': scroll_script, 'num_scrolls': 15, 'scroll_delay': 1, 'wait': 5})

    def parse_item(self, response):
        items = response.xpath('//ul[@class="review-list fd-clearbox ng-scope"]/li')
        for sel in items:
            item = CommentCrawlerItem()
            item['title'] = sel.xpath('.//a[@ng-if="Model.Title"]/text()').extract_first() 
            item['rating'] = sel.xpath('.//div[@ng-mouseenter="ReviewRatingPopup()"]/span/text()').extract_first()
            item['comment'] = sel.xpath('.//div[@ng-class="{\'toggle-height\':DesMore}"]/span/text()').extract_first()
            yield item