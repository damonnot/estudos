import scrapy


class ImbdSpider(scrapy.Spider):
    name = 'imbd'
    start_urls = ['http://imbd.com/']

    def parse(self, response):
        pass
