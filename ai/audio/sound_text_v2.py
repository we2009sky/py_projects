"""极速版翻译更快更准确, 直接HTTP请求，未使用Airspeech cient"""
# encoding=utf8
import time
import base64
import json
import requests

TOKEN_URL = 'http://openapi.baidu.com/oauth/2.0/token'
API_KEY = 'dkFrntdS3E9VIPc4ZK8pv9kg'
SECRET_KEY = 'KVsrMNlsihOrMvkppZQGsWRrcsV34Nsr'

# 极速版
DEV_PID = 80001
ASR_URL = 'http://vop.baidu.com/pro_api'
SCOPE = 'brain_enhanced_asr'  # 有此scope表示有极速版能力，没有请在网页里开通极速版

# 标准版
# DEV_PID = 1537
# ASR_URL = 'http://vop.baidu.com/server_api'
# SCOPE = 'audio_voice_assistant_get'  # 有此scope表示有asr能力，没有请在网页里勾选，非常旧的应用可能没有

AUDIO_FILE = 'test.pcm'  # 文件后缀只支持 pcm/wav/amr 格式，极速版额外支持m4a 格式
FORMAT = AUDIO_FILE[-3:]
CUID = '123456PYTHON'
# CUID = '3E-A0-BB-C6-E9-1A'
RATE = 16000  # 固定值


def fetch_token():
    params = {'grant_type': 'client_credentials',
              'client_id': API_KEY,
              'client_secret': SECRET_KEY}
    res = requests.post(TOKEN_URL, params)
    result = res.json()
    if 'access_token' in result.keys() and 'scope' in result.keys():
        if SCOPE and (not SCOPE in result['scope'].split(' ')):  # SCOPE = False 忽略检查
            raise Exception('scope is not correct')
        print('SUCCESS WITH TOKEN: %s  EXPIRES IN SECONDS: %s' % (result['access_token'], result['expires_in']))
        return result['access_token']
    else:
        raise Exception('MAYBE API_KEY or SECRET_KEY not correct: access_token or scope not found in token response')


if __name__ == '__main__':
    start = time.time()
    token = fetch_token()
    speech_data = []
    with open(AUDIO_FILE, 'rb') as speech_file:
        speech_data = speech_file.read()

    length = len(speech_data)
    if length == 0:
        raise Exception('file %s length read 0 bytes' % AUDIO_FILE)
    speech = base64.b64encode(speech_data)
    speech = str(speech, 'utf-8')
    params = {'dev_pid': DEV_PID,
              # "lm_id" : LM_ID,    #测试自训练平台开启此项
              'format': FORMAT,
              'rate': RATE,
              'token': token,
              'cuid': CUID,
              'channel': 1,
              'speech': speech,
              'len': length
              }
    post_data = json.dumps(params)
    headers = {'content-type': 'application/json'}
    res = requests.post(ASR_URL, post_data, headers=headers).json()
    print('耗时:[{}]'.format(time.time() - start))
    print('识别结果为:{}'.format(res.get('result')[0]))

    # with open("result.txt","w") as of:
    #     of.write(result_str)
