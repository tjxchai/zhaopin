import scrapy, json, time
from selenium import webdriver


class JobinfoSpider(scrapy.Spider):
    name = 'jobinfo'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/web/geek/job?query=']

    def parse(self, response):
        sql="select * from url limit 1"
        pass