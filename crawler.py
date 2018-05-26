import requests
from bs4 import BeautifulSoup

response = requests.get(
    "http://atu.hk/adm-grades.php?programme=JS1204&year=2017")
soup = BeautifulSoup(response.content, 'html.parser')

dse_score = soup.find_all('td')
dse_score = [item.text for item in dse_score]

