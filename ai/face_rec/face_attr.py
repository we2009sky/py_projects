"""人脸检测与属性分析"""
# encoding=utf8
import requests
import base64
import json
from aip import AipFace

API_KEY = 'f7pnKUZXu7A2yHKDaorvMCM3'
SECRET_KEY = 'oBISsLcI4T5bucaswTwj0XpVpXYyBaxQ'
REQUEST_URL = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
TOKEN_URL = 'https://aip.baidubce.com/oauth/2.0/token'


def fetch_token(api_key, secret_key, ):
    params = {'grant_type': 'client_credentials',
              'client_id': api_key,
              'client_secret': secret_key}
    res = requests.post(TOKEN_URL, params)
    result = res.json()
    if 'access_token' in result.keys() and 'scope' in result.keys():
        print('SUCCESS WITH TOKEN: %s  EXPIRES IN SECONDS: %s' % (result['access_token'], result['expires_in']))
        return result['access_token']
    else:
        raise Exception('MAYBE API_KEY or SECRET_KEY not correct: access_token or scope not found in token response')


with open('test.jpg', 'rb') as f:
    data = f.read()
speech = str(base64.b64decode(data))
params = {"image": speech,
          "image_type": "FACE_TOKEN",
          "face_field": "faceshape"}
params = json.dumps(params)

access_token = fetch_token(API_KEY, SECRET_KEY)
request_url = REQUEST_URL + "?access_token=" + access_token
headers = {'content-type': 'application/json'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print(response.json())
