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
				scoreSum[y] += df.iloc[x, 1]
				count[y] += 1
				break

def getHeights(scoreSum, count):
	heights = []
	for x in range(9):
		if count[x] == 0:
			heights.append(0)
		else:
			heights.append(scoreSum[x] / count[x])

	return heights

print(scoreSum)
print(count)

height = getHeights(scoreSum, count)

print(height)

plt.bar(left, height, tick_label = tick_label, width = 0.8)

plt.xlabel('most common genre')
plt.ylabel('average TAS score')

plt.savefig('graph_genre.png')
