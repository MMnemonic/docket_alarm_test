from urllib.request import urlopen
from urllib.error import HTTPError, URLError

try:
    ip_address = urlopen('https://api.ipify.org/').read().decode('utf-8')
    print(ip_address)
except (HTTPError, URLError):
    print("not connected")

