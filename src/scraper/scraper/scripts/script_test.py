from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from pathlib import Path
import json
import sys
import os
from scrapy.crawler import CrawlerProcess
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scraper.items import item_loader, ProductItem
import logging

options = Options()
options.add_argument("-profile")
options.add_argument("/home/abdessamadz/snap/firefox/common/.mozilla/firefox/g3l9pxya.bot_user")


class Provider():
    def __init__ (self, settings):
        #define algo-spec attributes
        self.webdriver = webdriver.Firefox(options=options)
        self.name = settings['name']
        self.url = settings['url']
        self.selectors  = settings['selectors']
    
    def search_for_args(self, args):
        self.webdriver.get(self.url)
        elm = self.webdriver.find_element(By.CSS_SELECTOR,self.selectors['search_box_selc'])
        elm.send_keys(args)
        btn = self.webdriver.find_element(By.CSS_SELECTOR,self.selectors['search_btn_selc'])
        btn.click()
        # self.webdriver.context()
        return self.webdriver.current_url
    def some_otherthings(self):
        pass

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
        urls = [self.provider.search_for_args(self.search_params['keyword'])]
        for url in urls: 
            print(url)
            yield scrapy.Request(f"{url}", self.parse)
    def parse(self, response):
        data = response.css(self.provider.selectors['product_link_selc']).getall()
        for url in data:
            yield scrapy.Request(url, self.parse_product_page)
    def parse_product_page(self, response):
        yield item_loader(ProductItem,response, self.provider.selectors)

def main():
    provider = Provider({"name": "Ebay","url": "https://www.ebay.com/","selectors":  {"search_box_selc": "input#gh-ac","search_btn_selc": "input#gh-btn","product_card_selc": "li.s-item.s-item__pl-on-bottom.s-item--watch-at-corner","product_link_selc": "div.s-item__info.clearfix>a.s-item__link::attr(href)","product_title_selc": "h1.x-item-title__mainTitle>span.ux-textspans.ux-textspans--BOLD::text","product_price_selc": "span#prcIsum"}})
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    process.crawl(GenSpider, search_params = {"keyword":sys.argv[1], "limit": 10}, provider_obj = provider)
    process.start()   

if __name__=='__main__':
    main()
