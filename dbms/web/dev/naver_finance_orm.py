import time

import pymysql
import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import date, datetime, timedelta
from dbms.models.api_models import NaverFinance
from django.db import models


def crawl_stock_date(code):
    url = f"https://finance.naver.com/item/main.naver?code={code}"
    res = requests.get(url)
    bsobj = BeautifulSoup(res.text, "html.parser")
    return bsobj

def parse_data(bsobj):
    div_today = bsobj.find("div", {"class":"today"})
    em = div_today.find("em")

    price = em.find("span", {"class":"blind"}).text
    h_company = bsobj.find("div", {"class":"h_company"})
    name = h_company.a.text
    div_description = h_company.find("div", {"class":"description"})
    code = div_description.span.text

    table_no_info = bsobj.find("table", {"class":"no_info"})
    tds = table_no_info.tr.find_all("td")
    volume = tds[2].find("span", {"class":"blind"}).text

    #----------- 전일가
    td_first = bsobj.find("td", {"class":"first"})
    yesterday_price = td_first.find("em").find("span", {"class":"blind"}).text
    # print("first_price:",td_first)
    # print("yesterday_price:", yesterday_price)

    global strd_dt
    strd_dt = time.strftime(('%Y%m%d'))
    ins_dt = time.strftime(('%Y%m%d%H%M%S'))

    dic = {"strd_dt":strd_dt, "code":code, "name":name, "yesterday_price":yesterday_price, "price":price, "volume":volume, "ins_dt":ins_dt}
    # print( dic)
    return dic

def get_stock():
    stock_codes = ["035720", "005930", "051910", "000660"]
    rslt = []

    for code in stock_codes:
        bsobj = crawl_stock_date(code)
        dic = parse_data(bsobj)
        rslt.append(dic)

    return rslt

aa = get_stock()
print(aa)

df = pd.DataFrame(aa)
# print(df.values[0])

# NaverFinance.objects.bulk_create(aa)