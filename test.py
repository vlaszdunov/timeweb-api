import requests
from settings import config
from BearierAuth import BearerAuth

TIMEWEB_API_TOKEN = config()

API_URL = 'https://api.timeweb.cloud/api/v1/'

list_of_projects = requests.get(API_URL+'projects',
                                auth=BearerAuth(TIMEWEB_API_TOKEN)).json()['projects']

for project in list_of_projects:
    if project['name'] == 'Test CI/CD':
        list_of_project_servers = requests.get(API_URL+f'projects/{project['id']}/resources/servers',
                                               auth=BearerAuth(TIMEWEB_API_TOKEN)).json()['servers']
for server in list_of_project_servers:
    if server['comment'] == 'Testing CI-CD':
        a = requests.post(API_URL+f'servers/{server['id']}/action', data={'action': 'shutdown'},
                          auth=BearerAuth(TIMEWEB_API_TOKEN))
print(a)
