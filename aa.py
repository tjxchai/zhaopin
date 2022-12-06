# import time
# from selenium import webdriver
# import webbrowser as web
# from selenium.webdriver.common.by import By
#
url = 'https://www.zhipin.com/web/geek/job?query=&city=101180100'
# url1 = 'https://www.zhipin.com/wapi/zpgeek/search/joblist.json?scene=1&query=&city=101180100&experience=&degree=&industry=&scale=&stage=&position=&salary=&multiBusinessDistrict=&page=1&pageSize=30'
#
# weburl = 'C:/Users/Administrator/AppData/Roaming/360se6/Application/360se.exe'
# web.register('360se', None, web.BackgroundBrowser(weburl))
#
# web.get('360se').open(url)web
# time.sleep(10)
# web.get('360se').open(url1, new=0)
# time.sleep(10)
# web.get('360se').open(url1, new=0)

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

'''使用Selenium模拟浏览器登录并获取cookies'''
# browser = webdriver.Chrome(executable_path="geckodriver.exe")
browser = webdriver.Chrome(executable_path="C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chrome.exe")
browser.get(url)  # ①
time.sleep(100)
