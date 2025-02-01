from PyKakao import Karlo
from PIL import Image
import requests
import io
import base64
import time
from dbms.common import config
from dbms.models.api_models import KakaoAiImage
from dbms.common.common_func import save_data

# 이미지 생성 및 파일저장
def urlToSave(input_text,api):
    # 프롬프트에 사용할 제시어
    text = input_text

    # 이미지 생성하기 REST API 호출
    img_dict = api.text_to_image(text, 1)

    # 생성된 이미지 정보
    # img_str = img_dict.get("images")[0].get('image')

    ## url='https://www.urbanbrush.net/web/wp-content/uploads/edd/2018/06/web-20180604115825983772.png'
    ## url='https://mk.kakaocdn.net/dna/karlo/image/2024-07-24/13/c98d1caf-2d07-47b8-bf72-3673878214d6.webp?credential=smxRqiqUEJBVgohptvfXS5JoYeFv4Xxa&expires=1721797449&signature=jI21qDrMq%2BP8xD1fKhVdIH2NWbQ%3D'
    # url = img_str
    # r = requests.get(url, stream=True).raw

    # 이미지를 파일로 생성
    # img = Image.open(r)
    
    # img.show()
    # img.save('./dbms/static/image/test1.png')

def transImage(api):
    # 이미지 파일 불러오기
    img = Image.open('./dbms/static/image/test1.png')

    # 이미지를 Base64 인코딩하기
    img_base64 = api.image_to_string(img)

    # 이미지 변환하기 REST API 호출
    response = api.transform_image(image=img_base64)

    # 응답의 첫 번째 이미지 생성 결과 출력하기
    result = api.string_to_image(response.get("images")[0].get("image"), mode='RGB')

# (미사용)Base64 인코딩 함수
def imageToString(img):
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    my_encoded_img = base64.encodebytes(img_byte_arr.getvalue()).decode('ascii')
    return my_encoded_img

# (미사용)Base64 디코딩 및 이미지 변환 함수
def stringToImage(base64_string, mode='RGBA'):
    imgdata = base64.b64decode(str(base64_string))
    img = Image.open(io.BytesIO(imgdata)).convert(mode)
    return img

# index.py에서 실행
def run_api_kakao_ai_image():
    print('--06 [run_api_kakao_ai_image] Start !!')
    
    SERVICE_KEY = config.SERVICE_KEY    
    api = Karlo(service_key=SERVICE_KEY)
    strd_dt = time.strftime(('%Y%m%d'))
    ins_dt = time.strftime(('%Y%m%d%H%M%S'))

    """ text 예시어
    text = "Cute magical flyng cat, soft golden fur, fantasy art drawn by Pixar concept artist, Toy Story main character, clear and bright eyes, sharp nose"
    """    
    input_text = "Antique and artistic Pixar-like, magical space"
    urlToSave(input_text, api)
        
    # df_dic = [{"strd_dt":strd_dt, "suggest_word":input_text,  "ins_dt":ins_dt}]

    # save_data(df_dic, KakaoAiImage)
    
    print('--06 [run_api_kakao_ai_image] End !!')        
