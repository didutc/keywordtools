import time
import random
import requests
import hashlib, hmac, base64
import pyzard
import pandas as pd
import pyperclip
# 생성된 key를 변수에 저장합니다.
t = pyzard.readfile('h.text')
t = t.split('\n')
filter = ['콘','드','로','이','친']
t2filtered_lst = pyzard.listfilter(True,filter,t)
t2filtered_lst ='\n'.join(t2filtered_lst)
pyperclip.copy(t2filtered_lst)