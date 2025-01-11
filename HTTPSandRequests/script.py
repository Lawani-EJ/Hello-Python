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
