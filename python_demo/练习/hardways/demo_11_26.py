from selenium import webdriver

if __name__ == '__main__':
    browser = webdriver.Chrome()
    url = 'http://www.baidu.com/'
    browser.get(url)
    browser.find_element_by_id("kw").clear()
    browser.find_element_by_id("kw").send_keys("douban")
