import numpy as np
import time

#  Maze size
sizex=4
sizey=6


class Node:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.next=None

class TraceRecord:
    steps=0
    def __init__(self):
        self.first=None
        self.last=None
        
    def isEmpty(self):
            return self.first==None

    def insert(self,x,y):
        newNode=Node(x,y)
        if self.first==None:
            self.first=newNode
            self.last=newNode
        else:
            self.last.next=newNode
            self.last=newNode
        self.steps+=1

        
    def delete(self): # delete node
        if self.first==None:
            print("Stack is empty")
            return
        if self.first == self.last:
            print("can not arrive everywhere")
            time.sleep(1000000)
            return
        newNode=self.first
        while newNode.next!=self.last:
            newNode=newNode.next
        newNode.next=self.last.next
        self.last=newNode
        self.steps-=1
        

maze=np.zeros((sizex,sizey),dtype=np.uint8)


prime=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311]
# record all of the failure strategy
failure=[] #O(N?)may need optimization

# used to be convert strategies to a simple number
def hashGenerator(HEAD,LAST):
    hashValue=0
    ptr=HEAD
    for step in range(1,sizex*sizey+1):
        if(ptr==None):
            break
        hashValue+=prime[ptr.x+1+sizex]*prime[ptr.y+1+sizex+sizex]*prime[step] # add sizex to avoid collision
        if(ptr != LAST):
            ptr=ptr.next
        else:
            break
    return hashValue
x=0
y=0

path=TraceRecord()

def check(x,y,currentHash):
    if(x<sizex and x>=0 and y<sizey and y>=0 and maze[x][y]==0):
        if(currentHash+prime[x+1+sizex]*prime[y+1+sizex+sizex]*prime[path.steps+1] not in failure):
            return 1
    return 0
def checkEnd():
    if(path.steps==sizex*sizey ):
        return 1
    return 0

def ShowMaze(maze):
    for i in range(sizex):
        for j in range(sizey):
            print(" "+str(maze[i][j]),end="")
        print()
    print("----------------")

path.insert(x,y)
while(True):
    maze[x][y]=1
    currentHash=hashGenerator(path.first,path.last)
    if(check(x+2,y+1,currentHash)): # knight move
        x+=2
        y+=1
        path.insert(x,y)
    elif(check(x+1,y+2,currentHash)):
        x+=1
        y+=2
        path.insert(x,y)
    elif(check(x-1,y+2,currentHash)):
        x-=1
        y+=2
        path.insert(x,y)
    elif(check(x-2,y+1,currentHash)):
        x-=2
        y+=1
        path.insert(x,y)
    elif(check(x-2,y-1,currentHash)):
        x-=2
        y-=1
        path.insert(x,y)
    elif(check(x-1,y-2,currentHash)):
        x-=1
        y-=2
        path.insert(x,y)
    elif(check(x+1,y-2,currentHash)):
        x+=1
        y-=2
        path.insert(x,y)
    elif(check(x+2,y-1,currentHash)):
        x+=2
        y-=1
        path.insert(x,y)
    elif(checkEnd()):
        print("found")
        time.sleep(1.3)
        break
    else:
        failure.insert(0,hashGenerator(path.first,path.last))
        maze[x][y]=0
        path.delete()
        x=path.last.x
        y=path.last.y
    '''
    print("x:",x)
    print("y:",y)
    print("step:",path.steps)
    '''

    '''
    for i in range(10):
        if(i<len(failure)):
            print(failure[i])
    '''
    #time.sleep(0.2) 
    
    
    
 
    
maze=np.zeros((sizex,sizey),dtype=np.uint8)

ptr=path.first
while(True):
    maze[ptr.x][ptr.y]=1
    ShowMaze(maze)
    if(ptr.next !=None):
        ptr=ptr.next
    else:
        break
    time.sleep(0.8)
    