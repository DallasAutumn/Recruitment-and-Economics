# -*- coding: utf-8 -*-

import re

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

from Recruit.items import DetailItem, RecruitItem


class DetailPipeline(object):
    def wash(self, text):
        return re.sub("\s|<.*?>", '', text)

    def process_item(self, item, spider):
        if isinstance(item, DetailItem):
            item['pos_info'] = [self.wash(item['pos_info'][0])]
            item['corp_info'] = [self.wash(item['corp_info'][0])]
        return item


class MongoPipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        self.db[RecruitItem.collection].create_index(
            [('id', pymongo.ASCENDING)])

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if isinstance(item, RecruitItem):
            self.db[item.collection].update(
                {'id': item.get('jobid')}, {'$set': item}, True)
        if isinstance(item, DetailItem):
            self.db[item.collection].update(
                {'id': item.get('jobid')},
                {
                    '$addToSet':
                    {
                        'pos_info': {'$each': item['pos_info']},
                        'corp_info': {'$each': item['corp_info']}
                    }
                }, True
            )
        return item
