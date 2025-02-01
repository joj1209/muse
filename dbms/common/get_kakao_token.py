import requests

client_id = 'aceabc7b457ce996bbc7feb914227837'
redirect_uri = 'https://example.com/oauth'
authorize_code = 'GCQ3LZ-1YVYFOSaqZ8hOx723AZ_sBg5uI-L4zcG49SmuZh8tuD1CeAAAAAQKKiWRAAABkSF7iNf7Ewsnpgvovw'


token_url = 'https://kauth.kakao.com/oauth/token'
data = {
    'grant_type': 'authorization_code',
    'client_id': client_id,
    'redirect_uri': redirect_uri,
    'code': authorize_code,
    }

response = requests.post(token_url, data=data)
tokens = response.json()
print(tokens)
print('------')
print(data)