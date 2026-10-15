import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6,8,12])
ypoints = np.array([0, 250,350,450])

plt.plot(xpoints, ypoints)
plt.plot(ypoints, marker = 'o')
plt.show()
plt.show(ypoints)