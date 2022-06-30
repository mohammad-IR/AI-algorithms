
from asyncio import new_event_loop
import copy
from heapq import heappush, heappop

 
def getInputs(dimension, value):
    array = [eval(i) for i in value]
    return [array[i : i + dimension] for i in range(0, dimension * dimension, dimension)] 
def searchTwoDimention(item, value):
    for indexi, valuei in enumerate(item):
        for indexj, valuej in enumerate(valuei):
            if valuej == value:
               return (indexi, indexj) 


class Node:
    def __init__(self, state, parent, depth, indexi, indexj, action):
        self.parent = parent
        self.state = state
        self.cost = (self.calcost() * 10) + depth
        self.depth = depth
        self.indexi = indexi
        self.indexj = indexj
        self.action = action
    def __lt__(self, other):
        return (self.cost) < (other.cost)
    def calcost(self):
        costNode = 0 
        lenState = len(self.state)
        for indexi, valuei in enumerate(self.state):
            for indexj, valuej in enumerate(valuei):
                if finalState[indexi][indexj] != valuej:
                    costNode += 1
        return costNode
    
    def checkInFrontier(self, node, frontier):
        for i in frontier:
            if i.state == node.state:
                if i.cost < node.cost:
                    heappush(frontier,node)
                    return True
        return False
    def checkNode(self,newState, reach, frontier):
        if str(newState.state) not in reach.keys() :
                reach[str(newState.state)] = newState
                heappush(frontier, newState)
        elif newState.depth < reach[str(newState.state)].depth:
                reach[str(newState.state)] = newState
                heappush(frontier, newState)
            
    def expandNode(self, reach, frontier):
        lenState = len(self.state) - 1
        reach[str(self.state)] = self
        if self.indexi > 0:
            newState = copy.deepcopy(self.state)
            newState[self.indexi][self.indexj], newState[self.indexi - 1][self.indexj] =  newState[self.indexi - 1][self.indexj], newState[self.indexi][self.indexj]
            newState = Node(newState, self, self.depth + 1, self.indexi - 1, self.indexj, 'U')
            self.checkNode(newState, reach, frontier)
                
        if self.indexj < lenState:
            newState = copy.deepcopy(self.state)
            newState[self.indexi][self.indexj], newState[self.indexi][self.indexj + 1] =  newState[self.indexi][self.indexj + 1], newState[self.indexi][self.indexj]
            newState = Node(newState, self, self.depth + 1, self.indexi, self.indexj + 1, 'R')
            self.checkNode(newState, reach, frontier)

                     
                     
        if self.indexi < lenState:
            newState = copy.deepcopy(self.state)
            newState[self.indexi][self.indexj], newState[self.indexi + 1][self.indexj] =  newState[self.indexi + 1][self.indexj], newState[self.indexi][self.indexj]
            newState = Node(newState, self, self.depth + 1, self.indexi + 1, self.indexj, 'D')
            self.checkNode(newState, reach, frontier)

                     
        if self.indexj > 0:
            newState = copy.deepcopy(self.state)
            newState[self.indexi][self.indexj], newState[self.indexi][self.indexj - 1] =  newState[self.indexi ][self.indexj - 1], newState[self.indexi][self.indexj]
            newState = Node(newState, self, self.depth + 1, self.indexi, self.indexj - 1, 'L')
            self.checkNode(newState, reach, frontier)

class AStar:
    def __init__(self, initialNode, finalNode):
        indexi, indexj = searchTwoDimention(initialNode, 0)
        self.initialNode = Node(state=initialNode, parent=None, depth=0, indexi=indexi, indexj=indexj, action='')
        self.finalNode = finalNode
    
    def AStarAlgorithm(self):
        reach = dict()
        frontier = list()
        if finalState == initialState:
            return "0\n"
        numberExpand = 0
        heappush(frontier, self.initialNode)
        while len(frontier) != 0:
            node = heappop(frontier)
            if node.state == self.finalNode:
                return self.display(node, numberExpand)
            node.expandNode(reach, frontier)
            numberExpand += 1 
        return self.display(None, numberExpand)
    
    

    def display(self, node, numberExapndNode):
        msg = ''
        if node == None:
            return f'{numberExapndNode - 1}\nno solution found'
        while node != None:
            msg = f'{node.action} {msg}'
            node = node.parent         
        msg = f'{numberExapndNode}\n{msg[1:]}'
        return msg
    

dimension = eval(input())
initialStateValue = input().split(' ')
finalStateValue = input().split(' ')

initialState = getInputs(dimension=dimension, value=initialStateValue)
finalState = getInputs(dimension=dimension, value=finalStateValue) 

aStar = AStar(initialState, finalState)
print(aStar.AStarAlgorithm())