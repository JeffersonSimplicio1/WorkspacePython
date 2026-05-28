import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.google.com.br')
except:
    print('Deu erro')
else:
    print('Tudo Certo!!')