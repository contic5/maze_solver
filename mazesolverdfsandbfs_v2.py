import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import copy


usingdfs=False
usingdfsv2=True
usingbfs=False

heavydebug=False
debug=True
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

pathfound=False
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
        return
    for i in range(len(moves)):
        newx=x+moves[i][0]
        newy=y+moves[i][1]
        if(validposition(newx,newy)):
            if(distances[newx][newy]==0 and grid[newx][newy]==0):
                if(heavydebug):
                    print('pos=','(',newx,',',newy,')',' val=',distances[newx][newy],' k=',k,sep='')
                
                dfs(newx,newy,k+1)
    return

def dfsv2(x,y,k):
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
        return

    movescopy=copy.deepcopy(moves)
    movedistances=[]
    for i in range(len(movescopy)):
        distance=calcdistance(x,y,goal[0],goal[1])
        movedistances.append(distance)
    
    movescopy=[movescopy for _, movescopy in sorted(zip(movedistances, movescopy),reverse=True)]

    for i in range(len(movescopy)):
        newx=x+movescopy[i][0]
        newy=y+movescopy[i][1]
        if(validposition(newx,newy)):
            if(distances[newx][newy]==0 and grid[newx][newy]==0):
                if(heavydebug):
                    print('pos=','(',newx,',',newy,')',' val=',distances[newx][newy],' k=',k,sep='')

                dfsv2(newx,newy,k+1)
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
        if(heavydebug):
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
        if(heavydebug):
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
                        if(heavydebug):
                            print(x,y)
                        k-=1
                        break
        mazeimg[x][y]=4
        path.reverse()
        if(heavydebug):
            print(path)
        #Plot size 1280 by 960
        fig, ax = plt.subplots(figsize=(len(grid[0]),len(grid)))
        ax.imshow(mazeimg, cmap=plt.cm.Dark2)
        if(len(grid)<30 and len(grid[0])<30):
            for i in range(len(path)):
                ypos=(len(grid)-path[i][0])/len(grid)-0.5/len(grid)
                xpos=(path[i][1])/len(grid[0])+0.5/len(grid[0])
                ax.text(xpos,ypos,str(i),transform=ax.transAxes,color='blue')

        #ax.scatter(x,y, color = "yellow", s = 200)
        #ax.scatter(goal[1],goal[0],  color = "red", s = 200)
        if(len(grid)<15):
            ax.set_xticks(np.arange(-0.5, len(grid[0]), 1))
            ax.set_yticks(np.arange(-0.5, len(grid), 1))
        else:
            ax.set_xticks(np.arange(-0.5, len(grid[0]), len(grid[0])))
            ax.set_yticks(np.arange(-0.5, len(grid), len(grid[0])))
        ax.set_xticklabels([])
        ax.set_yticklabels([])

        print(algname+' reached the end position in '+str(endval)+' moves with '+str(totalchecks)+' total checks')
        plt.title(algname+' reached the end position in '+str(endval)+' moves with '+str(totalchecks)+' total checks')
        plt.grid()
        plt.rc('grid', linestyle="-", color='black')
        plt.show()

    else:
        print('No path found')
        
def readfile(filename):
    myfile=open(filename+'.txt','r')
    lines = myfile.readlines() 
    res=[]
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
        val=[]
        for j in range(len(lines[0])):
            val.append(int(lines[i][j]))
        res.append(val)
    return res

def calcdistance(startx,starty,endx,endy):
    return ((startx-endx)**2+(starty-endy)**2)**0.5

def start():
    global totalchecks
    global goal
    global grid
    global distances
    filenames=['mazeorig','maze','maze2','maze3']
    for mazename in filenames:
        grid=readfile(mazename)
        x=0
        y=0
        startx=x
        starty=y
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]==2):
                    startx=i
                    starty=j
                if(grid[i][j]==3):
                    goal=(i,j)
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

        if(usingdfsv2):
            totalchecks=0
            distances=[]
            distances=[]
            for i in range(len(grid)):
                distances.append([])
                for j in range(len(grid[i])):
                    distances[-1].append(0)
            #print2d(grid)
            dfsv2(x,y,k=1)
            print()
            handlepath('dfsv2')

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
start()