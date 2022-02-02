import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('test.csv')

tas_scores = [range(80)]
tas_count = []

for x in range(df.shape[0]):
	score = int(df.iloc[x,1])
	for y in range(80):
		if y == score:

plt.scatter(hrs_gaming, hrs_gaming_tas)

plt.xlabel('age')
plt.ylabel('TAS score')
plt.title('Gamer Age per TAS-Score')

plt.savefig('graph_age.png')

#plt.show()
