import requests
import re
import time
import logging
from dbms.common import config
from dbms.common.common_func import save_data
from dbms.models.api_models import BlogKeword

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
class NaverSearchApi():    

    def call_api(self, keyword, start=1, display=10):
        
        X_NAVER_CLIENT_ID = config.X_NAVER_CLIENT_ID
        X_NAVER_CLIENT_SECRET = config.X_NAVER_CLIENT_SECRET
        
        url = f"{self.api_url}?query={keyword}&start={start}&display={display}"
        res = requests.get(url, headers={"X-Naver-Client-Id": X_NAVER_CLIENT_ID,
                                        "X-Naver-Client-Secret":X_NAVER_CLIENT_SECRET})
        r = res.json()
        
        return r

    def get_paging_call(self,keyword, quantity):
        if quantity > 1100:
            exit("Error 최대 요청할 수 있는 건수는 1100건 입니다")

        repeat = quantity // 100
        display = 100

        if quantity < 100:
            display = quantity
            repeat = 1

        result = []

        for i in range(repeat):
            start = i * 100 + 1
            print(f"     {i + 1}번 반복 합니다. start:{start} ")

            if start > 1000:
                start = 1000
            r = self.call_api(keyword, start=start, display=display)
            # print(r['items'][0])
            result += r['items']
        return result

    def blog(self,keyword,quantity=100):
        self.api_url = "https://openapi.naver.com/v1/search/blog.json"
        return self.get_paging_call(keyword,quantity)

    def news(self,keyword,quantity=100):
        self.api_url = "https://openapi.naver.com/v1/search/news.json"
        return self.call_api(keyword,quantity)

    def webkr(self, keyword, quantity=100):
        self.api_url = "https://openapi.naver.com/v1/search/webkr.json"
        return self.get_paging_call(keyword, quantity)
    
    def run_crawl_naver_blog_seek(self):

        logger.info('--04 [run_crawl_naver_blog_seek] Start !!')         
        
        r = self.webkr("시흥대야역맛집",20)
        strd_dt = time.strftime(('%Y%m%d'))
        ins_dt = time.strftime(('%Y%m%d%H%M%S'))

        df_dic = []
        for i in range(5):
            # print(r[i]['description'])
            title = re.sub("(<b>|</b>|'|#|시흥대야역|시흥대야|맛집)","",r[i]['description'])[:20]
            link = r[i]['link']
            row = {'strd_dt':strd_dt, 'keword':'시흥대야역맛집', 'title':title, 'link':link, 'ins_dt':ins_dt}
            df_dic.append(row)

        save_data(df_dic, BlogKeword)
        
        logger.info('--04 [run_crawl_naver_blog_seek] End !!')         
        print('\n\n')        
