# encoding=utf8
from aip import AipFace
import base64
import json

APP_ID = '18029476'
API_KEY = 'f7pnKUZXu7A2yHKDaorvMCM3'
SECRET_KEY = 'oBISsLcI4T5bucaswTwj0XpVpXYyBaxQ'
client = AipFace(APP_ID, API_KEY, SECRET_KEY)

imagetype = "BASE64"
with open('test.jpg', 'rb') as f:
    data = f.read()
image = str(base64.b64encode(data), 'utf8')

res = client.detect(image, imagetype)['result']
print(json.dumps(res, indent=4))
