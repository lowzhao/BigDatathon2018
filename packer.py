import csv
import pandas as pd



def go(year):
	df = pd.read_csv('KelvinUG_1.csv')
# print(df['Programme Code'])
	dataset = {
		'band': [],
		'best5': []
	}
	for item in df['Programme Code']:
		try :
			if item[2] == '3':
				try:
					df2 = pd.read_csv(item+'_'+year)
					# print(df2)
					try:
						for item2 in range(0, len(df2['band'])):
							dataset['band'].append(df2['band'][item2])
							dataset['best5'].append(df2['best5'][item2])
					except Exception as e2:
						print(str(e2))
				except Exception as e:
					print(str(e))
		except Exception as e:
			pass

	df = pd.DataFrame(dataset,columns=['band','best5'])
	df.to_csv('CS_'+year+'.csv')


	print(dataset)
go('2013')