import pandas as pd
import requests
import json
import urllib
import re
import time
import logging
from urllib.parse import quote
from datetime import date, timedelta
from dbms.common import config
from dbms.common.common_func import save_data
from dbms.models.api_models import JejuApiFloatingPopulation

pre_90_dt = (date.today()-timedelta(days=90)).strftime('%Y%m%d')
pre_150_dt = (date.today()-timedelta(days=150)).strftime('%Y%m%d')
strd_dt = time.strftime(('%Y%m%d'))
ins_dt = time.strftime(('%Y%m%d%H%M%S'))
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def api_call(start_dt, end_dt):
    # your_appkey = 't_0pcpt_22ejt0p0p2b0o_r12j5e08_t'
    your_appkey = config.YOUR_APPKEY

    data_all = []

    for datetime in pd.date_range(start='20240101', end='20240101'):
        date = str(datetime.date()).replace('-', '')
        query = quote('아라동')  # 연동, 화북동, 삼양동, 노형동, 아라동, 애월읍

        date = str(datetime.date()).replace('-', '')

        # print(date)

        # api_url = f"https://open.jejudatahub.net/api/proxy/Daaa1t3at3tt8a8DD3t55538t35Dab1t/{your_appkey}?startDate={date}&endDate={date}&emd=" + query
        api_url = f"https://open.jejudatahub.net/api/proxy/Daaa1t3at3tt8a8DD3t55538t35Dab1t/{your_appkey}?startDate={pre_150_dt}&endDate={pre_90_dt}&emd=" + query

        weburl = urllib.request.urlopen(api_url)
        data = weburl.read()
        data_all.append(data)
        # numbers = re.findall(r'\d+', str(data))
        # numbers_all.append(numbers)

    # print('data:',data)

    contents = json.loads(data)
    row_data=contents.get('data')
    df_tmp = pd.DataFrame(row_data)

    print(df_tmp)
    
    # 인덱스 재배열
    df_tmp.reset_index(drop=False)
    
    
    
    df_tmp.insert(0,'strd_dt',strd_dt)
    df_tmp['ins_dt'] = ins_dt   

    # 인덱스 삭제(실제로는 열로 변환됨)
    df = df_tmp.reset_index(drop=True)

    # 컬럼정의
    df.columns = ['strd_dt','regist_dt','city','emd','gender','age_group','resd_pop','work_pop','visit_pop','ins_dt']
    
    save_data(df.to_dict('records'), JejuApiFloatingPopulation) 
    
    # print(row_data)

# jeju_api_run()



def run_api_jeju_floating_population():
    start_dt = '20240101'
    end_dt = '20240101'
    
    logger.info('--10 [run_api_jeju_floating_population] Start !!')         
    
    api_call(start_dt, end_dt)
    
    logger.info('--10 [run_api_jeju_floating_population] End !!')         
    print('\n\n')