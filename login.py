from json import load
from dotenv import load_dotenv
import os

load_dotenv()
user = os.getenv('USERNAME')
pwd = os.getenv('PASSWORD')

import requests
from dotenv import load_dotenv
load_dotenv()
import os
password = os.getenv('PASSWORD')
user = os.getenv('USERNAME')

payload = {
    'j_username': user,
    'j_password': password,
    '_eventId_proceed': '' 
}

s = requests.Session()
s.get('https://myportal.fhda.edu/')
r = s.post('https://ssoshib.fhda.edu/idp/profile/cas/login?execution=e1s1', data=payload)

with open('output.html', 'w') as f:
    f.write(r.text)

s.close()