# -*- coding: utf-8 -*-
import json
import re
import time

import scrapy

from Recruit.items import DetailItem, RecruitItem


class Beijing51Spider(scrapy.Spider):
    name = 'beijing51'
    allowed_domains = ['search.51job.com']
    start_urls = ['https://search.51job.com/']

    arg = 'list/000000,000000,0000,00,9,99,%2B,2,2.html'
    jobid = 0

    def start_requests(self):
        yield scrapy.Request(self.start_urls[0] + self.arg, callback=self.parse_job)

    def parse_job(self, response):
        jobs = response.css('#resultList .el')[2:]

        for job in jobs:
            item = RecruitItem()
            item['jobid'] = job.css(
                ".t1 .checkbox::attr('value')").extract_first()
            item['position'] = job.css(
                ".t1 span a::attr('title')").extract_first()
            item['corp'] = job.css(
                ".t2 a::attr('title')").extract_first()
            item['place'] = job.css(
                ".t3::text").extract_first()
            item['salary'] = job.css(
                ".t4::text").extract_first()
            item['time'] = job.css(
                ".t5::text").extract_first()
            # item['pos_info'] = []
            # item['corp_info'] = []
            detail_page = job.css(".t1 span a::attr(href)").extract_first()
            item['detail_page'] = detail_page

            yield scrapy.Request(detail_page, callback=self.parse_details, dont_filter=True)
            yield item

        # detail_pages = response.css('.t1 span a::attr(href)').extract()
        # for detail_page in detail_pages:
        #     yield scrapy.Request(detail_page, callback=self.parse_details, dont_filter=True)

        next_page = response.css(
            '.dw_page .p_box .p_wp .p_in ul .bk a::attr(href)').extract()[1]
        print('下一页是： %s' % next_page)
        yield scrapy.Request(next_page, callback=self.parse_job)
        time.sleep(2.0)

    def parse_details(self, response):
        item = DetailItem()
        item['jobid'] = re.search(
            'com/(.*?)/(.*?).html', response.url, re.S).group(2)
        item['pos_info'] = [response.css(
            '.bmsg.job_msg.inbox').extract_first()]
        item['corp_info'] = [response.css(
            '.tmsg.inbox').extract_first()]
        yield item
