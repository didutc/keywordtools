import time
import random
import requests
import hashlib, hmac, base64
import pyzard
import pandas as pd
# 생성된 key를 변수에 저장합니다.

CUSTOMER_ID = '2784540'
API_KEY = '010000000005c54ac506c3795b3f14c7350b5b123ed69c5ac1612f5ecbab04893089d633f5'
SECRET_KEY = 'AQAAAAAFxUrFBsN5Wz8UxzULWxI+x0EF6Ct0KsalNjPqhq8+CQ=='

t = pyzard.readfile('data.text')
t= t.split('\n')

t_lst=pyzard.listsplit(t,5)
print(t_lst)

t= ','.join(t)

BASE_URL = 'https://api.naver.com'
uri = '/keywordstool'   # BASE_URL 뒤에 오는 uri 입니다.
method = 'GET'          # GET 방식을 사용합니다.

# parameter 들을 입력합니다. (가장 먼저 hintKeywords와 showDetail 만 입력해보겠습니다.)


def get_header(method, uri, api_key, secret_key, customer_id):
    timestamp = str(int(time.time() * 1000))
    signature = generate(timestamp, method, uri, SECRET_KEY)
    return {'Content-Type': 'application/json; charset=UTF-8', 'X-Timestamp': timestamp, 'X-API-KEY': API_KEY, 'X-Customer': str(CUSTOMER_ID), 'X-Signature': signature}
def generate(timestamp, method, uri, secret_key):
    message = "{}.{}.{}".format(timestamp, method, uri)
    hash = hmac.new(secret_key.encode("utf-8"), message.encode("utf-8"), hashlib.sha256)

    hash.hexdigest()
    return base64.b64encode(hash.digest())
last_lst =[]

for li in t_lst:
    query = {
        'siteId': '',
        'biztpId': '',
        'hintKeywords': li,
        'event': '',
        'month': '',
        'showDetail': '1'
        }
    time.sleep(1.5)
    r = requests.get(
        BASE_URL + uri,
        params = query,
        headers = get_header(
            method=method,
            uri=uri,
            api_key=API_KEY,
            secret_key=SECRET_KEY,
            customer_id=CUSTOMER_ID
        ))
    r_data = r.text
    last_lst.append(r_data)
    # print(r_data)

last_lst = ','.join(last_lst)
key = pyzard.pinset(last_lst,'"relKeyword":"','"')
p = pyzard.pinset(last_lst,'"monthlyPcQcCnt":',',')
m= pyzard.pinset(last_lst,'"monthlyMobileQcCnt":',',')

pm = []


for li1,li2 in zip(p,m):
    if "<" in li1:
        li1 = 0
    if "<" in li2:
        li2 = 0
    q = int(li1)+int(li2)

    pm.append(q)
print(key)
print(pm)
data = pd.DataFrame({
    '이름': key,
    '검색량': pm,

})

data = data.drop_duplicates(['이름'])
data.to_csv("filename.csv", mode='w',index = False , encoding='utf-8-sig')
# # 필터

# fkey = []
# pmkey = []
# for l1,l2 in zip(key,pm):
#     if '콘' in l1:
#         fkey.append(l1)
#         pmkey.append(l2)
#         pass
#     if '드' in l1:
#         fkey.append(l1)
#         pmkey.append(l2)
#         pass
#     if '로' in l1:
#         fkey.append(l1)
#         pmkey.append(l2)
#         pass
#     if '이' in l1:
#         fkey.append(l1)
#         pmkey.append(l2)
#         pass
#     if '친' in l1:
#         fkey.append(l1)
#         pmkey.append(l2)
#         pass
# data = pd.DataFrame({
#     '이름': fkey,
#     '검색량': pmkey,

# })

# data = data.drop_duplicates(['이름'])
# data.to_csv("filename.csv", mode='w',index = False , encoding='utf-8-sig')