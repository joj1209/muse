from bs4 import BeautifulSoup
import time
import pandas as pd
import requests
import logging
from dbms.common.common_func import save_data
from dbms.models.api_models import EvCarPortal

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
class EvGoKrSubsidyParser():

    trs = []

    def __init__(self, html_text):
        # print('---init')
        bsobj = BeautifulSoup(html_text, "html.parser")
        table = bsobj.find("table", {"class": "table01 fz15"})
        # print(table)
        
        self.trs = table.find("tbody").find_all("tr")

    def parse_tr(self,tr):
        # print('---parse_tr')
        ths = tr.find_all("td")
        tds = tr.find_all("td")

        sido = ths[0].text
        region = ths[1].text

        replace_brackets = lambda x: x.replace("(", "").replace(")", "").split(" ")[1:]

        ## form_bak = lambda a, b, c, d, e: {"sido": a, "region": b, "sep1": c, "sep2": d, "value": e}
        form = lambda a, b, c, d, e, f, g: {"strd_dt":a, "sido_nm": b, "region": c, "receipt_way": d, "receipt_priority": e, "value": f, "ins_dt":g}

        민간공고대수 = replace_brackets(tds[5].text)
        접수대수 = replace_brackets(tds[6].text)
        출고대수 = replace_brackets(tds[7].text)
        출고잔여대수 = replace_brackets(tds[8].text)
        
        strd_dt = time.strftime(('%Y%m%d'))
        ins_dt = time.strftime(('%Y%m%d%H%M%S'))

        l = [
            form(strd_dt,sido, region, "민간공고대수", "우선순위"   , int(민간공고대수[0]),ins_dt),
            form(strd_dt,sido, region, "민간공고대수", "법인과기관" , int(민간공고대수[1]),ins_dt),
            form(strd_dt,sido, region, "민간공고대수", "택시"      , int(민간공고대수[2]),ins_dt),
            form(strd_dt,sido, region, "민간공고대수", "우선비대상" , int(민간공고대수[3]),ins_dt),
            form(strd_dt,sido, region, "접수대수"    , "우선순위"  , int(접수대수[0]),ins_dt),
            form(strd_dt,sido, region, "접수대수"    , "법인과기관", int(접수대수[1]),ins_dt),
            form(strd_dt,sido, region, "접수대수"    , "택시"      , int(접수대수[2]),ins_dt),
            form(strd_dt,sido, region, "접수대수"    , "우선비대상", int(접수대수[3]),ins_dt),
            form(strd_dt,sido, region, "출고대수"    , "우선순위"  , int(출고대수[0]),ins_dt),
            form(strd_dt,sido, region, "출고대수"    , "법인과기관", int(출고대수[1]),ins_dt),
            form(strd_dt,sido, region, "출고대수"    , "택시"      , int(출고대수[2]),ins_dt),
            form(strd_dt,sido, region, "출고대수"    , "우선비대상", int(출고대수[3]),ins_dt),
            form(strd_dt,sido, region, "출고잔여대수", "우선순위"  , int(출고잔여대수[0]),ins_dt),
            form(strd_dt,sido, region, "출고잔여대수", "법인과기관", int(출고잔여대수[1]),ins_dt),
            form(strd_dt,sido, region, "출고잔여대수", "택시"      , int(출고잔여대수[2]),ins_dt),
            form(strd_dt,sido, region, "출고잔여대수", "우선비대상", int(출고잔여대수[3]),ins_dt),
        ]

        return l

    def parse(self):
        collected_list = []
        for tr in self.trs:
            row = self.parse_tr(tr)
            collected_list += row
            
        return collected_list

    # 미사용
    def save_to_excel(self, excel_filename):
        collected_list = self.parse()
        df = pd.DataFrame(collected_list)
        df.to_excel(excel_filename)
        
        
def run_crawl_ev_og_portal():

    logger.info('--02 [run_crawl_ev_og_portal] Start !!')
    
    # url = "https://ev.or.kr/nportal/buySupprt/initSubsidyPaymentCheckAction.do"
    # url = "https://www.ev.or.kr/portal/localInfo"   
    # req = requests.get(url)
    # html = req.text
    
    f = open("local_info2.html", encoding="utf-8")
    html = f.read()

    ev_or_kr_parser = EvGoKrSubsidyParser(html)

    df_dic = ev_or_kr_parser.parse()
    
    # print("df_dic:",df_dic)

    save_data(df_dic, EvCarPortal)
    
    # 미사용:엑셀저장
    # ev_or_kr_parser.save_to_excel("all_sido2.xlsx")
    
    logger.info('--02 [run_crawl_ev_og_portal] End !!')
    print('\n\n')


