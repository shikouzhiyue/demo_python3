# selenium浏览器模拟登陆
from selenium import webdriver
import json

url = 'https://passport.baidu.com/v2/?login'
browser = webdriver.Chrome()
browser.get(url)
# 清除搜索框
browser.find_element_by_id("TANGRAM__PSP_3__userName").clear()
# # 通过id方式定位，并输入内容
browser.find_element_by_id("TANGRAM__PSP_3__userName").send_keys('shikouyue2')
browser.find_element_by_id("TANGRAM__PSP_3__password").clear()
browser.find_element_by_id("TANGRAM__PSP_3__password").send_keys('huwang199500')
browser.find_element_by_id("TANGRAM__PSP_3__submit").click()
# #点击按钮
# browser.find_element_by_id("su").click()
# #通过id方式定位
# browser.find_element_by_id("kw").send_keys("selenium")
# #通过name方式定位
# browser.find_element_by_name("wd").send_keys("selenium")
# #通过tag name方式定位
# browser.find_element_by_tag_name("input").send_keys("selenium")
# browser.find_element_by_tag_name("button").click()
# # 通过class name 方式定位
# browser.find_element_by_class_name("btn btn-primary  sbt ").send_keys("selenium")
# #通过CSS方式定位
# browser.find_element_by_css_selector("#kw").send_keys("selenium")
# 通过xphan方式定位
# browser.find_element_by_xpath('//*[@id="kw"]').send_keys("selenium")
#获取cookie
# cookie = [item["name"] + "=" + item["value"] for item in browser.get_cookies()]
print(browser.get_cookies())
# dict = {}
# for item in cookie:
#     itm = item.split("=")
#     dict[itm[0]] = itm[1]
#
# file = open("cookie.json","w")
# file.write(json.dumps(dict))
# file.close()
browser.quit()
