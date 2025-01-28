# Requests in Python
# Import Necessary Libraries
import requests 
import os

from PIL import Image
from IPython.display import IFrame

# make a GET request
url = 'https://www.ibm.com'
r = requests.get(url)

print(r.status_code)
print(r.request.headers)
print("request body:", r.request.body)
print(r.headers)
print(r.headers['date'])
print(r.headers['Content-Type'])
print(r.encoding)
print(r.text[0:100])

# making a POST request
url2 = 'https://www.ibm.com'
r2 = requests.post(url2, json = {'content': 'Hello, World!'})
print(r2.status_code)


# making a GET request with URL paremeters (params)
url_get = 'http://httpbin.org/get'
# add a query string
# ? -> parameter name -> = -> value -> & -> parameter name -> = -> value
payload = {"name": "Joseph", "ID": "123"}
r3 = requests.get(url_get,params=payload)
print(r3.url)
print("request body: ", r3.request.body)
print(r3.status_code)
print(r3.text)


# making a POST request 
url_post = 'http://httpbin.org'
r_post = requests.post(url_post, data=payload)
print("POST request URL: ",r_post.url)
print("POST request body: ",r_post.request.body)