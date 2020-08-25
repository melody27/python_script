import requests
import requests_cache

requests_cache.install_cache()
requests_cache.clear
url = 'http://127.0.0.1:5000/'
s = requests.Session()

for x in range(2):
    s.get(url)
    print(s.from_cache)