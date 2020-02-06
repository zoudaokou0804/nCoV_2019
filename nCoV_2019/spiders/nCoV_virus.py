"# -*- encoding:utf-8 -*_",
import os
import sys
import scrapy
# 以下代码解决导入类名报错问题（找不到item类）
fpath = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ffpath = os.path.abspath(os.path.join(fpath, ".."))
print(ffpath)
sys.path.append(ffpath)
from Ncov2019.items import "items文件中Item类名"


class NcovVirusSpider(scrapy.Spider):
    name = 'nCoV_virus'
    allowed_domains = ['https://news.sina.cn']
    start_urls = ['https://news.sina.cn/zt_d/yiqing0121?from=singlemessage&isappinstalled=0']

    def parse(self, response):
        list=response.xpath()
