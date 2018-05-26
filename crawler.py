import requests
from bs4 import BeautifulSoup

response = requests.get(
    "http://atu.hk/adm-grades.php?programme=JS1204&year=2017")
soup = BeautifulSoup(response.content, 'html.parser')

dse_score = soup.find_all('td')
dse_score = [item.text for item in dse_score]


dse_arr = []
count = 0


while(len(dse_score) > 0):
    dse_arr.append(dse_score[0:10])

print(dse_arr)





