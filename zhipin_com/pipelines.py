# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import datetime
import logging
import pymysql
import jieba.analyse as ana
from sql_exec import sql_start

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter



class ZhipinComPipeline(sql_start):
    data_list = []
    data_keys = []
    mysql_table = ''

    def process_item(self, item, spider):
        item = sql_start.sqlstart(self, item)
        return item

    def close_spider(self, spider):
        self.update_into(self.mysql_table, self.data_keys, self.data_list)
        self.cursor.close()
        self.conn.close()
