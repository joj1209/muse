import pandas as pd
import requests
import time
import json
import urllib
import re
import logging
from urllib.parse import quote
from dbms.common import config
from dbms.common.common_func import save_data
from dbms.models.api_models import SeoulApiSpopFornLongResdJachi
from datetime import date, timedelta
from dbms.common import config

apikey = config.SEOUL_API_KEY
# apikey = '70517359706a6f6a3731477969764a'

# 자치구단위 서울 생활인구(장기체류 외국인)
sample_url = 'http://openapi.seoul.go.kr:8088/(인증키)/xml/SPOP_FORN_LONG_RESD_JACHI/1/5/'

pre_7_dt = (date.today()-timedelta(days=10)).strftime('%Y%m%d')
strd_dt = time.strftime(('%Y%m%d'))
ins_dt = time.strftime(('%Y%m%d%H%M%S'))
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def seoul_api_run():
    
    logger.info('--11 [run_api_jeju_seoul_api_runfloating_population] Start !!')         
    
    # API 요청
    startnum = 1
    endnum = 50
    url1 = f'http://openapi.seoul.go.kr:8088/{apikey}/json/SPOP_FORN_LONG_RESD_JACHI/{startnum}/{endnum}/{pre_7_dt}'
    requests.get(url1)

    # Get in Json
    json1 = requests.get(url1).json()

    # 총건수 (추출건수가 아니라 공공db에 저장되어 있는 건수) - 미구현
    # json1['SPOP_FORN_LONG_RESD_JACHI']['list_total_count']

    # 데이터 (추출데이터)
    raw1 = json1['SPOP_FORN_LONG_RESD_JACHI']['row']

    # 데이터프레임으로 변경
    raw1 = pd.DataFrame(json1['SPOP_FORN_LONG_RESD_JACHI']['row'])
    raw1.head()

    # 1 ~ 5 & 6 ~ 10 데이터 가져오고 합병하기
    startnum = 51
    endnum = 100
    url2 = f'http://openapi.seoul.go.kr:8088/{apikey}/json/SPOP_FORN_LONG_RESD_JACHI/{startnum}/{endnum}/{pre_7_dt}'
    json2 = requests.get(url2).json()
    raw2 = pd.DataFrame(json2['SPOP_FORN_LONG_RESD_JACHI']['row'])

    # data merge
    data = pd.concat([raw1,raw2])

    # 인덱스 재배열
    data.reset_index(drop=False)
    
    
    
    data.insert(0,'strd_dt',strd_dt)
    data['ins_dt'] = ins_dt   

    # 인덱스 삭제(실제로는 열로 변환됨)
    df = data.reset_index(drop=True)

    # 컬럼정의
    df.columns = ['strd_dt','stdr_de_id','tmzon_pd_se','adstrd_code_se','tot_lvpop_co','china_staypop_co','etc_staypop_co','ins_dt']

    # 인덱스컬럼 삭제
    # del df['index']

    # print(df.info())
        
    # print(df)
    
    save_data(df.to_dict('records'), SeoulApiSpopFornLongResdJachi)  

    # 데이터 정보
    # data.info

    # 엑셀로 저장
    # data.to_excel('for_pop.xlsx', index=False)
    
    # print(data)
    
    # print(raw1)
    # print('----')
    # print(raw2)
    
    # print('env_테스트')
    
    logger.info('--11 [run_api_jeju_seoul_api_runfloating_population] End !!')         
    print('\n\n')    
    
# seoul_api_run()