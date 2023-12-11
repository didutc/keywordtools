from konlpy.tag import Okt
from collections import Counter
import platform
print(platform.architecture())
f = open('startkeyword.text','r',encoding='utf-8')	
news = f.read()

# okt 객체 생성
okt = Okt()
noun = okt.nouns(news)
count = Counter(noun)
	
# 명사 빈도 카운트
noun_list = count.most_common(100)
for v in noun_list:
	print(v)

import pyzard

