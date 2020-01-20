# encoding=utf8
import requests
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

