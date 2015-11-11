import requests
import json


url = "https://compressor.io/server/Lossy.php"
files = {'file': open('dark_earth-wallpaper-1366x768.jpg', 'rb')}

headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0'
headers['Accept'] = 'application/json, text/javascript, */*; q=0.01'
headers['Host'] = 'compressor.io'
headers['Accept-Encoding'] = 'gzip, deflate'
headers['X-Requested-With'] = 'XMLHttpRequest'
headers['Connection'] = 'keep-alive'

r = requests.post(url, headers=headers, data=files)

print(r.json())
# print(r.headers)
