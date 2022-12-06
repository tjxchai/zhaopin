import requests
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def get_cookies(url, url1):
    '''使用Selenium模拟浏览器登录并获取cookies'''
    cookies = []
    browser = webdriver.Chrome(executable_path="geckodriver.exe")
    # 等待3秒，用于等待浏览器启动完成，否则可能报错
    time.sleep(2)

    browser.get(url)  # ①
    time.sleep(1)
    # 获取输入用户名的文本框
    # elem_user = browser.find_element("//input[@id='username']")
    elem_user = browser.find_element(By.XPATH, r"//div[2]/input")
    # # 模拟输入用户名
    # elem_user.send_keys('17788113680')  # ②
    elem_user.send_keys('adm')  # ②
    # # 获取输入密码的文本框
    elem_pwd = browser.find_element(By.XPATH, r"//div[4]/input")
    # # 模拟输入密码
    # elem_pwd.send_keys('zlx789456#')  # ③
    elem_pwd.send_keys('ft123')  # ③
    # # 获取提交按钮
    commit = browser.find_element(By.XPATH, r"//button[@id='submit']")
    # # 模拟单击提交按钮
    commit.click()  # ④
    # 暂停10秒，等待浏览器登录完成
    time.sleep(6)
    # 登录成功后获取cookie
    # return browser.sess
    # return browser.session_id()
    # browser.get(url1)  # ①
    return browser.get_cookies()




def get_cookies1(url, url1,url2):

    '''使用Selenium模拟浏览器登录并获取cookies'''
    browser = webdriver.Chrome(executable_path="geckodriver.exe")
    # 等待3秒，用于等待浏览器启动完成，否则可能报错
    time.sleep(2)
    browser.delete_all_cookies()
    browser.get(url)  # ①
    time.sleep(2)
    browser.get(url1)  # ①
    time.sleep(6)
    browser.get(url2)  # ①
    time.sleep(2)
    return browser.get_cookies()

url = ['https://weibo.com/login.php',
       'http://ft.naopi.cn/Main/Login',
       'https://www.jb51.net/article/171069.htm',
       'https://www.zhipin.com/zhengzhou/',
       'https://www.zhipin.com/web/geek/job?city=101180100&areaBusiness=410105',
       'https://www.zhipin.com/wapi/zpgeek/search/joblist.json?scene=1&query=&city=101180100&experience=&degree=&industry=&scale=&stage=&position=&salary=&multiBusinessDistrict=410105:38344261_83794426&page=1&pageSize=30'
       ]
login_cookies = get_cookies1(url[3], url[4], url[5])

print(login_cookies)
cookies = {}
for i in login_cookies:
    print(i['name'], i['value'])
    cookies[i['name']] = i['value']

print(cookies)


# headers = {
#     'Origin': 'http://ft.naopi.cn',
#     'Referer': 'http://ft.naopi.cn/Main/Indexa',
#     'Host': 'ft.naopi.cn'
# }


headers = {
    # ':authority': 'www.zhipin.com',
    # ':path': '/wapi/zpgeek/search/joblist.json?scene=1&query=&city=101180100&experience=&degree=&industry=&scale=&stage=&position=&salary=&multiBusinessDistrict=410105&page=1&pageSize=30',
    'Origin': 'http://ft.naopi.cn',
    'Referer': 'https://www.zhipin.com/web/geek/job?city=101180100&areaBusiness=410105',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Core/1.94.186.400 QQBrowser/11.3.5195.400',
    'Host': 'ft.naopi.cn'
}


url1 = 'https://www.zhipin.com/wapi/zpgeek/search/joblist.json?scene=1&query=&city=101180100&experience=&degree=&industry=&scale=&stage=&position=&salary=&multiBusinessDistrict=410105&page=1&pageSize=30'
# ret = requests.post(url1, data={'id': '1'}, cookies=cookies, headers=headers)
ret = requests.get(url1, cookies=cookies, headers=headers)
print(ret.text)
