import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

room = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

start=(0,0)
goal=(len(room)-1, len(room[0])-1)

fig, ax = plt.subplots(figsize=(10,10))
ax.imshow(room, cmap=plt.cm.Dark2)
ax.scatter(start[1],start[0], color = "yellow", s = 200)
ax.scatter(goal[1],goal[0],  color = "red", s = 200)
plt.show()

for i in range(len(room)):
    for j in range(len(room[0])):
        print(room[i][j],end='')
    print()
