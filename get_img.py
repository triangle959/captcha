#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
# @Author   :Zhangjinzhou
# @Time     :2019/4/17 17:55
# @Filename :get_img.py


from selenium import webdriver
from PIL import Image
from selenium.webdriver.support.wait import WebDriverWait

url = 'http://106.13.9.45:8996/signup'
options = webdriver.ChromeOptions()
# 不加载图片,加快访问速度
# options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
# 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_argument('--headless')
browser = webdriver.Chrome(executable_path="G:\chromedriver_win32\chromedriver.exe", options=options)

# 打开网页
browser.get(url)

element = browser.find_element_by_xpath('//*[@id="checkCode"]')    #找到验证码图片
print(element.location)                # 打印元素坐标
print(element.size)                    # 打印元素大小
left = element.location['x']
top = element.location['y']
right = element.location['x'] + element.size['width']
bottom = element.location['y'] + element.size['height']

for i in range(10):
    browser.save_screenshot('./img/'+ str(i) +'.png')
    im = Image.open('./img/'+ str(i) +'.png')
    im = im.crop((left, top, right, bottom))
    im.save('./img/'+ str(i) +'.png')                          # 将得到的图片保存在本地
    browser.refresh()

browser.close()