import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, dump, ElementTree
import pandas as pd
import ssl
import json
import urllib
import chardet
import urllib3

urllib3.disable_warnings()

ssl._create_default_https_context = ssl._create_unverified_context

ccbaCtcd_list = ['11']
rsac_gut_fstt_ogidNm_list = ['서울소방재난본부']
rcpt_ym = '202312'
fire = []
total_df = pd.DataFrame()

service_key = 'wZGYpzXWq52dGL%2BPdY4haekI7B%2FfMs8HaYjX0EWeoQn8dO3g3mES8Z5nHbEIJFpImMOtOoX2OjrXbAaAZghFIw%3D%3D'

for rsac_gut_fstt_ogidNm in  rsac_gut_fstt_ogidNm_list:

    # ap_svc1 = 'uddi:19c0c9ab-ac89-486b-b4b8-b026506dc3fa'    
    # url = f"https://api.odcloud.kr/api/15111391/v1/{ap_svc1}?page=1&perPage=10&returnType=XML&serviceKey={service_key}"
    
    ap_svc1 = 'uddi:41944402-8249-4e45-9e9d-a52d0a7db1cc'    
    start_row = 1
    end_row = 1000
    
    while True:
        print(f'Start:{start_row}')
        print(f'End  :{end_row}')
        url = f"https://api.odcloud.kr/api/15111389/v1/{ap_svc1}?page={start_row}&perPage={end_row}&serviceKey={service_key}"

        response = requests.get(url,  verify=False)
        print(response)

        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            # print(soup)

        else : 
            print(response.status_code)

        json_object = json.loads(soup.text) 
        
        df = pd.DataFrame(json_object['data'])
            
        total_df = pd.concat([df,total_df])
        
        # break

        # Origin        
        # if len(df) < 1000:
        #     print('len_df : ',len(df))
        #     break
        # else:
        #     start_row = end_row + 1
        #     end_row += 1000
            
        if len(df) < 1000:
            print('len_df : ',len(df))
            break
        else:
            start_row = start_row + 1
    
    
print(total_df)
        
total_df.to_excel(f"animal_1_{rcpt_ym}.xlsx")    
        
        
        