# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YahooscrapingItem(scrapy.Item):
    # define the fields for your item here like:
    stock_name = scrapy.Field()
    intraday_price = scrapy.Field()
    price_change = scrapy.Field()
    market_cap = scrapy.Field()
    volume = scrapy.Field()
    
    
    pass
