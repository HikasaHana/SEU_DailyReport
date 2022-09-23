# coding=UTF8

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
import re
import os
import base64


# 通过webhook发送消息
def send_msg(message):
    webhook = 'http://43.153.176.127/send_private_msg'  # webhook URL，可自行部署，或使用默认
    qq = ''      # 要使用默认webhook功能，请填入QQ号码，并加1211966553为好友
    if qq != '':
        data = {"user_id": qq,
                "message": message}
        requests.post(webhook, data)
    
    
# 通过webhook发送截图
def send_screenshots(driver):
    timeline = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    pic_path = "%s.png" % timeline
    driver.get_screenshot_as_file(pic_path)
    with open(pic_path, "rb") as f:
        img_data = f.read()
        base64_data = base64.b64encode(img_data)
        base64_str = str(base64_data, "utf-8")
        base_str = 'base64://' + base64_str
        cq_img = '[CQ:image,file=' + base_str + ',cache=1]'
    send_msg(cq_img)
    os.remove(pic_path)
    
    
# 获取ip地址
def getOutterIP(ip):
    if ip == '':
        try:
            res = requests.get('https://myip.ipip.net', timeout=5).text
            ip = re.findall(r'(\d+\.\d+\.\d+\.\d+)', res)
            ip = ip[0] if ip else ''
        except:
            pass
    return ip
    
    
# 配置信息
number = ''     # 一卡通号
password = ''       # 密码
ip = ''     # ip地址，若不填则默认获取本地ip
temp = '36.3'   # 体温，默认36.3

# 如果edgedriver文件夹不在环境变量中，则添加
if os.environ["PATH"].find('edgedriver') == -1:
    file_path = os.path.split(os.path.realpath(__file__))[0] + '\edgedriver_win32'
    os.environ["PATH"] += os.pathsep + file_path

# 打开浏览器
options = webdriver.EdgeOptions()
useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'     # 默认win10的useragent，可自行修改
options.add_argument("user-agent:{}".format(useragent))
options.add_argument("--proxy-server = http://{}".format(getOutterIP(ip)))
driver = webdriver.Edge(options=options)
url = 'http://ehall.seu.edu.cn/qljfwapp2/sys/lwReportEpidemicSeu/index.do?t_s=1663806336536&amp_sec_version_=1&gid_=UHltZHBQNHNManRNSm1TZzRESHh2ZlAxWERmZmJ3UFNMR0dXTWkweDArK1VEMXF6YVBqNmd5NFl2NGRRVGdTQ3hUZFgzK1UyaTRlT1JFV2o4WFZONHc9PQ&EMAP_LANG=zh&THEME=indigo#/dailyReport'
while True:
    try:
        driver.get(url)
        break
    except:
        driver.refresh()
        time.sleep(10)

# 关闭多余窗口
now = driver.current_window_handle
all = driver.window_handles
for i in all:
    if i != now:
        driver.switch_to.window(i)
        driver.close()
driver.switch_to.window(now)

# 填报
driver.find_element(By.CSS_SELECTOR, '#username.auth_input').send_keys(number)
driver.find_element(By.CSS_SELECTOR, '#password.auth_input').send_keys(password)
driver.find_element(By.CSS_SELECTOR, '#casLoginForm > p:nth-child(5)').click()
if driver.find_element(By.CLASS_NAME, 'auth_error'):
    error = '登录失败！' + driver.find_element(By.CLASS_NAME, 'auth_error').text
    send_msg(error)
    driver.close()
    exit(-1)
time.sleep(10)
while True:
    try:
        report_time = driver.find_element(By.CSS_SELECTOR, '#row0emapdatatable > td:nth-child(95) > span').get_attribute('innerText')
        break
    except:
        driver.refresh()
        time.sleep(10)
try:
    driver.find_element(By.CSS_SELECTOR, 'body > main > article > section > div.bh-mb-16 > div.bh-btn.bh-btn-primary').click()
    time.sleep(10)
    driver.find_element(By.NAME, 'DZ_JSDTCJTW').send_keys('36.3')
    driver.find_element(By.CSS_SELECTOR, '#save').click()
    driver.find_element(By.CLASS_NAME, 'bh-dialog-btn').click()
    send_msg('填报成功！')
except:
    send_screenshots(driver)
    send_msg('填报异常！最新填报时间为%s，具体异常原因请检查截图！' % report_time)
driver.close()
