import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import math
import seaborn as sns

# Node class for A*
class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

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

def astar(room, start, goal):
    #initialize start and goal nodes
    startNode = Node(None, start)
    goalNode = Node(None, goal)
    startNode.g = 0
    startNode.h = 0
    startNode.f = 0
    goalNode.g = 0
    goalNode.h = 0
    goalNode.f = 0
    
    openList = []
    closedList = []
    
    openList.append(startNode)
    
    while len(openList) > 0:
        currNode = openList[0]
        currIndex = 0

        idx = 0

        # find next best node to step to
        for idx, itm in enumerate(openList, 0):
        	if itm.f < currNode.f:
        		currNode = itm
        		currIndex = idx


        openList.pop(currIndex)
        closedList.append(currNode)

        # found goal
        if currNode == goalNode:
        	path = []
        	curr = currNode
        	while curr is not None:
        		path.append(curr.position)
        		curr = curr.parent
        	return(path[::-1])

        # create child nodes of current node
        childNodes = []

        for nextStep in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
        	nextPosition = (currNode.position[0] + nextStep[0], currNode.position[1] + nextStep[1])

        	# check child node is within bounds of the array
        	if nextPosition[0] > (len(room) - 1) or nextPosition[0] < 0 or nextPosition[1] < 0 or nextPosition[1] > (len(room[len(room)-1]) - 1):
        		continue

        	# check child node is not an obstacle 
        	if room[nextPosition[0]][nextPosition[1]] == 1:
        		continue

        	newNode = Node(currNode, nextPosition)
        	childNodes.append(newNode)


        for child in childNodes:

        	# check if child node is already on the closed node list
        	isClosed = 0
        	for childClosed in closedList:
        		if child == childClosed:
        			isClosed = 1
        			continue
        	if isClosed == 1:
        		continue
        	child.g = currNode.g + 1
        	child.h = ((child.position[0] - goalNode.position[0]) ** 2) + ((child.position[1]- goalNode.position[1]) ** 2)
        	child.f = child.g + child.h

        	# check if child node is already on open node list
        	isOpen = 0
        	for openNode in openList:
        		if child == openNode and child.g > openNode.g:
        			isOpen = 1
        			continue
        	if isOpen == 1:
        		continue
        	# add child node to open node list
        	openList.append(child)




def main():
	# 2d robot space
    '''
    room = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    '''
    
    room=readfile('maze3')
    


    # room = [[0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1],
    # [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    # [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0],
    # [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    # [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    # [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    #room[row][col]
    # coordinates of start and goal node
    start=(0,0)
    goal=(len(room)-1, len(room[0])-1)

    for i in range(len(room)):
            for j in range(len(room[0])):
                if(room[i][j]==2):
                    start=(i,j)
                if(room[i][j]==3):
                    goal=(i,j)


    heuristic = []

    for i in range(0, len(room)-1):
    	new = []
    	for j in range(0,len(room[0])-1):
    		fScore = (((i - goal[0]) ** 2) + ((j - goal[1]) **2)) + math.floor(math.sqrt(((i ** 2) + (j ** 2))))
    		new.append(fScore)
    	heuristic.append(new)
    
    ax = sns.heatmap(heuristic, annot=True, fmt="d")
    
    print(heuristic)

    # create figure displaying robot space
    fig, ax = plt.subplots(figsize=(8,8))
    ax.imshow(room, cmap=plt.cm.Dark2)
    ax.scatter(start[1],start[0], color = "blue", s = 200)
    ax.scatter(goal[1],goal[0],  color = "red", s = 200)
    plt.show()

    path = astar(room, start, goal)

    print(path)

    xCoord = []
    yCoord = []

    for i in (range(0,len(path))):
    	xCoord.append(path[i][0])
    	yCoord.append(path[i][1])

    # create figure displaying robot path through the space
    fig, ax = plt.subplots(figsize=(len(room[0]),len(room)))
    ax.imshow(room, cmap=plt.cm.Dark2)
    ax.scatter(start[1],start[0], color = "blue", s = 200)
    ax.scatter(goal[1],goal[0],  color = "red", s = 200)
    ax.plot(yCoord, xCoord)
    plt.title('A_Star reached the end position in '+str(len(path))+' moves')
    plt.show()

    
    
if __name__ == '__main__':
    main()
















