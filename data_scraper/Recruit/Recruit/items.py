# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item
from scrapy.item import Field


class RecruitItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    collection = 'info'
    jobid = Field()
    position = Field()
    corp = Field()
    place = Field()
    salary = Field()
    time = Field()
    pos_info = Field()
    corp_info = Field()
    detail_page = Field()


class DetailItem(Item):
    collection = 'info'
    jobid = Field()
    pos_info = Field()
    corp_info = Field()
