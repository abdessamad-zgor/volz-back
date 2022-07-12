import scrapy
from scrapy.spiders import CrawlSpider
from scraper.items import item_loader, ProductItem
import logging


#error _ handeling


class GenSpider(CrawlSpider):
    name = 'crawl spiders'
    def __init__(self, search_params, provider_obj, *args, **kwargs):
        logger = logging.getLogger('scrapy.spidermiddlewares.httperror')
        logger.setLevel(logging.INFO)
        super(GenSpider, self).__init__(*args, **kwargs)

        self.provider = provider_obj
        self.limit = search_params['limit']
        self.search_params = search_params
    def start_requests(self):
        url = self.provider.search_for_args(self.search_params['keyword'])
        yield scrapy.Request(url, self.parse)
    def parse(self, response):
        data = response.css(self.provider.selectors['product_link_selc']).getall()
        for url in data:
            yield scrapy.Request(url, self.parse_product_page)
    def parse_product_page(self, response):
        yield item_loader(ProductItem,response, self.provider.selectors)

