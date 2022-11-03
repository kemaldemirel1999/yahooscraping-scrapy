import scrapy

from ..items import YahooscrapingItem

class MostactiveSpider(scrapy.Spider):
    name = 'mostactive'
    
    #allowed_domains = ['finance.yahoo.com']
    #start_urls = ['http://finance.yahoo.com/']

    def start_requests(self):
        urls = ['https://finance.yahoo.com/quote/MSFT?p=MSFT']
        urls.append('https://finance.yahoo.com/quote/MSFT?p=MSFT')
        urls.append('https://finance.yahoo.com/quote/AAPL?p=AAPL')
        urls.append('https://finance.yahoo.com/quote/AMZN?p=AMZN')
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        items = YahooscrapingItem()
        
        items['stock_name'] = response.xpath('//*[@id="quote-header-info"]/div[2]/div[1]/div[1]/h1').css('::text').extract()
        items['intraday_price'] = response.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/span[1]').css('::text').extract()
        items['price_change'] = response.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/span[2]').css('::text').extract()
        items['market_cap'] = response.xpath('//*[@id="quote-summary"]/div[2]/table/tbody/tr[1]/td[2]').css('::text').extract()
        items['volume'] = response.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[7]/td[2]/fin-streamer').css('::text').extract()
        
        
        
        yield items
        
