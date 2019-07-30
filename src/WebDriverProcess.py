from selenium import webdriver
import selenium
# Forefox 需要下載 geckodriver
# Chrome 需要下載 chromedriver
import time
from selenium.webdriver.common.keys import Keys

driver_path = "E:/geckodriver/geckodriver.exe"
browser = webdriver.Firefox(executable_path=driver_path)
url = "http://aaa.24ht.com.tw"
url = 'http://www.grandtech.info'
# url = "http://www.grandtech.info/file_not_existed"
# url = "http://www.grandtech.info/"
browser.get(url)

# ele = browser.find_element_by_tag_name('body')
# time.sleep(3)
# ele.send_keys(Keys.PAGE_DOWN)       # 網頁捲動到下一頁
# time.sleep(3)
# ele.send_keys(Keys.END)             # 網頁捲動到最底端
# time.sleep(3)
# ele.send_keys(Keys.PAGE_UP)         # 網頁捲動到上一頁
# time.sleep(3)
# ele.send_keys(Keys.HOME)            # 網頁捲動到最上端

txtBox = browser.find_element_by_id('key')
txtBox.send_keys('洪錦魁')          # 輸入表單資料
time.sleep(5)                       # 暫停5秒
txtBox.submit()                     # 送出表單

browser.refresh()                   # 沒這行會掛掉

eleLink = browser.find_element_by_link_text('認證考試')
print(type(eleLink))            # 列印eleLink資料類別
time.sleep(5)                   # 暫停5秒
eleLink.click()                 # 執行超連結至書級的證照類別


try:
    tag = browser.find_element_by_tag_name('title')
    print("標籤名稱 = %s, 內容是 = %s " % (tag.tag_name, browser.title))

    tag = browser.find_element_by_id("author")
    print("\n標籤名稱 = %s, 內容是 = %s " % (tag.tag_name, tag.text))

    print("")
    tag = browser.find_elements_by_id("content")
    for i in range(len(tag)):
        print("標籤名稱 = %s, 內容是 = %s " % (tag[i].tag_name, tag[i].text))

    print("")
    tag = browser.find_elements_by_tag_name("p")
    for i in range(len(tag)):
        print("標籤名稱 = %s, 內容是 = %s " % (tag[i].tag_name, tag[i].text))

    print("")
    tag = browser.find_elements_by_tag_name("img")
    for i in range(len(tag)):
        print("標籤名稱 = %s, 內容是 = %s " % (tag[i].tag_name, tag[i].get_attribute("src")))

except:
    print("沒有找到相符的元素")

browser.quit()
