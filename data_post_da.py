import requests
user = 'username'
passwd = 'sads'

payload = {
    'j_username': user,
    'j_password': passwd,
    '_eventId_proceed': '' 
}

s = requests.Session()
s.get('https://myportal.fhda.edu/')
r = s.post('https://ssoshib.fhda.edu/idp/profile/cas/login?execution=e1s1', data=payload)

with open('output.html', 'w') as f:
    f.write(r.text)

s.close()