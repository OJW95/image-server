import requests

image = open('img_1.png', 'rb')

upload = {'file': image}

r = requests.post('http://192.168.0.5:5000/image/upload/', files=upload)

if r != None:
    print('OK')