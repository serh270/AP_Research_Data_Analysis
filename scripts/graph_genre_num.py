import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('test.csv')

left = [1,2,3,4,5,6,7,8]

scoreSum = [0,0,0,0,0,0,0,0]
count = [0,0,0,0,0,0,0,0]

label = ['Action/Adventure', 'First/Third Person Shooter', 'MMORPG (Massively Multiplayer Online Role Play Game)', 'MOBA (Multiplayer Online Battle Arena)', 'Puzzle', 'Real Time Strategy', 'Sandbox', 'Simulation and Sports']

tick_label = ['AA', 'FPS', 'MMORPG', 'MOBA', 'Puzzle', 'RTS', 'Sand', 'Sim']

for x in range(df.shape[0]):
	response = df.iloc[x, 5]
	if (response not in label):
		print(response)
	else:	
		for y in range(8):
			if response == label[y]:
				count[y] += 1
				break

print(scoreSum)
print(count)

plt.bar(left, count, tick_label = ["","","","","","","",""], width = 0.8)

for x in range(len(count)):
	count[x] = str(count[x])

celltxt = [count]
x
plt.subplots_adjust(left=0.2, bottom=0.2)

plt.table(cellText=celltxt, colLabels=tick_label, loc='bottom')

plt.ylabel('number of respondants')

plt.title ('Number Of Respondants Per Genre Groups')

plt.savefig('graph_genre_num.png')
