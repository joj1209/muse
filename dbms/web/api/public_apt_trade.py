import time
import logging
from PublicDataReader import TransactionPrice
from dbms.common import config
from dbms.models.api_models import PublicAptTrade
from dbms.common.common_func import save_data
from datetime import date, timedelta

SERVICE_KEY = config.PUBLIC_SERVICE_KEY
api = TransactionPrice(SERVICE_KEY)
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def run_api_public_apt_trade():
    logger.info('--08 [run_api_public_apt_trade] Start !!')         
        
    strd_dt = time.strftime(('%Y%m%d'))
    ins_dt = time.strftime(('%Y%m%d%H%M%S'))
    
    sigungu = "41390",    # 11650 서초구 / 41390 시흥시
    start_mm = (date.today()-timedelta(days=40)).strftime('%Y%m')
    end_mm = (date.today()-timedelta(days=40)).strftime('%Y%m')

    # 기간 내 조회
    df_tmp = api.get_data(
        property_type="아파트",
        trade_type="매매",
        sigungu_code=sigungu,    # 11650 서초구 / 41390 시흥시
        start_year_month=start_mm,
        end_year_month=end_mm,
    )

    df = df_tmp[['sggCd','roadNm','aptNm','excluUseAr','dealYear','dealAmount','floor','buildYear','slerGbn','buyerGbn']]    

    # 맨앞열에 열 추가
    df.insert(0,'strd_dt',strd_dt)
    df['ins_dt'] = ins_dt   
    
    # 컬럼정의
    df.columns = ['strd_dt','sgg_cd','road_nm','apt_nm','excul_use_area','deal_year','deal_amount','floor','build_year','seller_gubun','buyer_gubun','ins_dt']
    
    save_data(df.to_dict('records'), PublicAptTrade)
    
    logger.info('--08 [run_api_public_apt_trade] End !!')         
    print('\n\n')
