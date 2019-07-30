import webbrowser
import requests
import re
import traceback
import logging
import time
from src.Utility import ToolFile
import bs4
import os

logging.debug("")
logging.debug("-" * 20 + " WebBrowserProcess.py")

# address = input("請輪入地址:")
# webbrowser.open("http://www.google.com.tw/maps/place/" + address)

# url_address = "http://www.grandtech.info/file_not_existed"
# url_address = "http://www.grandtech.info/"
url_address = "http://aaa.24ht.com.tw/"

def split_html_error_log():
    return traceback.format_exc().split("\n")


def check_url(url):
    """檢查網址的合法性"""
    # 偽裝瀏覽器
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
            Safari/537.36', }
    html_data = None
    try:
        html_data = requests.get(url, headers=headers)      # 處理網址錯誤的問題
        # html_data = requests.get(url)
        logging.info("網頁下載成功(%s)", url)
        try:
            html_data.raise_for_status()                    # 無法處理網址錯誤的問題，只能處理正確網址的後面附加檔案的問題
            logging.info("網址正確(%s)", url)
        except requests.exceptions.HTTPError as err:
            logging.error("網址錯誤(requests.exceptions.HTTPError):%s" % err)
            txt_list = split_html_error_log()
            for txt in txt_list:
                logging.error(txt)
        except Exception as err:
            logging.error("網址錯誤(Exception):%s" % err)
    except requests.exceptions.ConnectionError as err:
        logging.error("網頁下載錯誤(requests.exceptions.ConnectionError):%s" % err)
    except Exception as err:
        logging.error("網頁下載錯誤(Exception):%s" % err)

    return html_data


def save_html_file(file_name, parm_html_file):
    """儲存抓回來網頁的內容"""
    with open(file_name, "wb") as file_obj:
        for diskStorage in parm_html_file.iter_content(1024 * 10):
            size = file_obj.write(diskStorage)
            logging.info("%s" % size)
        logging.info("以 %s 儲存網頁成功" % file_name)


def search_html_file(parm_html_file):
    """搜尋 html 的內容"""
    if parm_html_file.status_code == requests.codes.ok:
        print("取得網頁內容成功:")
        pattern = input("請輪入欲搜尋的字串:")
        if pattern in parm_html_file.text:
            print("搜尋 %s 成功" % pattern)
        else:
            print("搜尋 %s 失敗" % pattern)

        name = re.findall(pattern, parm_html_file.text)
        if name != None:
            print("%s 出現 %d 次" % (pattern, len(name)))
        else:
            print("error %s 出現 %d 次" % (pattern, len(name)))
    else:
        print("取得網頁內容失敗:")


def test():
    htmlFile = open("./resource/myhtml.html", encoding="utf-8")
    objSoup = bs4.BeautifulSoup(htmlFile, "lxml")
    objTag = objSoup.find("h1")         # 搜尋第一個
    print(objSoup.title)
    print(objSoup.title.text)
    print(objTag)
    print(objTag.text)
    print("")
    objTag = objSoup.find_all("h1")
    # 取網頁的內容下面二個方式都可，objTag[0].getText() 、 data.text
    print(objTag[0].getText())
    print(objTag)
    for data in objTag:
        print(data.text)
    print("")
    objTag = objSoup.select("#author")
    print(objTag[0].attrs)
    print(objTag[0].getText)
    print(objTag[0].get_text)


file_dir = "./out21_25/"

html_file = check_url(url_address)
ToolFile.check_dir(file_dir)

obj_Soup = bs4.BeautifulSoup(html_file.text, "lxml")
img_tag = obj_Soup.select("img")
print("搜尋到的圖片數量:", len(img_tag))
if len(img_tag) > 0:
    for i in range(len(img_tag)):
        img_url = img_tag[i].get("src")
        print("%s 圖片下載中..." % img_url)
        file_url = url_address + img_url
        print("%s 圖片下載中..." % file_url)
        donwload_html_file = check_url(file_url)
        donwload_path = os.path.join(file_dir, os.path.basename(img_url))
        save_html_file(donwload_path, donwload_html_file)

# save_html_file("./resource/test.html", html_file)
# search_html_file(html_file)
# print(html_file)

tet = file_dir[-2:]
print(tet)



# print("網頁內容大小:" , len(html_file.text))
# print(html_file.text)
