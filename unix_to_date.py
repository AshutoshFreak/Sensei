from datetime import datetime
import pandas as pd
import os

def unix_to_date(ts):
	ts = int(ts)
	return datetime.utcfromtimestamp(ts).strftime('%Y')

if __name__ == "__main__":
	path = os.path.join("./data/csv", "submissions-copy.csv")
	df = pd.read_csv(path)
	df['creationTimeSeconds'] = df['creationTimeSeconds'].apply(unix_to_date)
	df = df[['creationTimeSeconds', 'programmingLanguage']]
	print(df)
	dic = df.to_dict()
	print(dic.keys())
	data = {'Programming Language': []}
	for i in range(len(dic['programmingLanguage'])-1):
		if dic['programmingLanguage'][i] != dic['programmingLanguage'][i+1]:
			if dic['programmingLanguage'][i] == dic['programmingLanguage'][i]:	# Eliminating NaN
				data['Programming Language'].append(dic['programmingLanguage'][i])

	years = []
	for i in range(len(dic['creationTimeSeconds'])-1):
		data[dic['creationTimeSeconds'][i]] = []

	for i in data.keys():
		if i != 'Programming Language':
			years.append(i)

	for i in years:
		for j in range(len(data['Programming Language'])):
			data[i].append(0)

	for i in range(len(dic['programmingLanguage'])-1):
		if dic['programmingLanguage'][i] == dic['programmingLanguage'][i]:
			ind = data['Programming Language'].index(dic['programmingLanguage'][i])
			data[str(dic['creationTimeSeconds'][i])][ind] += 1

print(data)

df = pd.DataFrame(data)
df.to_csv('example.csv')