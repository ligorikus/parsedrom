# -*- coding: utf-8 -*-
import scrapy


class DromSpider(scrapy.Spider):
    name = 'drom'
    allowed_domains = ['drom.ru']
    start_urls = ['http://drom.ru/']

    def parse(self, response):
        pass
