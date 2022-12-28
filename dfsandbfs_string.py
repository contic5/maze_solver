import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import copy

pathfound=False
usingdfs=True
usingbfs=False
grid = np.array([[2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 3]])
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

existingWires = """
SX.
X..
XXG
""".strip('\n')

distances = []
totalchecks=0
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
    global totalchecks
    global goal
    global grid
    global pathfound
    global distances
    distances[x][y]=k
    totalchecks+=1
    if(x==goal[0] and y==goal[1]):
        print('Goal reached')
        pathfound=True
        pass
    for i in range(len(moves)):
        newx=x+moves[i][0]
        newy=y+moves[i][1]
        if(validposition(newx,newy)):
            if(distances[newx][newy]==0 and grid[newx][newy]==0):
                print('pos=','(',newx,',',newy,')',' val=',distances[newx][newy],' k=',k,sep='')
                dfs(newx,newy,k+1)
    pass
def bfs(x,y):
    global totalchecks
    k=1
    distances[x][y]=1
    while(distances[goal[0]][goal[1]])==0 and k<len(grid)**2:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(distances[i][j]==k):
                    totalchecks+=1
                    x=i
                    y=j
                    for m in range(len(moves)):
                        newx=x+moves[m][0]
                        newy=y+moves[m][1]
                        if(validposition(newx,newy)):
                            if(distances[newx][newy]==0 and grid[newx][newy]==0):
                                distances[newx][newy]=k+1
        print(k) 
        k+=1
def handlepath(algname):
    global goal
    global grid
    global distances
    global totalchecks

    mazeimg=copy.deepcopy(grid)
    #Set wall color to be black
    for i in range(len(mazeimg)):
        for j in range(len(mazeimg[0])):
            if(mazeimg[i][j]==1):
                mazeimg[i][j]=7
    #print2d(distances)
    path=[]
    path.append((goal[0],goal[1]))
    if(distances[goal[0]][goal[1]]!=0):
        x=goal[0]
        y=goal[1]
        k=distances[goal[0]][goal[1]]

        mazeimg[x][y]=5
        endval=k
        print(k)
        while(k>1):
            for i in range(len(moves)):
                newx=x+moves[i][0]
                newy=y+moves[i][1]
                if(validposition(newx,newy)):
                    if(distances[newx][newy]==k-1):
                        path.append((newx,newy))
                        x=newx
                        y=newy
                        mazeimg[x][y]=2+((k+1)%2)
                        print(x,y)
                        k-=1
                        break
        mazeimg[x][y]=4
        path.reverse()
        print(path)
    else:
        print('No path found')
        

def start(mazestr):
    global totalchecks
    global goal
    global grid
    global distances
    filenames=['mazeorig','maze','maze2','maze3']
    for mazename in filenames:
        strgrid=mazestr.split('\n')
        for i in range(len(strgrid)):
            strgrid[i]=strgrid[i].split()
        print(strgrid)
        x=0
        y=0
        startx=x
        starty=y
        grid=[[0 for i in range(len(strgrid[0]))] for j in range(len(strgrid))] 

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(strgrid[i][j]=='S'):
                    startx=i
                    starty=j
                if(strgrid[i][j]=='G'):
                    goal=(i,j)
                if(strgrid[i][j]=='X'):
                    grid[i][j]=1
                else:
                    grid[i][j]=0
        x=startx
        y=starty
        grid[x][y]=1
        grid[goal[0]][goal[1]]=0
        
        if(usingdfs):
            totalchecks=0
            distances=[]
            distances=[]
            for i in range(len(grid)):
                distances.append([])
                for j in range(len(grid[i])):
                    distances[-1].append(0)
            #print2d(grid)
            dfs(x,y,k=1)
            print()
            handlepath('dfs')

        if(usingbfs):
            totalchecks=0
            distances=[]
            for i in range(len(grid)):
                distances.append([])
                for j in range(len(grid[i])):
                    distances[-1].append(0)
            #print2d(grid)
            x=startx
            y=starty
            bfs(x,y)
            print()
            handlepath('bfs')
    
plt.rc('grid', linestyle="-", color='black',linewidth=4)
start(existingWires)

