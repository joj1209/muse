from django.shortcuts import render
from dbms.models import NaverFinance
from dbms.web.crawler.naver_finance import run_crawl_naver_finance

import requests



def index_naver(request):
    run_crawl_naver_finance()
    
    board_list = NaverFinance.objects.all().order_by('-id')
    context = {
        'board_list':board_list,
    }
    
    return render(request, 'dbms/index_naver.html', context)

def list(request):
    board_list = NaverFinance.objects.all().order_by('-id')
    context = {
        'board_list':board_list,
    }
    return render(request, 'dbms/list.html', context)