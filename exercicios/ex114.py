import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print('\033[31mO site do pudim não está acessivel no momento. \033[m')
else:
    print('\033[32mO site do pudim está disponivel\033[m')