import json

import scrapy


class ZhiweiSpider(scrapy.Spider):
    name = 'zhiwei'
    allowed_domains = ['www.zhipin.com']
    start_urls = ['http://www.zhipin.com/']

    def parse(self, response):
        pass
        url = 'https://www.zhipin.com/wapi/zpCommon/data/cityGroup.json'
        yield scrapy.Request(url, callback=self.city)

    def city(self, response):
        resp = json.loads(response.text)
        resp = resp['zpData']['cityGroup']
        k = 0
        datalist = {'mysql_table': 'city'}
        for i in resp:
            for j in i['cityList']:
                k += 1
                datalist[k] = {'city_name': j['name'], 'city_code': j['code']}
        yield datalist
        for i in range(len(datalist) - 1):
            # print(datalist[i + 1])
            url = 'https://www.zhipin.com/wapi/zpgeek/businessDistrict.json?cityCode=' + str(
                datalist[i + 1]['city_code'])
            yield scrapy.Request(url, callback=self.business)
            # break

    def business(self, response):
        resp = json.loads(response.text)
        citycode = resp['zpData']['businessDistrict']['code']
        cityname = resp['zpData']['businessDistrict']['name']
        resp = resp['zpData']['businessDistrict']['subLevelModelList']
        k = 0

        datalist = {'mysql_table': 'district'}
        for i in resp:
            if i['subLevelModelList'] != None:
                for j in i['subLevelModelList']:
                    k += 1
                    url = 'https://www.zhipin.com/web/geek/job?city=' + str(citycode) + '&areaBusiness=' + str(
                        i['code']) + '%3A' + str(j['code'])
                    datalist[k] = {'city_code': citycode, 'countyname': i['name'], 'countyncode': i['code'],
                                   'district_name': j['name'], 'district_code': j['code'], 'url': url}
            else:
                k += 1
                datalist[k] = {'city_code': citycode, 'countyname': i['name'], 'countyncode': i['code'],
                               'district_name': '', 'district_code': '', 'url': ''}

        yield datalist
    # print(datalist)
