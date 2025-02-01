import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, dump, ElementTree
import pandas as pd


ccbaCtcd_list = ['11','21','22','23','24','25','26','45','31','32','33','34','35','36','37','38','50']
heritages = []

for ccbaCtcd_l in  ccbaCtcd_list:

    url = f"https://www.khs.go.kr/cha/SearchKindOpenapiList.do?pageUnit=10&ccbaCncl=N&ccbaKdcd=11&ccbaCtcd={ccbaCtcd_l}"

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
        heritage['sn'] = elem.find('sn').text
        heritage['no'] = elem.find('no').text
        heritage['ccmaname'] = elem.find('ccmaname').text
        heritage['crltsnonm'] = elem.find('crltsnonm').text
        heritage['ccbamnm1'] = elem.find('ccbamnm1').text
        heritage['ccbamnm2'] = elem.find('ccbamnm2').text
        heritage['ccbactcdnm'] = elem.find('ccbactcdnm').text
        heritage['ccsiname'] = elem.find('ccsiname').text
        heritage['ccbaadmin'] = elem.find('ccbaadmin').text
        heritage['ccbakdcd'] = elem.find('ccbakdcd').text
        heritage['ccbactcd'] = elem.find('ccbactcd').text
        heritage['ccbaasno'] = elem.find('ccbaasno').text
        heritage['ccbacncl'] = elem.find('ccbacncl').text
        heritage['ccbacpno'] = elem.find('ccbacpno').text
        heritage['longitude'] = elem.find('longitude').text
        heritage['latitude'] = elem.find('latitude').text
        heritages.append(heritage) # 문화재 1개의 필요 파라미터 값들을 모두 딕셔너리에 담는 것을 완료한 후, heritages 배열에 담아준다.

print(heritages)

# if cnt % 1000 == 0:
#     print(cnt)
# cnt+=1
# print(page, " 전체목록 완료")    


df = pd.DataFrame(heritages)
df.to_excel("heritages.xlsx")