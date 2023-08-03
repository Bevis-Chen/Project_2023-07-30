import requests
import time
import copy
import json
import pandas as pd
from tools import get_chrome, get_soup, get_time
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent


url1 = "https://tw.stock.yahoo.com/class-quote?sectorId=26&exchange=TAI"
# 滚动到浏览器顶部
js_top = "var q=document.documentElement.scrollTop=0"
# 滚动到浏览器底部
js_bottom = "window.scrollTo(0,document.body.scrollHeight)"


def get_one_page_data():
    try:
        global chrome
        # , hide=True
        chrome = get_chrome(url1)
        soup1 = BeautifulSoup(chrome.page_source, "lxml")
        total_num_str = soup1.find(
            class_="Pb(0px) C(#6e7780) Fz(14px) Fz(14px)--mobile Fw(n)").text.split()[1]
        total_num = eval(total_num_str)
        while True:
            # time.sleep(0.5)
            chrome.execute_script(js_bottom)
            soup2 = BeautifulSoup(chrome.page_source, "lxml")
            lis = soup2.find("ul", class_="M(0) P(0) List(n)").find_all("li")
            if len(lis) == total_num:
                print("成功了~٩(๑•̀ㅂ•́)و٩(๑•̀ㅂ•́)و~~!")
                break
        # time.sleep(1)
        chrome.execute_script(js_top)
        soup2 = BeautifulSoup(chrome.page_source, "lxml")
        title_list = []
        title1 = soup2.find(
            "div", class_="Fxs(0) Fg(1) Fb(116px) Ta(start) Mend(12px)").text.split("/")
        title2 = soup2.find(
            "div", class_="table-header-wrapper").find_all("div", class_="Fxg(1)")
        title_list.extend(title1)
        for i in title2:
            title_list.append(i.text)
        title = title_list[0:3]+title_list[-4:-1]
        lis = soup2.find("ul", class_="M(0) P(0) List(n)").find_all("li")
        datas = []
        for li in lis:
            data = [li.find("div", class_="Lh(20px)").text, li.find("span", class_="Fz(14px)").text] + \
                [i.text for i in li.find_all(class_="Fxg(1)")]
            datas.append(data[0:3]+data[-4:-1])

    except Exception as e:
        print("拿尼~(*´･д･)?(*´･д･)?(*´･д･)?")
        print(e)
    return title, datas
# datas= get_one_page_data()
# df = pd.DataFrame(datas, columns=title)
# df1 = pd.DataFrame(datas, columns=title_list).set_index(["股票名稱"])


if __name__ == "__main__":
    print(get_one_page_data())
