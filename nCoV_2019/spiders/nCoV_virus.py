"# -*- encoding:utf-8 -*_",
import os
import sys
import scrapy
from selenium import webdriver
import time, re
from bs4 import BeautifulSoup
# 以下代码解决导入类名报错问题（找不到item类）
fpath = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ffpath = os.path.abspath(os.path.join(fpath, ".."))
print(ffpath)
sys.path.append(ffpath)
# from Ncov2019.items import "items文件中Item类名"      


class NcovVirusSpider(scrapy.Spider):
    name = 'nCoV_virus'     
    allowed_domains = ['https://news.sina.cn']
    start_urls = ['https://news.sina.cn/zt_d/yiqing0121?from=singlemessage&isappinstalled=0']

    def parse(self, response):
        url = R'https://news.sina.cn/zt_d/yiqing0121?from=singlemessage&isappinstalled=0'
        chromedriver = 'C:\迅雷下载\chromedriver.exe'
        options = webdriver.ChromeOptions()
        options.add_argument('User-Agent = Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36')
        driver = webdriver.Chrome(chromedriver, chrome_options=options)
        driver.get(url)
        driver.refresh()
        html=driver.page_source
        bf = BeautifulSoup(html, 'lxml')
        print(bf.text)
