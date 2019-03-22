# -*- coding: utf-8 -*-
import scrapy
import sys
import json
import logging

sys.path.append('..')
from Tmall.items import TmallItem


class GoodsSpider(scrapy.Spider):
    name = 'goods'
    allowed_domains = ['tmall.com']
    # custom_settings = {
    #     'USER_AGENT': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1',
    #     # 'Referer': 'http://list.tmall.com/search_product.htm?spm=a223c.7814651.navcategory176.1&cat=50025145&from=nav_ct_176_8141_8142',
    # }
    start_urls = ['https://ochirly.m.tmall.com/shop/shop_auction_search.do?p=1&page_size=12']

    def parse(self, response):
        open('goodsinfo.txt', 'wb').write(response.text.encode('utf8'))
        # logging.warning(response.text.encode('utf8')[17:-1])
        data = eval(response.text.encode('utf8'))
        shop_id = data['shop_id']
        user_id = data['user_id']
        shop_title = data['shop_title']
        total_page = data['total_page']  # 商品总页数
        shop_Url = data['shop_Url']
        items = data['items']
        for p in range(1, int(total_page) + 1):
            print(p)
            yield scrapy.Request(url='https://ochirly.m.tmall.com/shop/shop_auction_search.do?page_size=12&p=' + str(p),
                                 callback=self.parse2, dont_filter=True)

    def parse2(self, response):
        print(response.url)
        data = eval(response.text.encode('utf8'))
        items = data['items']
        for it in items:
            item = TmallItem()
            item['item_id'] = it['item_id']
            item['title'] = it['title']
            item['img'] = it['img']
            item['sold'] = it['sold']
            item['quantity'] = it['quantity']
            item['totalSoldQuantity'] = it['totalSoldQuantity']
            item['url'] = it['url']
            item['price'] = it['price']
            item['titleUnderIconList'] = it['titleUnderIconList']
            yield item
