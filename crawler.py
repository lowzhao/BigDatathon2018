import requests
from bs4 import BeautifulSoup

response = requests.get(
    "http://atu.hk/adm-grades.php?programme=JS1204&year=2017")
soup = BeautifulSoup(response.content, 'html.parser')

dse_score = soup.find_all('td')
dse_score = [item.text for item in dse_score]


dse_arr = []
count = 0

while(len(dse_score) > count ):
	dse_arr.append(dse_score[count:count + 10])
	count +=10

dataset = []


for index in range(0,len(dse_arr)):
	data = {}
	data['band'] = dse_arr[index][1]
	data['best5'] = dse_arr[index][-3]
	dataset.append(data)
print(dataset)
# print(dse_arr)





