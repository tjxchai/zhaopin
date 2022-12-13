import random
from sql_exec import sql_start
import time
from selenium import webdriver

class base_info():

    def randinfo(self, x):
        temp = {}

        """下面是调用user_agents_list"""
        if x == 'user_agents_list':
            temp['user_agents_list'] = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60",
            "Opera/8.0 (Windows NT 5.1; U; en)",
            "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50",
            # Firefox
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
            "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
            # Safari
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
            # chrome
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16"
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
            # 1) Chrome # Win7:
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',  # 2) Firefox# Win7:
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
            # 3) Safari# Win7:
            'Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50',  # 4) Opera# Win7:
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)',
            # 5) IE# Win7+ie9：         # Win7+ie8：
            'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)',
            # WinXP+ie8：
            'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB7.0)',  # WinXP+ie7：
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)',  # WinXP+ie6：
            'Mozilla/5.0 (Windows; U; Windows NT 6.1; ) AppleWebKit/534.12 (KHTML, like Gecko) Maxthon/3.0 Safari/534.12',
            # 6) 傲游        # 傲游3.1.7在Win7+ie9,高速模式:
            # 傲游3.1.7在Win7+ie9,IE内核兼容模式:
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)',
            # 7) 搜狗        # 搜狗3.0在Win7+ie9,IE内核兼容模式:
            # 搜狗3.0在Win7+ie9,高速模式:
            'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.33 Safari/534.3 SE 2.X MetaSr 1.0',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)'
            # 8) 360        # 360浏览器3.0在Win7+ie9:
        ]



        """下面是调用IP代理地址"""
        if x == 'proxy_list':
            sql = "select ip,port from ip order by times desc limit 100"
            rows = sql_start.read_mysql(self, sql=sql)
            ip_port = []
            for i in rows:
                ip_port.append({'ip_port':  str(i[0]) + ':' + str(i[1])})
            temp['proxy_list'] = ip_port


        return random.choice(temp[x])

    def get_cookies(self,url):
        '''使用Selenium模拟浏览器登录并获取cookies'''
        browser = webdriver.Chrome(executable_path="geckodriver.exe")
        # 等待3秒，用于等待浏览器启动完成，否则可能报错
        time.sleep(2)
        browser.delete_all_cookies()
        browser.get(url)  # ①
        time.sleep(5)
        # # 获取输入用户名的文本框
        # elem_user = browser.find_element(By.XPATH, r"//div[2]/input")
        # # 模拟输入用户名
        # elem_user.send_keys('adm')  # ②
        # # 获取输入密码的文本框
        # elem_pwd = browser.find_element(By.XPATH, r"//div[4]/input")
        # # 模拟输入密码
        # elem_pwd.send_keys('ft123')  # ③
        # # 获取提交按钮
        # commit = browser.find_element(By.XPATH, r"//button[@id='submit']")
        # commit.click()  # 模拟单击提交按钮
        # time.sleep(6)  # 暂停10秒，等待浏览器登录完成
        cookies = {}
        for i in browser.get_cookies():  # 登录成功后获取cookie
            # print(i['name'], i['value'])
            cookies[i['name']] = i['value']
        return cookies
