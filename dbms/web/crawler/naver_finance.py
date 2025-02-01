import time
import requests
import logging
from bs4 import BeautifulSoup
from dbms.common.common_func import save_data
from dbms.models.api_models import NaverFinance

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
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

    # 전일가
    td_first = bsobj.find("td", {"class":"first"})
    yesterday_price = td_first.find("em").find("span", {"class":"blind"}).text

    # 기준일자(당일), 입력일시(당일)
    global strd_dt
    strd_dt = time.strftime(('%Y%m%d'))
    ins_dt = time.strftime(('%Y%m%d%H%M%S'))

    dic = {"strd_dt":strd_dt, "stock_cd":code, "stock_nm":name, "pre_price":yesterday_price, "today_price":price, "trading_volume":volume, "ins_dt":ins_dt}

    return dic

def get_stock():
    stock_codes = ["035720", "005930", "379780", "433330", "418660"]
    # 035720 카카오
    # 005930 삼성전자
    #------- 051910 LG화학
    #------- 000660 SK하이닉스
    # 418660 TIGER 미국나스닥100레버리지(합성)
    # 379780 RISE 미국S&P500
    # 433330 SOL 미국S&P500
    rslt = []

    for code in stock_codes:
        bsobj = crawl_stock_date(code)
        dic = parse_data(bsobj)
        rslt.append(dic)

    return rslt

# def save_data():
def run_crawl_naver_finance():    

    logger.info('--01 [run_crawl_naver_finance] Start !!')
    
    df_dic = get_stock()

    save_data(df_dic, NaverFinance)
    
    logger.info('--01 [run_crawl_naver_finance] End !!')
    print('\n\n')

    
