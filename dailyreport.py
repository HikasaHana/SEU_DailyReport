# coding=UTF8

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# 打开浏览器
options = webdriver.EdgeOptions()
useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'
options.add_argument("user-agent:{}".format(useragent))
options.add_argument("--proxy-server = http://{}".format('183.226.192.242'))    # 填入自己的ip地址
driver = webdriver.Edge(options=options)
driver.set_page_load_timeout(10)
url = 'http://ehall.seu.edu.cn/qljfwapp2/sys/lwReportEpidemicSeu/index.do?t_s=1663806336536&amp_sec_version_=1&gid_=UHltZHBQNHNManRNSm1TZzRESHh2ZlAxWERmZmJ3UFNMR0dXTWkweDArK1VEMXF6YVBqNmd5NFl2NGRRVGdTQ3hUZFgzK1UyaTRlT1JFV2o4WFZONHc9PQ&EMAP_LANG=zh&THEME=indigo#/dailyReport'
driver.get(url)

# 关闭多余窗口
now = driver.current_window_handle
all = driver.window_handles
for i in all:
    if i != now:
        driver.switch_to.window(i)
        driver.close()
driver.switch_to.window(now)

# 填报
driver.find_element(By.CSS_SELECTOR, '#username.auth_input').send_keys('213202650')     # 一卡通号
driver.find_element(By.CSS_SELECTOR, '#password.auth_input').send_keys('Hitorinogcq0701!')      # 密码
driver.find_element(By.CSS_SELECTOR, '#casLoginForm > p:nth-child(5)').click()
time.sleep(5)
try:
    driver.find_element(By.CSS_SELECTOR, 'body > main > article > section > div.bh-mb-16 > div.bh-btn.bh-btn-primary').click()
    time.sleep(3)
    driver.find_element(By.NAME, 'DZ_JSDTCJTW').send_keys('36.3')   # 体温
    driver.find_element(By.CSS_SELECTOR, '#save').click()
    driver.find_element(By.CLASS_NAME, 'bh-dialog-btn').click()
    print("上报成功！")
except:
    print("今日已填报！")
driver.close()
