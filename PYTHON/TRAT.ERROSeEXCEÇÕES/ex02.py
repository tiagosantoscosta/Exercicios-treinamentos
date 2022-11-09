import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim não está acessível no momento. ')
else:
    print('\nO site Pudim ESTÁ acessível no momento.\n ')
    print(site.read())