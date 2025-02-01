import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, dump, ElementTree
import pandas as pd
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

ccbaCtcd_list = ['11']
rsac_gut_fstt_ogidNm_list = ['서울소방재난본부','인천소방본부','부산소방안전본부','대구소방안전본부','대전소방본부','광주소방안전본부','울산소방본부','경기소방재난본부','경기북부소방재난본부','강원소방본부','충남소방본부','충북소방본부','경남소방본부','경북소방본부','전남소방본부','전북소방본부','제주소방안전본부','창원소방본부','세종소방본부']
rcpt_ym = '202312'
fire = []

service_key = 'wZGYpzXWq52dGL%2BPdY4haekI7B%2FfMs8HaYjX0EWeoQn8dO3g3mES8Z5nHbEIJFpImMOtOoX2OjrXbAaAZghFIw%3D%3D'

for rsac_gut_fstt_ogidNm in  rsac_gut_fstt_ogidNm_list:

    ap_svc1 = 'getEmgDispatchResultStats'   # 소방청 구급통계 교통사고구급활동현황 목록조회
    url = f"http://apis.data.go.kr/1661000/EmergencyStatisticsService/{ap_svc1}?ServiceKey={service_key}&pageNo=1&numOfRows=1000&resultType=xml&sidoHqOgidNm={rsac_gut_fstt_ogidNm}&rcptYm={rcpt_ym}"

    response = requests.get(url,  verify=False)
    print(response)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'xml')
        # print(soup)

    else : 
        print(response.status_code)
        
    doc = ET.fromstring(str(soup)) # object 형태로 데이터를 반환
    iter_elem = doc.iter(tag="item") # Creates a tree iterator with the current element as the root.

    cnt = 1 # 진행상황 확인을 위한 cnt 선언
    
    print('iter_elem:',iter_elem)

    for elem in iter_elem:
        # print('elem[seq]:',elem.find('seq').text)
        # 파라미터 값에 접근할때 전부 소문자임을 주의
        foreigner = {} # 딕셔너리에 키와 벨류 형태로 문화재 목록 정보를 담는다.
        foreigner['시도본부'] = elem.find('sidoHqOgidNm').text
        foreigner['출동소방서'] = elem.find('rsacGutFsttOgidNm').text
        foreigner['접수년월'] = elem.find('rcptYm').text
        foreigner['출동건수'] = elem.find('gutCo').text
        foreigner['이송건수'] = elem.find('trnfCo').text
        foreigner['이송환자수'] = elem.find('trnfPcnt').text
        foreigner['출동유형'] = elem.find('gutTyCdNm').text
        fire.append(foreigner) # 문화재 1개의 필요 파라미터 값들을 모두 딕셔너리에 담는 것을 완료한 후, fire 배열에 담아준다.

print(fire)

# if cnt % 1000 == 0:
#     print(cnt)
# cnt+=1
# print(page, " 전체목록 완료")    


df = pd.DataFrame(fire)
df.to_excel(f"fire_emg_{rcpt_ym}.xlsx")