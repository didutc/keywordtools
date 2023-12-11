import time
import random
import requests
import hashlib, hmac, base64
import pyzard
import pandas as pd
# 생성된 key를 변수에 저장합니다.

key= []
q = pyzard.readfile('naver_ad.text')
q = q.split('\n') 
q = q
for li in q:
    url = 'https://search.shopping.naver.com/search/all?where=all&frm=NVSCTAB&query='
    pyzard.pinset

    time.sleep(2)
    print(li)
    t = requests.get(url+li).text
    print(t)
    q = pyzard.pinset(t,'title="검색어 입력" value="','"/>')
    t= pyzard.pinset(t,'adProduct_inner','<div class="adProduct_item__1zC9h"><div class="')
    

    if len(t) == 0:
        print('skip')
        continue
    if not li == q:
        print(q)
        print(li)
        print('skip2')
        continue
    key.append(li)
    
key = '\n'.join(key)
pyzard.report('nr.text',key)

    