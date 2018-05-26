from snownlp import SnowNLP

import requests

from bs4 import BeautifulSoup



reponse  = requests.get('https://forum.hkgolden.com/view.aspx?type=SC&message='+6906541+'&page='+1+'&highlight_id=0&authorOnly=False')

soup = BeautifulSoup(reponse.content,'html.parser')

items = soup.find_all('div',class_='ContentGrid')


text -> translate into english 
-> nltk fins similarity

dse
jupas
HKdse
computing,
business,
nursing

