import numpy as np; np.random.seed(13)
import matplotlib.pyplot as plt

data = np.random.randint(0,12,size=72)
bins = np.arange(13)-0.5

hist, edges = np.histogram(data, bins=bins)

y = np.arange(1,hist.max()+1)
x = np.arange(12)
X,Y = np.meshgrid(x,y)

plt.scatter(X,Y, c=Y<=hist, cmap="Greys")

plt.show()