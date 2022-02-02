import matplotlib.pytplot as plt
import pandas as pd

df = pd.read_csv('test.csv')

left = [1,2,3,4,5,6,7]
heights = [0,0,0,0,0,0,0]
scoreSum = [0,0,0,0,0,0,0]
count = [0,0,0,0,0,0,0]

label = ['White', 'Asian', 'American Indian or Alska Native', 'Black or African American', 'Hispanic or Latino', 'Middle Eastern' 

for x in range(df.shape[0]):
	response = df.iloc[x,4]
	 

for x in range(len(left)):
	if count[x] != 0:
		heights[x] = scoreSum[x]/count[x]
	else:
		heights[x] = 0

