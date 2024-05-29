import requests
from settings import config
import os
from BearierAuth import BearerAuth

TIMEWEB_API_TOKEN = config()
del os.environ['TIMEWEB_API_TOKEN']

API_URL = 'https://api.timeweb.cloud/api/v1/'

response = requests.get(API_URL+'projects',
                        auth=BearerAuth(TIMEWEB_API_TOKEN))
print(response.json())
