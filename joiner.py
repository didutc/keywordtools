import pyzard
import pyperclip
q = pyzard.readfile('joiner.text')
q = q.replace('\n',',')
pyperclip.copy(q)