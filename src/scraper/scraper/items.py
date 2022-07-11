# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from itemloaders.processors import TakeFirst, MapCompose, Join
from  scrapy.item import Item, Field
from scrapy.loader import ItemLoader
from w3lib.html import remove_tags


class ProductItem(Item):
    # define the fields for your item here like:
    title = Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    price = Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    link = Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())



def item_loader(Item, response, selectors):
    l = ItemLoader(item = Item(), response = response)
    l.add_css('title', selectors['product_title_selc'])
    l.add_css('price', selectors['product_price_selc'])
    l.add_value('link', response.url)
    return l.load_item()


