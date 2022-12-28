import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import copy
pathfound=False
grid = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
goal=(len(grid)-1,len(grid[0])-1)
moves=[
(1,0),
(1,-1),
(0,-1),
(-1,-1),
(-1,0),
(-1,1),
(0,1),
(1,1)
]
track = []
def print2d(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            if((a[i][j])<10):
                print(a[i][j],' ',end=' ',sep='')
            else:
                print(a[i][j],end=' ')
        print()

def validposition(x,y):
    global grid
    if(x>=0 and x<len(grid) and y>=0 and y<len(grid[0])):
        return True
    return False

def dfs(x,y,k):
    global goal
    global grid
    global pathfound
    global track
    track[x][y]=k
    if(x==goal[0] and y==goal[1]):
        print('Goal reached')
        pathfound=True
        pass
    for i in range(len(moves)):
        newx=x+moves[i][0]
        newy=y+moves[i][1]
        if(validposition(newx,newy)):
            if(track[newx][newy]==0 and grid[newx][newy]==0):
                print('pos=','(',newx,',',newy,')',' val=',track[newx][newy],' k=',k,sep='')
                dfs(newx,newy,k+1)
    pass
def handlepath():
    global goal
    global grid
    global track

    mazeimg=copy.deepcopy(grid)
    print2d(track)
    path=[]
    path.append((goal[0],goal[1]))
    if(track[goal[0]][goal[1]]!=0):
        x=goal[0]
        y=goal[1]
        mazeimg[x][y]=2
        k=track[goal[0]][goal[1]]
        print(k)
        while(k>0):
            for i in range(len(moves)):
                newx=x+moves[i][0]
                newy=y+moves[i][1]
                if(validposition(newx,newy)):
                    if(track[newx][newy]==k-1):
                        path.append((newx,newy))
                        x=newx
                        y=newy
                        mazeimg[x][y]=2
                        print(x,y)
                        k-=1
                        break
        path.reverse()
        print(path)

        fig, ax = plt.subplots(figsize=(10,10))
        ax.imshow(mazeimg, cmap=plt.cm.Dark2)
        ax.scatter(x,y, color = "yellow", s = 200)
        ax.scatter(goal[0],goal[1],  color = "red", s = 200)
        plt.show()
    else:
        print('No path found')

def start():
    global goal
    global grid
    global track
    x=0
    y=0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if(grid[i][j]==2):
                x=i
                y=j
            if(grid[i][j]==3):
                goal=(i,j)
    grid[x][y]=1
    grid[goal[0]][goal[1]]=0

    for i in range(len(grid)):
        track.append([])
        for j in range(len(grid[i])):
            track[-1].append(0)
    print2d(grid)
    dfs(x,y,k=0)
    print()
    handlepath()
    
start()