# encoding=utf8

import json

import base64

import requests

from urllib.request import urlopen

from urllib.request import Request

from urllib.error import URLError

from urllib.parse import urlencode


API_KEY = 'kVcnfD9iW2XVZSMaLMrtLYIz'

SECRET_KEY = 'O9o1O213UgG5LFn0bDGNtoRN3VWl2du6'

AUDIO_FILE = 'output.wav'  # 只支持 pcm/wav/amr 格式，极速版额外支持m4a 格式

FORMAT = AUDIO_FILE[-3:]  # 文件后缀只支持 pcm/wav/amr 格式，极速版额外支持m4a 格式

CUID = '123456PYTHON'

RATE = 16000  # 固定值


# 普通版

DEV_PID = 1536  # 1537 表示识别普通话，使用输入法模型。1536表示识别普通话，使用搜索模型。根据文档填写PID，选择语言及识别模型

ASR_URL = 'http://vop.baidu.com/server_api'

SCOPE = 'audio_voice_assistant_get'  # 有此scope表示有asr能力，没有请在网页里勾选，非常旧的应用可能没有



#测试自训练平台需要打开以下信息， 自训练平台模型上线后，您会看见 第二步：“”获取专属模型参数pid:8001，modelid:1234”，按照这个信息获取 dev_pid=8001，lm_id=1234

# DEV_PID = 8001 ;

# LM_ID = 1234 ;


# 极速版 打开注释的话请填写自己申请的appkey appSecret ，并在网页中开通极速版（开通后可能会收费）

# DEV_PID = 80001

# ASR_URL = 'http://vop.baidu.com/pro_api'

# SCOPE = 'brain_enhanced_asr'  # 有此scope表示有极速版能力，没有请在网页里开通极速版


class DemoError(Exception):

    pass

TOKEN_URL = 'http://openapi.baidu.com/oauth/2.0/token'


def fetch_token():

    params = {'grant_type': 'client_credentials',
              'client_id': API_KEY,
              'client_secret': SECRET_KEY}

    post_data = urlencode(params)
    post_data = post_data.encode('utf-8')
    req = Request(TOKEN_URL, post_data)

    try:

        f = urlopen(req)

        result_str = f.read()

    except URLError as err:

        print('token http response http code : ' + str(err.code))

        result_str = err.read()

    result_str =  result_str.decode()

    result = json.loads(result_str)

    if ('access_token' in result.keys() and 'scope' in result.keys()):


        if SCOPE and (not SCOPE in result['scope'].split(' ')):  # SCOPE = False 忽略检查

            raise DemoError('scope is not correct')

        print('SUCCESS WITH TOKEN: %s  EXPIRES IN SECONDS: %s' % (result['access_token'], result['expires_in']))

        return result['access_token']

    else:

        raise DemoError('MAYBE API_KEY or SECRET_KEY not correct: access_token or scope not found in token response')


if __name__ == '__main__':

    token = fetch_token()

    speech_data = []

    with open(AUDIO_FILE, 'rb') as speech_file:

        speech_data = speech_file.read()


    length = len(speech_data)

    if length == 0:

        raise DemoError('file %s length read 0 bytes' % AUDIO_FILE)

    speech = base64.b64encode(speech_data)
    speech = str(speech, 'utf-8')
    print(type(speech))
    params = {'dev_pid': DEV_PID,
             #"lm_id" : LM_ID,    #测试自训练平台开启此项
              'format': FORMAT,
              'rate': RATE,
              'token': token,
              'cuid': CUID,
              'channel': 1,
              'speech': speech,
              'len': length
              }
    post_data = json.dumps(params, sort_keys=False)
    print(type(post_data))
    # req = Request(ASR_URL, post_data.encode('utf-8'))
    # req.add_header('Content-Type', 'application/json')
    # f = urlopen(req)
    # result_str = f.read()
    # result_str = str(result_str, 'utf-8')
    # print(result_str)
    headers = {'content-type': 'application/json'}
    res = requests.post(ASR_URL, post_data, headers=headers)
    print(res.text)