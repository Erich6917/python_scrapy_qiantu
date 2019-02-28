# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy_qiantu.spiders.logger_util import *
from scrapy.http import Request


class QiantuSpider(scrapy.Spider):
    name = 'qiantu'
    allowed_domains = ['58pic.com']
    start_urls = ['http://www.58pic.com/piccate/9-0-0.html']

    def parse(self, response):

        page_total = self.get_page_total(response)
        if not page_total:
            return
        println()

        # item_xpath = '//div[@class="clickRecord"]/div/div/p/span[@class="title-text"]/text()'
        # res = response.xpath(item_xpath).extract()
        # infos(page_total)


        yield Request(url=response.url,
                      # meta={"front_image_url": urljoin(response.url, image_url)},
                      callback=self.parse_detail)


        item_pages = '//div[@class="qt-pagination"]' \
                     '//span[@class="cpage"]' \
                     '/following-sibling::a[1]/@href'
        next_page = response.xpath(item_pages).extract_first()
        if next_page:
            infos('telnet ne    xt page > {}'.format(next_page))
            yield Request(url=next_page,
                          # meta={"front_image_url": urljoin(response.url, image_url)},
                          callback=self.parse)
        # else:
        #     infos(">>>>>>>>>>>...the END...未找到NEXT PAGE")

        println()
        pass

    def get_page_total(self, response):
        res = response.xpath('//div[@class="adstyle-bgcolor"]'
                             '/div[@class="result-wrapper w1500"]'
                             '/div[@class="bread-crumbs"]'
                             '/em[@class="text-orange"]'
                             '/text()').extract_first()

        match = re.search('([0-9]+)', res)
        if match:
            return match.group()
        else:
            errors("查找总结果数失败！")

    def parse_detail(self, response):
        infos('>>>>>>>>>>>parse_detail<<<<<<<<<<<<<')

        item_xpath = '//div[@class="clickRecord"]/div/div/p/span[@class="title-text"]/text()'
        res = response.xpath(item_xpath).extract()
        for each in res:
            infos("title > {}".format(each))

        infos('URL > {} ,Total > {}'.format(response.url,len(res)))

        pass

# import requests
#
# url = 'http://www.58pic.com/newpic/25862637.html'
#
# hd = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#     'Accept-Encoding': 'gzip, deflate, sdch',
#     'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
#     'Connection': 'keep-alive',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
#     'Host': 'www.ximalaya.com'
# }
# req = requests.get(url,headers = hd)
#
# infos(req.text)