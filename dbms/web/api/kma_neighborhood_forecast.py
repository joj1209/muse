# weather.py
import json
import requests
from urllib.request import urlopen
import pandas as pd
import time
import logging
from dbms.common import config
from dbms.common.common_func import save_data
from dbms.models.api_models import KmaNeighborhoodWeather

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
def run_api_kma_neighborhood_forecast():
    
    logger.info('--09 [run_api_kma_neighborhood_forecast] Start !!')         
    
    strd_dt = time.strftime(('%Y%m%d'))
    ins_dt = time.strftime(('%Y%m%d%H%M%S'))

    """
    # 초단기실황조회
    authKey	    인증키	            100 	1	인증키(URL Encode)	공공데이터포털에서 발급받은 인증키
    numOfRows	한 페이지 결과 수	   4 	 1	10	                한 페이지 결과 수Default: 10
    pageNo	    페이지 번호	           4	1	1	                페이지 번호 Default: 1
    dataType	응답자료형식	       4 	0	XML	                요청자료형식(XML/JSON) Default: XML
    base_date	발표일자	           8	1	20210628	        ‘21년 6월 28일 발표
    base_time	발표시각	           4	1	0600	            06시 발표(정시단위) -매시각 40분 이후 호출
    """

    # 도메인은 고정
    domain = "https://apihub.kma.go.kr/api/typ02/openApi/VilageFcstInfoService_2.0/getUltraSrtNcst?"
    
    # API_KEY
    API_KEY = config.API_KEY

    # 페이지 번호(pageNo)
    page_no = 1

    # 한 페이지 결과 수(numOfRows)
    num_rows = 10

    # base_date, base_time
    base_date, base_time = strd_dt, '0600'
    
    # nx, ny
    nx, ny = 55, 127    

    # api_url = "https://apihub.kma.go.kr/api/typ02/openApi/VilageFcstInfoService_2.0/getUltraSrtNcst?authKey=nBUFejf4RvmVBXo3-Pb56A&dataType=JSON&numOfRows=10&pageNo=1&base_date=20240827&base_time=0600&nx=55&ny=127"
    api_url = f"{domain}authKey={API_KEY}&dataType=JSON&numOfRows={num_rows}&pageNo={page_no}&base_date={base_date}&base_time={base_time}&nx={nx}&ny={ny}"
    
    with urlopen (api_url) as I:
        html_bytes = I.read ()
        html = html_bytes.decode('utf-8')

    json_object = json.loads(html)
    
    # 데이터프레임으로 변환
    df = pd.DataFrame(json_object['response']['body']['items']['item'])

    df.insert(0,'strd_dt',strd_dt)
    df['ins_dt'] = ins_dt   

    # 인덱스 삭제(실제로는 열로 변환됨)
    df = df.reset_index(drop=True)

    # 컬럼정의
    df.columns = ['index','strd_dt','strd_tm','category','nx','ny','obsr_value', 'ins_dt']

    # 인덱스컬럼 삭제
    del df['index']

    save_data(df.to_dict('records'), KmaNeighborhoodWeather)

    logger.info('--09 [run_api_kma_neighborhood_forecast] End !!')         
    print('\n\n')        


















