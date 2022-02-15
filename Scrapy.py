import scrapy
class NewSpider(scrapy.Spider):
 name = "new_spider"
 start_urls = ['http://192.168.1.1/sets/1']
