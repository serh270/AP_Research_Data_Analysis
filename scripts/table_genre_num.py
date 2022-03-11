import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('test.csv')

left = [1,2,3,4,5,6,7,8,9]

scoreSum = [0,0,0,0,0,0,0,0,0]
count = [0,0,0,0,0,0,0,0,0]


label = ['Action/Adventure', 'First/Third Person Shooter', 'MMORPG (Massively Multiplayer Online Role Play Game)', 'MOBA (Multiplayer Online Battle Arena)', 'Puzzle', 'Real Time Strategy', 'Sandbox', 'Simulation and Sports']

tick_label = ['AA', 'FPS', 'MMORPG', 'MOBA', 'Puzzle', 'RTS', 'Sand', 'Sim', 'Other']

for x in range(df.shape[0]):
	print('Respondant Score:', df.iloc[x,1])
	response = df.iloc[x, 5]
	if (response not in label):
		scoreSum[8] += df.iloc[x,1]
		count[8] += 1
	else:	
		for y in range(8):
			if response == label[y]:
				print('match found')
				count[y] += 1
				break

print(scoreSum)
print(count)


for x in range(len(count)):
	count[x] = str(count[x])

celltxt = [count]

plt.table(cellText=celltxt, colLabels=tick_label)

# plt.xlabel('most common genre')
# plt.ylabel('number of respondants')

plt.savefig('table_genre_num.png')
