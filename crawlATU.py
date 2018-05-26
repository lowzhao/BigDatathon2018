import requests
from bs4 import BeautifulSoup

import pandas as pd
import os

import json

import math

def toCSV(code,year):
	try:
		response = requests.get('http://atu.hk/adm-grades.php?programme='+code+'&year='+year)
		soup = BeautifulSoup(response.content, 'html.parser')

		dse_score = soup.find_all('td')
		dse_score = [item.text for item in dse_score]


		dse_arr = []
		count = 0

		while(len(dse_score) > count ):
			dse_arr.append(dse_score[count:count + 10])
			count +=10 

		dataset = {
			'band':[],
			'best5':[]
		}


		for index in range(0,len(dse_arr)):
			dataset['band'].append(dse_arr[index][1])
			dataset['best5'].append(dse_arr[index][-3])
		# dataset
		print(dataset)

		# create CSV

		# delimiter = ','

		# band , best5
		open(code+'_'+year,'a').close()

		df = pd.DataFrame(dataset,columns=['band','best5'])
		df.to_csv(code+'_'+year)
	except Exception as e2:
		try : 
			excepted = open('excepted','a')
			excepted.write('http://atu.hk/adm-grades.php?programme='+code+'&year='+year + '\n')
			excepted.close()
		except Exception as e:
			print(str(e))
		print(str(e2))



def searchAll():
	for num in range(1,11):
		searchUni(num)


# def searchUni(uni):
# 	for num in range(2012,2018)
# 		searchYear(uni,num)


# def searchYear(uni,year):
# 	yearResponse = request.get('http://atu.hk/get_programmes.ajax.php?inst='+uni+'&year='+year)
# 	tempcodes = json.loads(yearResponse.text)
# 	for item in tempcodes :
# 		# item[0] == code
# 		# item[1] == name
# 		# year == year
# 		for item2 in AllCodes:
# 			if item2['code'] == item[0]:
# 				item2['year'].append(year)
# 				item2['name'].append(item[1])



def crawlCode(code):
	for num in range(2012,2018):
		toCSV(code,str(num))


# http://atu.hk/get_programmes.ajax.php?inst=2&year=2016

# AllCodes = [{
# 	'code':
# 	'year':[],
# 	'name':[]
# }
# ]

toCSV('JS1001','2017')
# toCSV(url = 'http://atu.hk/adm-grades.php?programme=JS1204&year=2017', filename = 'url.csv')
# toCSV(url = 'http://atu.hk/adm-grades.php?programme=JS1204&year=2017', filename = 'url.csv')
# toCSV(url = 'http://atu.hk/adm-grades.php?programme=JS1204&year=2017', filename = 'url.csv')
# toCSV(url = 'http://atu.hk/adm-grades.php?programme=JS1204&year=2017', filename = 'url.csv')




# CSV -> code Array

df = pd.read_csv('KelvinUG_1.csv')
print(df['Programme Code'])

# codeArr = []

for item in df['Programme Code']:
	if item != 'NaN':
		crawlCode(item)
	



