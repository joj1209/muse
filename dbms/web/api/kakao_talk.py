import pendulum
import json
import requests
import time
import logging
from dbms.common.common_func import save_data
from dbms.models.api_models import KakaoTalk
from dbms.common import config

REDIRECT_URL = 'https://example.com/oauth'
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def _refresh_token_to_variable():
    CLIENT_ID = config.KAKAO_CLIENT_SECRET
    
    # kakao_tokens = {'access_token': 'eYutRoeX3tx3sCUdl8nf0ejrSEK5Z6ZDAAAAAQo9cpcAAAGRJiI9ExKZRqbpl2cW', 'token_type': 'bearer', 'refresh_token': 'KKRo8uPXDwtfsqfYbYIVhDKD66LQcpMqAAAAAgoqJZEAAAGRIXvvxBKZRqbpl2cW', 'expires_in': 21599, 'scope': 'talk_message', 'refresh_token_expires_in': 5183999, 'updated': '2024-08-06 14:21:03'}
    kakao_tokens = {'access_token': 'kTQblwxUOhTLy8ulPH6QkuoH4-jbKAOkAAAAAQorDKYAAAGTTZBoqRKZRqbpl2cW', 'token_type': 'bearer', 'refresh_token': 'pafE8bvTrhPnibRW3_D-yW4nR5IxHwvQAAAAAgorDKYAAAGTTZBopxKZRqbpl2cW', 'expires_in': 21599, 'scope': 'talk_message', 'refresh_token_expires_in': 5183999, 'updated': '2024-08-06 14:21:03'}
    tokens = kakao_tokens
    refresh_token = tokens.get('refresh_token')
    url = "https://kauth.kakao.com/oauth/token"
    
    data = {
        "grant_type": "refresh_token",
        "client_id": CLIENT_ID,
        "refresh_token": f"{refresh_token}"
    }
    
    response = requests.post(url, data=data)
    rslt = response.json()
    new_access_token = rslt.get('access_token')
    new_refresh_token = rslt.get('refresh_token')         # Refresh 토큰 만료기간이 30일 미만이면 refresh_token 값이 포함되어 리턴됨.
    
    if new_access_token:
        tokens['access_token'] = new_access_token
    if new_refresh_token:
        tokens['refresh_token'] = new_refresh_token

    now = pendulum.now('Asia/Seoul').strftime('%Y-%m-%d %H:%M:%S')
    tokens['updated'] = now
    # print(f'kakao_tokens "{tokens}"')
    print('     variable 업데이트 완료(key: kakao_tokens)')

    return tokens

def send_kakao_msg(talk_title: str, content: dict):
    # kakao_tokens = {'access_token': 'eYutRoeX3tx3sCUdl8nf0ejrSEK5Z6ZDAAAAAQo9cpcAAAGRJiI9ExKZRqbpl2cW', 'token_type': 'bearer', 'refresh_token': 'KKRo8uPXDwtfsqfYbYIVhDKD66LQcpMqAAAAAgoqJZEAAAGRIXvvxBKZRqbpl2cW', 'expires_in': 21599, 'scope': 'talk_message', 'refresh_token_expires_in': 5183999, 'updated': '2024-08-06 14:21:03'}
    kakao_tokens = {'access_token': 'kTQblwxUOhTLy8ulPH6QkuoH4-jbKAOkAAAAAQorDKYAAAGTTZBoqRKZRqbpl2cW', 'token_type': 'bearer', 'refresh_token': 'pafE8bvTrhPnibRW3_D-yW4nR5IxHwvQAAAAAgorDKYAAAGTTZBopxKZRqbpl2cW', 'expires_in': 21599, 'scope': 'talk_message', 'refresh_token_expires_in': 5183999, 'updated': '2024-08-06 14:21:03'}
    try_tokens = {}
    try_cnt = 0
    try_tokens_exits = 0
    
    while True:
        ### get Access 토큰
        if try_tokens_exits == 0:
            tokens = kakao_tokens
        else:
            tokens = try_tokens    
            
        access_token = tokens.get('access_token')
        content_lst = []
        button_lst = []

        for title, msg in content.items():
            content_lst.append({
                'title': f'{title}',
                'description': f'{msg}',
                'image_url': '',
                'image_width': 40,
                'image_height': 40,
                'link': {
                    'web_url': '',
                    'mobile_web_url': ''
                }
            })
            button_lst.append({
                'title': '',
                'link': {
                    'web_url': '',
                    'mobile_web_url': ''
                }
            })

        list_data = {
            'object_type': 'list',
            'header_title': f'{talk_title}',
            'header_link': {
                'web_url': '',
                'mobile_web_url': '',
                'android_execution_params': 'main',
                'ios_execution_params': 'main'
            },
            'contents': content_lst,
            'buttons': button_lst
        }

        send_url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
        headers = {
            "Authorization": f'Bearer {access_token}'
        }
        data = {'template_object': json.dumps(list_data)}
        response = requests.post(send_url, headers=headers, data=data)
        print(f'     try횟수: {try_cnt}, reponse 상태:{response.status_code}')
        try_cnt += 1

        if response.status_code == 200:         # 200: 정상
            return response.status_code,kakao_tokens
        elif response.status_code == 400:       # 400: Bad Request (잘못 요청시), 무조건 break 하도록 return
            return response.status_code,kakao_tokens
        elif response.status_code == 401 and try_cnt <= 2:      # 401: Unauthorized (토큰 만료 등)
            try_tokens = _refresh_token_to_variable()
            try_tokens_exits = 1
        elif response.status_code != 200 and try_cnt >= 3:      # 400, 401 에러가 아닐 경우 3회 시도때 종료
            return response.status_code
        
    return '1'

def run_api_kakao_talk():
    logger.info('--07 [run_api_kakao_talk] Start !!')         
    
    '''
    content:{'tltle1':'content1', 'title2':'content2'...}
    '''    
    title1 = "run_api_kakao_talk1"
    title2 = "run_api_kakao_talk2"
    content1 = "카카오API로 나에게 카톡전송1!!"
    content2 = "카카오API로 나에게 카톡전송2!!"
    talk_title = "카카오톡 전송"
    strd_dt = time.strftime(('%Y%m%d'))
    ins_dt = time.strftime(('%Y%m%d%H%M%S'))
    
    content = {f'{title1}': f'{content1}', f'{title2}': f'{content2}'}
    tokens = send_kakao_msg(talk_title=f'{talk_title}',content=content)

    map = []
    for i in range(1):             
        row = {'strd_dt':strd_dt, 'access_token':tokens[1]['access_token'], 'token_type':tokens[1]['token_type'], 'refresh_token':tokens[1]['refresh_token'], 'scope':tokens[1]['scope'], 'upd_dt':tokens[1]['updated'], 'ins_dt':ins_dt}
        map.append(row)
    
    save_data(map, KakaoTalk)
    
    logger.info('--07 [run_api_kakao_talk] End !!')         
    print('\n\n')