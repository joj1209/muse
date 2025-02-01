from django.db import models


# 01.네이버증권
class NaverFinance(models.Model):

    strd_dt = models.CharField(max_length=8, help_text="기준일자")
    stock_cd = models.CharField(max_length=10, help_text="종목코드")
    stock_nm = models.CharField(max_length=500, help_text="종목명")
    pre_price = models.CharField(max_length=500, help_text="전일가")
    today_price = models.CharField(max_length=500, help_text="현재가")
    trading_volume = models.CharField(max_length=500, help_text="거래량")
    ins_dt = models.CharField(max_length=500, help_text="입력일시")

    class Meta:
        db_table = 'dbms_naver_finance'
        

# 02.전기차보조금
class EvCarPortal(models.Model):
    
    strd_dt = models.CharField(max_length=8, help_text="기준일자")
    sido_nm = models.CharField(max_length=500, help_text="시도명")
    region = models.CharField(max_length=500, help_text="지역명")
    receipt_way = models.CharField(max_length=500, help_text="접수방법")
    receipt_priority = models.CharField(max_length=500, help_text="접수순위")
    value = models.CharField(max_length=500, help_text="보급대수")
    ins_dt = models.CharField(max_length=500, help_text="입력일시")

    class Meta:
        db_table = 'dbms_ev_car_portal'    
        

# 03.FinanceData.KR
class MarketStock(models.Model):
    
    strd_dt = models.CharField(max_length=8, help_text="기준일자")
    market = models.CharField(max_length=500, help_text="마켓")
    stock_day = models.DateField(help_text="주식일자")
    opening_price = models.FloatField(help_text="시가")
    high_price = models.FloatField(help_text="고가")
    low_price = models.FloatField(help_text="저가")
    closing_price = models.FloatField(help_text="종가")
    volume = models.FloatField(help_text="거래량")
    ins_dt = models.CharField(max_length=500, help_text="입력일시")

    class Meta:
        db_table = 'dbms_market_stock'
        
        
# 04.네이버블러그
class BlogKeword(models.Model):
    
    strd_dt = models.CharField(max_length=8, help_text="기준일자")
    keword = models.CharField(max_length=500, help_text="검색어")
    title = models.CharField(max_length=500,help_text="제목")
    link = models.CharField(max_length=500,help_text="링크")
    ins_dt = models.CharField(max_length=500, help_text="입력일시")

    class Meta:
        db_table = 'dbms_blog_keword'     
        

# 05.유투브        
class YoutubeKeword(models.Model):
    
    strd_dt = models.CharField(max_length=8, help_text="기준일자")
    keword = models.CharField(max_length=500, help_text="검색어")
    link = models.CharField(max_length=500,help_text="링크")
    video_id = models.CharField(max_length=500,help_text="비디오ID")
    main_text = models.CharField(max_length=500,help_text="본문")    
    comment_author = models.CharField(max_length=500,help_text="댓글작성자")
    ins_dt = models.CharField(max_length=500, help_text="입력일시")

    class Meta:
        db_table = 'dbms_youtube_keword'           
        

# 06.Kakao
class KakaoAiImage(models.Model):
    
    strd_dt = models.CharField(max_length=8, help_text="기준일자")
    suggest_word = models.CharField(max_length=500, help_text="제시어")
    ins_dt = models.CharField(max_length=500, help_text="입력일시")

    class Meta:
        db_table = 'dbms_kakao_ai_image'         
        
        
# 07.KakaoTalk
class KakaoTalk(models.Model):
    
    strd_dt = models.CharField(max_length=8, help_text="기준일자")
    access_token = models.CharField(max_length=500, help_text="접근토큰")
    token_type = models.CharField(max_length=500, help_text="토큰타입")
    refresh_token = models.CharField(max_length=500, help_text="갱신토큰")
    scope = models.CharField(max_length=500, help_text="접근범위")
    upd_dt = models.CharField(max_length=50, help_text="변경일시")
    ins_dt = models.CharField(max_length=50, help_text="입력일시")

    class Meta:
        db_table = 'dbms_kakao_talk' 
        

# 08.공공데이터포털
class PublicAptTrade(models.Model):
    
    strd_dt = models.CharField(max_length=8, help_text="기준일자")
    sgg_cd = models.CharField(max_length=500, help_text="법정동시군구코드")
    road_nm = models.CharField(max_length=500, help_text="도로명")
    apt_nm = models.CharField(max_length=500, help_text="아파트명")
    excul_use_area = models.CharField(max_length=500, help_text="전용면적")
    deal_year = models.CharField(max_length=50, help_text="계약년도")
    deal_amount = models.CharField(max_length=50, help_text="거래금액(만원)")
    floor = models.CharField(max_length=50, help_text="층")
    build_year = models.CharField(max_length=50, help_text="건축년도")
    seller_gubun = models.CharField(max_length=50, help_text="매도자구분")
    buyer_gubun = models.CharField(max_length=50, help_text="매수자구분")
    ins_dt = models.CharField(max_length=50, help_text="입력일시")

    class Meta:
        db_table = 'dbms_public_apt_trade' 
        
        
# 09.기상청자료개방포털
class KmaNeighborhoodWeather(models.Model):
    
    strd_dt = models.CharField(max_length=8, help_text="기준일자")
    strd_tm = models.CharField(max_length=500, help_text="기준시간")
    category = models.CharField(max_length=500, help_text="카테고리")
    nx = models.CharField(max_length=500, help_text="예보지점X좌표")
    ny = models.CharField(max_length=500, help_text="예보지점Y좌표")
    obsr_value = models.CharField(max_length=50, help_text="강수량")
    ins_dt = models.CharField(max_length=50, help_text="입력일시")

    class Meta:
        db_table = 'dbms_kma_neighborhood_forecast'
        
 
 # 10.제주데이터허브
class JejuApiFloatingPopulation(models.Model):
    
    strd_dt = models.CharField(max_length=8, help_text="기준일자")
    regist_dt = models.CharField(max_length=8, help_text="등록일자")
    city = models.CharField(max_length=500, help_text="시군구")
    emd = models.CharField(max_length=500, help_text="읍면동")
    gender = models.CharField(max_length=500, help_text="성별")
    age_group = models.CharField(max_length=500, help_text="연령대")
    resd_pop = models.CharField(max_length=50, help_text="거주인구")
    work_pop = models.CharField(max_length=50, help_text="근무인구")
    visit_pop = models.CharField(max_length=50, help_text="방문자수")
    ins_dt = models.CharField(max_length=50, help_text="입력일시")

    class Meta:
        db_table = 'dbms_jeju_api_floating_population'
        
# 11.서울시공공데이터API : 자치구 단위 서울생활인구(장기체류 외국인)        
class SeoulApiSpopFornLongResdJachi(models.Model):
    
    strd_dt = models.CharField(max_length=8, help_text="기준일자")
    stdr_de_id = models.CharField(max_length=500, help_text="기준일ID")
    tmzon_pd_se = models.CharField(max_length=500, help_text="시간대구분")
    adstrd_code_se = models.CharField(max_length=500, help_text="자치구코드")
    tot_lvpop_co = models.CharField(max_length=500, help_text="총생활인구수")
    china_staypop_co = models.CharField(max_length=500, help_text="중국인체류인구수")
    etc_staypop_co = models.CharField(max_length=500, help_text="중국외외국인체류인구수")
    ins_dt = models.CharField(max_length=50, help_text="입력일시")

    class Meta:
        db_table = 'dbms_seoul_api_spop_forn_long_resd_jachi'  
        
        
# API 통계
class ApiDataSum(models.Model):
    
    strd_dt = models.CharField(max_length=8, help_text="기준일자")
    api_nm = models.CharField(max_length=500, help_text="API명")
    data_gb = models.CharField(max_length=50, help_text="API데이터구분")
    data_cnt = models.FloatField(help_text="적재건수")
    memo = models.CharField(max_length=500, help_text="메모")
    ins_dt = models.CharField(max_length=50, help_text="입력일시")

    class Meta:
        db_table = 'td_dbms_api_s'  
