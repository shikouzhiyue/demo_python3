from selenium import webdriver

# options = webdriver.ChromeOptions()
# # 设置中文
# options.add_argument('lang=zh_CN.UTF-8')
# # 增加头部 手机样式
# options.add_argument(
#     'user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')
# url = 'http://image.baidu.com/'
# # 无图模式
# prefs = {
#     'profile.default_content_setting_values': {
#         'images': 2
#     }
# }
# options.add_experimental_option('prefs', prefs)
# #使用手机样式
# #browser = webdriver.Chrome(chrome_options=options)
# browser = webdriver.Chrome()
# browser.get(url)
# #selenium 使用js打开新的窗口
# newwindow = "window.open('https://www.baidu.com');"
# # 通过js新打开一个窗口
# browser.execute_script(newwindow)
# # 捕获所有的句柄
# handles = browser.window_handles
# 窗口切换，切换为新打开的窗口
# browser.switch_to_window(handles[-1])
# # 切换回最初打开的窗口
# browser.switch_to_window(handles[0])
# 携带cookie访问网页
url = "https://www.soushuba.com/"
browser = webdriver.Chrome()
# browser.get(url)
# # 通过js新打开一个窗口
# newwindow='window.open("https://www.baidu.com");'
# # 删除原来的cookie
# browser.delete_all_cookies()
# # 携带cookie打开
# browser.add_cookie({'name':'ABC','value':'DEF'})
# # 通过js新打开一个窗口
# browser.execute_script(newwindow)
# 设置最长加载时间为90秒
browser.set_page_load_timeout(5)
try:
	# 输入网址
	browser.get(url)
except:
	# 超过90秒强制停止加载
	browser.execute_script('window.stop()')
#selenium 能截取当前屏幕：
browser.save_screenshot("E:/img.png")