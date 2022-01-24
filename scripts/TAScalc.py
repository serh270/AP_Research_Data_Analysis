import pandas as pd
import csv

points_norm = {
	'Completely Disagree'	: 1,
	'Disagree'		: 2,
	'Neutral'		: 3,
	'Agree'			: 4,
	'Completely Agree'	: 5
}

points_rev = {
	'Completely Disagree'	: 5,
	'Disagree'		: 4,
	'Neutral'		: 3,
	'Agree'			: 2,
	'Completely Agree'	: 1
}

revQs = [4,5,10,18,19]

# configure pandas dataframes
df = pd.read_csv('test.csv')
df2 = df.iloc[:, 8:df.shape[1]]

#configure log files 
try:
	os.remove('log.txt')
except:
	pass

logFile = open('log.txt', 'w')

# return score for each response. Accounts for reverse scored questions
def getScore(response, qNum):
	isRev = False
	if (qNum + 1) in revQs:
		isRev = True

	if isRev:
		myDict = points_rev
#		print('Reversed: ', (qNum + 1))
	else:
		myDict = points_norm

	if response in myDict:
		return myDict[response]
	else:
		return 0

# general logging function
def log(message):
	message = str(message)
	print(message)
	logFile.write(message)
	logFile.write('\n')

def main():
	for x in range(df2.shape[0]):
		score = 0
		for y in range(20):
			log(('#', (y+1), ':', df2.iloc[x,y], getScore(df2.iloc[x,y], y)))	
			score += getScore(df2.iloc[x,y], y)

		df.at[x,'Score'] = score
		log(('RESPONDANT', (x+1), 'SCORE:', df.iloc[x,1], '------------')) 
	
	print(df["Score:"])

	df.to_csv('test.csv', index=False)
	
main()
