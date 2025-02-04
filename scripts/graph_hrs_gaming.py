import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('test.csv')

hrs_gaming = []
hrs_gaming_tas = []

for x in range(df.shape[0]):
	hrs_gaming.append(df.iloc[x,7])
	hrs_gaming_tas.append(df.iloc[x,1])

plt.scatter(hrs_gaming, hrs_gaming_tas)

plt.xlabel('hours spend gaming')
plt.ylabel('TAS score')
plt.title('Hours spend gaming per TAS-Score')

plt.savefig('graph_hrs_gaming.png')

#plt.show()
