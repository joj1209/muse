import FinanceDataReader as fdr
import pandas as pd
import time
import datetime
import logging
from dbms.common import utils
from datetime import date, timedelta
from dbms.models.api_models import MarketStock
from dbms.common.common_func import save_data

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
class FinanceDataReaderParser():
    logger = utils.getLogger('FinanceDataReaderParser.Start')

    def __init__(self):
        # print('in self')
        # 전일자, 당일, 입력시간
        pre_dt = (date.today()-timedelta(days=1)).strftime('%Y%m%d')
        pre2_dt = (date.today()-timedelta(days=2)).strftime('%Y%m%d')
        strd_dt = time.strftime(('%Y%m%d'))
        ins_dt = time.strftime(('%Y%m%d%H%M%S'))
        week_nm = date.today().weekday()
        # print('pre_dt:'+pre_dt)
        # print('strd_dt:'+strd_dt)
        # print('ins_dt:'+ins_dt)
        # print(date.today().weekday())
        
        if week_nm == 1:
            us_pre_dt = (date.today()-timedelta(days=3)).strftime('%Y%m%d')

        # KOSPI,KRX Index 코스피 지수 데이터 
        df_kospi = fdr.DataReader('KS11',strd_dt,strd_dt)
        df_kosdaq = fdr.DataReader('KQ11',strd_dt,strd_dt)
        
        # US market Indices 미국 시장 지수 데이터:나스닥, S&P500, 다우존스
        df_nasdaq = fdr.DataReader('IXIC',pre_dt)
        df_sp500 = fdr.DataReader('S&P500',pre_dt)
        df_dji = fdr.DataReader('DJI',pre_dt)


        # 인덱스(날짜)->열로 변환
        df_kospi = df_kospi.reset_index()
        df_kosdaq = df_kosdaq.reset_index()
        df_nasdaq = df_nasdaq.reset_index()
        df_sp500 = df_sp500.reset_index()
        df_dji = df_dji.reset_index()

        # 열추가 : 기준일자, 마켓
        df_kospi.insert(0,'strd_dt',strd_dt)
        df_kospi.insert(1,'market','KOSPI')

        # print(df_kosdaq)
        df_kosdaq.insert(0,'strd_dt',strd_dt)
        df_kosdaq.insert(1,'market','KOSDAQ')

        df_nasdaq.insert(0,'strd_dt',strd_dt)
        df_nasdaq.insert(1,'market','NASDAQ')
        # print(df_nasdaq)
        df_sp500.insert(0,'strd_dt',strd_dt)
        df_sp500.insert(1,'market','S&P500')

        df_dji.insert(0,'strd_dt',strd_dt)
        df_dji.insert(1,'market','DowJones')

        # # # 행병합 : 5개 마켓
        df_total = pd.concat([df_kospi, df_kosdaq, df_nasdaq, df_sp500, df_dji])
        df_total.replace({pd.NaT: datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}, inplace=True)
        
        # # # 열삭제 : 해외지수에 없는 6개 열 삭제
        # self.df = df_total.drop(['Change','UpDown','Comp','Amount','MarCap','Adj Close','index'],axis=1)
        self.df = df_total.drop(['Adj Close'],axis=1)
        
        # # # 컬럼명 재정의
        self.df.columns = ['strd_dt','market','stock_day','opening_price','high_price','low_price','closing_price','volume']
        
        # # # 열추가 : 입력일시
        self.df['ins_dt'] = ins_dt
        # print(self.df)

    
    def run_api_finance_data_reader(self):
        
        logger.info('--03 [run_api_finance_data_reader] Start !!')

        save_data(self.df.to_dict('records'), MarketStock)
        
        logger.info('--03 [run_api_finance_data_reader] End !!')
        print('\n\n')
            
        
