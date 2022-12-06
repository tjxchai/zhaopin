import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_cookies(url):
    '''使用Selenium模拟浏览器登录并获取cookies'''
    browser = webdriver.Chrome(executable_path="geckodriver.exe")
    # 等待3秒，用于等待浏览器启动完成，否则可能报错
    time.sleep(2)
    browser.delete_all_cookies()
    browser.get(url)  # ①
    time.sleep(20)
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
    while 1:
        time.sleep(60)
    return cookies
