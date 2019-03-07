# -*- coding: utf-8 -*-
import json

import scrapy

from Recruit.items import RecruitItem


class Beijing51Spider(scrapy.Spider):
    name = 'beijing51'
    allowed_domains = ['search.51job.com']
    start_urls = ['http://search.51job.com/']

    arg = 'list/000000%252C00,000000,0000,00,9,12,%2B,2,{page}.html'
    url = start_urls[0] + arg

    def start_requests(self):

    def parse(self, response):
        jobs = response.css('.el')
        for job in jobs:
            position = job.css(".t1 span a:attr('title')").extract_first()
