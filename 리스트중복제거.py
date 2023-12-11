import pyzard
import pyperclip

t = pyzard.readfile('nr.text')
t = t.split('\n')
t=list(dict.fromkeys(t))
t = '\n'.join(t)
pyperclip.copy(t)