import requests,json

data = {'message':'What time is it?'}

r = requests.post("http://127.0.0.1:5000", json = data)
print(r.text)