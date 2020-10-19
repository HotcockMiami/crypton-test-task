# -*- coding: utf-8 -*-
import scrapy

from google_scraper.items import GoogleScraperItem

class GoogleSpiderSpider(scrapy.Spider):
    name = 'google_spider'
    start_urls = ['https://www.google.com/search?q=scrapy']

    def parse(self, response):
        item = GoogleScraperItem()
        for i in range(3,15):
            print('---------------------------   ', i)
            item['name'] = response.xpath('//*[@id="main"]/div[{}]/div/div[1]/a/h3/div/text()'.format(i)).get()
            if item['name'] is None:
                continue
            item['url'] = response.xpath('//*[@id="main"]/div[{}]/div/div[1]/a/@href'.format(i)).get()
            item['url'] = item['url'][7:item['url'].find("&")]
            item['desc'] = response.xpath('//*[@id="main"]/div[{}]/div/div[3]/div/div/div/div/div/text()'.format(i)).get()
            yield item
