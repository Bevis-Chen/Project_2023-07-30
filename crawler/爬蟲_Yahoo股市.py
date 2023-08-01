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
try:
    chrome = get_chrome(url1)
    soup1 = BeautifulSoup(chrome.page_source, "lxml")
    total_num_str = soup1.find(
        class_="Pb(0px) C(#6e7780) Fz(14px) Fz(14px)--mobile Fw(n)").text.split()[1]
    total_num = eval(total_num_str)
    while True:
        time.sleep(0.5)
        js = "window.scrollTo(0, document.body.scrollHeight);"
        chrome.execute_script(js)
        soup2 = BeautifulSoup(chrome.page_source, "lxml")
        lis = soup2.find("ul", class_="M(0) P(0) List(n)").find_all("li")
        if len(lis) == total_num:
            print("成功了!")
            break
except Exception as e:
    print(e)
