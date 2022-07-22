import requests

r= requests.get("http://10.33.16.19:5000", data="Hey")

print(r.text)
print(r)