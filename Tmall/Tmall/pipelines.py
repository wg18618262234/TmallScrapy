# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv


class TmallPipeline(object):
    def process_item(self, item, spider):
        data = [
            str(item['item_id']),
            str(item['sold']),
            str(item['quantity']),
            str(item['totalSoldQuantity']),
            str(item['url']), str(item['price']),
            str(item['titleUnderIconList'])
        ]

        with open('goods.csv', 'a', newline='') as csv_file:
            csv_write = csv.writer(csv_file)
            csv_write.writerow(data)
        return item
