from django.http import HttpResponse
from django.shortcuts import render
from dbms.models import NaverFinance, EvCarPortal, MarketStock, BlogKeword, YoutubeKeword, KakaoAiImage, KakaoTalk, PublicAptTrade, KmaNeighborhoodWeather, JejuApiFloatingPopulation, SeoulApiSpopFornLongResdJachi, ApiDataSum
from dbms.web.crawler.naver_finance import run_crawl_naver_finance
from dbms.web.crawler.ev_og_portal import run_crawl_ev_og_portal
from dbms.web.api.finance_data_reader import FinanceDataReaderParser
from dbms.web.crawler.naver_blog_seek import NaverSearchApi
from dbms.web.crawler.google_youtube_comment import YoutubeApi
from dbms.web.api.kakao_ai_image import run_api_kakao_ai_image
from dbms.web.api.kakao_talk import run_api_kakao_talk
from dbms.web.api.public_apt_trade import run_api_public_apt_trade
from dbms.web.api.kma_neighborhood_forecast import run_api_kma_neighborhood_forecast
from dbms.web.api.jeju_floating_population import run_api_jeju_floating_population
from dbms.web.api.seoul_long_foreigner import seoul_api_run
from dbms.web.scheduler.sch_dbms_api_s import my_custom_sql
from dbms.common import utils

logger = utils.getLogger('Main.logger.Start')

# logger.info('log')
logger.debug('log')

# logger.info('log2')

def index(request):
    
    # return HttpResponse("TEst index")
    # return render(request, 'dbms/index.html')


    # # 01. Naver Fiannce
    run_crawl_naver_finance()
    
    # # 02. EV Portal
    run_crawl_ev_og_portal()
    
    # 03. FinanceDataReader
    # p = FinanceDataReaderParser()    
    # p.run_api_finance_data_reader()  
    
    # # 04. Naver API(BLOG)
    p2 = NaverSearchApi()
    p2.run_crawl_naver_blog_seek()
    
    # # # 05. Youtube API(Comment)
    p3 = YoutubeApi("A")
    p3.run_crawl_google_youtube_comment("공공데이터활용")
    
    # # # 06. Kakao AI image
    # # # run_api_kakao_ai_image()  #-->종료
    
    # # # 07. Kakao Talk Sendpy
    # run_api_kakao_talk()
    
    # # # 08. 공공데이터:아파트실거래
    run_api_public_apt_trade()
    
    # # # 09. 기상청 기상자료개방포털
    run_api_kma_neighborhood_forecast()
    
    # # # 10. 제주API : 지역별시간방문자수
    run_api_jeju_floating_population()
    
    # # # 11. 자치구 단위 서울 생활인구(장기체류 외국인)
    seoul_api_run()
    
    #-----------------------------------------------
    # 
    my_custom_sql('2024','20241126')
    
    board_list = NaverFinance.objects.all().order_by('-id')[:15]
    ev_list = EvCarPortal.objects.all().order_by('-id')[:15]
    market_list = MarketStock.objects.all().order_by('-id')[:15]
    blog_crawl_list = BlogKeword.objects.all().order_by('-id')[:15]
    youtube_comment_list = YoutubeKeword.objects.all().order_by('-id')[:15]
    kakao_ai_image = KakaoAiImage.objects.all().order_by('-id')[:5]
    kakao_talk = KakaoTalk.objects.all().order_by('-id')[:15]
    public_apt_trade = PublicAptTrade.objects.all().order_by('-id')[:15]
    kma_forecast = KmaNeighborhoodWeather.objects.all().order_by('-id')[:15]
    jeju_api_flo_pop = JejuApiFloatingPopulation.objects.all().order_by('-id')[:15]
    seoul_api_for_pop = SeoulApiSpopFornLongResdJachi.objects.all().order_by('-id')[:15]
    api_batch_list = ApiDataSum.objects.all().order_by('-id')[:15]
        
    context = {
        'board_list':board_list,
        'ev_list':ev_list,
        'market_list':market_list,
        'blog_crawl_list':blog_crawl_list,
        'youtube_comment_list':youtube_comment_list,
        'kakao_ai_image':kakao_ai_image,
        'kakao_talk':kakao_talk,
        'public_apt_trade':public_apt_trade,
        'kma_forecast':kma_forecast,
        'jeju_api_flo_pop':jeju_api_flo_pop,
        'seoul_api_for_pop':seoul_api_for_pop,
        'api_batch_list':api_batch_list,
    }
    
    # print('----1->>>>>')
    # print(seoul_api_for_pop)
    
    # print('----2->>>>>')
    # print(api_batch_list)
    
    return render(request, 'dbms/index.html', context)

logger = utils.getLogger('Main.logger.End')