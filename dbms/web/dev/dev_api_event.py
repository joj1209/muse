import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, dump, ElementTree
import pandas as pd

ccbaCtcd_list = ['11']
heritages = []
year = '2026'
month_list = ['01','02','03','04','05','06','07','08','09','10','11','12']

for month in month_list:

    # url = f"https://www.khs.go.kr/cha/SearchKindOpenapiList.do?pageUnit=10&ccbaCncl=N&ccbaKdcd=11&ccbaCtcd={ccbaCtcd_l}"

    url = f"http://www.khs.go.kr/cha/openapi/selectEventListOpenapi.do?pageUnit=10&searchYear={year}&searchMonth={month}"

    response = requests.get(url)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        print(soup)

    else : 
        print(response.status_code)
        
    doc = ET.fromstring(str(soup)) # object 형태로 데이터를 반환
    iter_elem = doc.iter(tag="item") # Creates a tree iterator with the current element as the root.

    cnt = 1 # 진행상황 확인을 위한 cnt 선언

    for elem in iter_elem:
        # 파라미터 값에 접근할때 전부 소문자임을 주의
        heritage = {} # 딕셔너리에 키와 벨류 형태로 문화재 목록 정보를 담는다.
        heritage['seqNo'] = elem.find('seqno').text
        heritage['siteCode'] = elem.find('sitecode').text
        heritage['subTitle'] = elem.find('subtitle').text
        heritage['subContent'] = elem.find('subcontent').text
        heritage['sDate'] = elem.find('sdate').text
        heritage['eDate'] = elem.find('edate').text
        heritage['groupName'] = elem.find('groupname').text
        heritage['contact'] = elem.find('contact').text
        heritage['subDesc'] = elem.find('subdesc').text
        heritage['subPath'] = elem.find('subpath').text
        heritage['subDesc2'] = elem.find('subdesc_2').text
        heritage['subDesc3'] = elem.find('subdesc_3').text
        heritage['mainImageTemp'] = elem.find('mainimagetemp').text
        heritage['sido'] = elem.find('sido').text
        heritage['gugun'] = elem.find('gugun').text
        heritage['subDate'] = elem.find('subdate').text
        heritages.append(heritage) # 문화재 1개의 필요 파라미터 값들을 모두 딕셔너리에 담는 것을 완료한 후, heritages 배열에 담아준다.

    print(heritages)
    print('----excel')
    df = pd.DataFrame(heritages)
    df.to_excel(f"heritages_event_{year}_{month}.xlsx")


# print(heritages)

# if cnt % 1000 == 0:
#     print(cnt)
# cnt+=1
# print(page, " 전체목록 완료")    


# df = pd.DataFrame(heritages)
# df.to_excel("heritages1.xlsx")