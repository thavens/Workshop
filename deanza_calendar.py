import requests
from bs4 import BeautifulSoup

r = requests.get('https://deanza.instructure.com/feeds/calendars/user_hv4WJdm6Cv2lT9yUWWtq4kvlWHBF1iaWTn3FKMen.ics')

soup = BeautifulSoup(r.text)
print(soup.text)
