BOT_NAME = 'comment_crawler'

SPIDER_MODULES = ['comment_crawler.spiders']
NEWSPIDER_MODULE = 'comment_crawler.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'comment_crawler (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32
# DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 2

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

#SPIDER_MIDDLEWARES = {
#    'comment_crawler.middlewares.CommentCrawlerSpiderMiddleware': 543,
#}

#DOWNLOADER_MIDDLEWARES = {
#    'comment_crawler.middlewares.CommentCrawlerDownloaderMiddleware': 543,
#}

ITEM_PIPELINES = {
   'comment_crawler.pipelines.CommentCrawlerPipeline': 300,
}

SPLASH_URL = 'http://127.0.0.1:8050'
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
COOKIES_ENABLED = True 
SPLASH_COOKIES_DEBUG = False
SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}
CLOSESPIDER_PAGECOUNT = 50000
DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': 400,
}
DOWNLOAD_TIMEOUT = 300
LOG_LEVEL = "DEBUG"
DUPEFILTER_CLASS = 'scrapy.dupefilters.BaseDupeFilter'