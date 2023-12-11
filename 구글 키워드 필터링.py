import pyperclip
import pyzard
filtered=input('필터할 문구 쓰시오:')
filtered = filtered.split(',')
original =  pyperclip.paste()
original = original.split('\n')
original = pyzard.listfilter(False,filtered,original)
original = '\n'.join(original)
print(original)
pyperclip.copy(original)