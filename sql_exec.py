import datetime
import logging
import pymysql
import scrapy
from scrapy import crawler


def get_connect():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        passwd="123123",
        database='zhipin_com',
        charset='utf8'
    )

    return conn


class BasePipeline(object):
    def __init__(self):
        self.conn = get_connect()
        self.cursor = self.conn.cursor()
        self.fetch_data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.replace_sql_tem = "REPLACE INTO into {} ({}) values({})"
        self.update_sql_tem = 'INSERT INTO {} ({}) VALUES ({}) ON  DUPLICATE KEY UPDATE {}'

    def replace_into(self, table_name, keys, datalist):
        replace_sql = self.replace_sql_tem.format(table_name, ','.join(keys), ','.join(['%s'] * len(keys)))
        return self.save_mysql(replace_sql, datalist)

    def update_into(self, table_name, keys, datalist):
        update_sql = self.update_sql_tem.format(table_name, ','.join(keys), ','.join(['%s'] * len(keys)),
                                                ','.join(['{}=values({})'.format(x, x) for x in keys]))
        return self.save_mysql(update_sql, datalist)

    def save_mysql(self, sql, datalist):
        nums = ''
        try:
            nums = sql
            nums = self.cursor.executemany(sql, datalist)
            self.conn.commit()
        except:
            try:
                self.cursor.close()
                self.conn.close()

                self.conn = get_connect()
                self.cursor = self.conn.cursor()
                nums = self.cursor.executemany(sql, datalist)
                self.conn.commit()
            except Exception as e:
                logging.error('插入mysql失败,error={}'.format(e))
        return nums

    def read_mysql(self, sql):
        self.conn = get_connect()
        self.cursor = self.conn.cursor()
        results = 0
        try:
            results = sql
            results = self.cursor.execute(sql)
            results = self.cursor.fetchall()
        except:
            try:
                self.cursor.close()
                self.conn.close()

                self.conn = get_connect()
                self.cursor = self.conn.cursor()
                results = self.cursor.fetchall()
            except Exception as e:
                logging.error('查询mysql失败,error={}'.format(e))
        return results


class sql_start(BasePipeline):

    data_list = []
    data_keys = []
    mysql_table = ''
    def sqlstart(self, item):
        self.data_keys = item.get(1, '')
        self.mysql_table = item['mysql_table']
        for i in item:
            if i != 'mysql_table':
                self.data_list.append(tuple(item[i].get(x) for x in self.data_keys))
        if len(self.data_list) >= 1:
            print(self.update_into(self.mysql_table, self.data_keys, self.data_list))
            self.data_list = []
        return item

    def close_conn(self):
        self.cursor.close()
        self.conn.close()
