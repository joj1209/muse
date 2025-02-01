import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, dump, ElementTree
import pandas as pd
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

ccbaCtcd_list = ['11']
foreigners = []

service_key = 'wZGYpzXWq52dGL%2BPdY4haekI7B%2FfMs8HaYjX0EWeoQn8dO3g3mES8Z5nHbEIJFpImMOtOoX2OjrXbAaAZghFIw%3D%3D'

for ccbaCtcd_l in  ccbaCtcd_list:

    url = f"https://apis.data.go.kr/1741000/ForeignLocalGovernmentsYear/getForeignLocalGovernmentsYear?ServiceKey={service_key}&pageNo=1&numOfRows=100"

    # print(url)


    response = requests.get(url,  verify=False)
    print(response)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'xml')
        # print(soup)

    else : 
        print(response.status_code)
        
    doc = ET.fromstring(str(soup)) # object 형태로 데이터를 반환
    iter_elem = doc.iter(tag="data") # Creates a tree iterator with the current element as the root.

    cnt = 1 # 진행상황 확인을 위한 cnt 선언
    
    print('iter_elem:',iter_elem)

    for elem in iter_elem:
        # print('elem[seq]:',elem.find('seq').text)
        # 파라미터 값에 접근할때 전부 소문자임을 주의
        foreigner = {} # 딕셔너리에 키와 벨류 형태로 문화재 목록 정보를 담는다.
        foreigner['연도'] = elem.find('wrttimeid').text
        foreigner['합계'] = elem.find('tot').text
        foreigner['서울'] = elem.find('seoul').text
        foreigner['부산'] = elem.find('busan').text
        foreigner['대구'] = elem.find('daegu').text
        foreigner['인천'] = elem.find('incheon').text
        foreigner['광주'] = elem.find('gwangju').text
        foreigner['대전'] = elem.find('daejeon').text
        foreigner['울산'] = elem.find('ulsan').text
        foreigner['세종'] = elem.find('sejong').text        
        foreigner['경기'] = elem.find('gyeonggi').text
        foreigner['강원'] = elem.find('gangwon').text
        foreigner['충북'] = elem.find('chungbuk').text
        foreigner['충남'] = elem.find('chungnam').text
        foreigner['전북'] = elem.find('jeonbuk').text
        foreigner['전남'] = elem.find('jeonnam').text
        foreigner['경북'] = elem.find('gyeongbuk').text
        foreigner['경남'] = elem.find('gyeongnam').text
        foreigner['제주'] = elem.find('jeju').text
        foreigners.append(foreigner) # 문화재 1개의 필요 파라미터 값들을 모두 딕셔너리에 담는 것을 완료한 후, foreigners 배열에 담아준다.

print(foreigners)

# if cnt % 1000 == 0:
#     print(cnt)
# cnt+=1
# print(page, " 전체목록 완료")    


df = pd.DataFrame(foreigners)
df.to_excel("foreigners.xlsx")