
import copy



def searchTwoDimention(item, value):
    for indexi, valuei in enumerate(item):
        for indexj, valuej in enumerate(valuei):
            if valuej == value:
               return (indexi, indexj) 

def getInputs(x_dimension):
    return [list(input()) for i in range(x_dimension)] 

class Node:
    def __init__(self, state, indexi, indexj):
        self.state = state
        self.indexi = indexi
        self.indexj = indexj
    def validActions(self, untried):
        x_len = len(self.state[1]) - 1
        y_len = len(self.state) - 1
        if self.indexj > 0 :
            if  state[self.indexi][self.indexj - 1] != "#":
                untried.append("L")
            
        if self.indexi < y_len :
            if  state[self.indexi + 1][self.indexj] != "#":
                untried.append("D")

        if self.indexj < x_len :
            if state[self.indexi][self.indexj + 1] != "#":
                untried.append("R")

        if  self.indexi > 0 :
            if state[self.indexi - 1][self.indexj] != "#":
                untried.append("U")
    
    def setAction(self, a):
        newState = self.state 
        if a == 'U':
            if newState[self.indexi - 1][self.indexj] == "G":
                newState[self.indexi - 1][self.indexj] = "AG"
                newState[self.indexi][self.indexj] = '.'
            else:
                newState[self.indexi][self.indexj], newState[self.indexi - 1][self.indexj] =  newState[self.indexi - 1][self.indexj], newState[self.indexi][self.indexj]            
            self.indexi -= 1

        elif a == 'R':
            if newState[self.indexi][self.indexj + 1] == "G":
                newState[self.indexi][self.indexj + 1] = "AG"
                newState[self.indexi][self.indexj] = '.'
            else:
                newState[self.indexi][self.indexj], newState[self.indexi][self.indexj + 1] =  newState[self.indexi][self.indexj + 1], newState[self.indexi][self.indexj]
            self.indexj += 1
            
        elif a == "D":
            if newState[self.indexi + 1][self.indexj] == "G":
                newState[self.indexi + 1][self.indexj] = "AG"
                newState[self.indexi][self.indexj] = '.'
            else:
                newState[self.indexi][self.indexj], newState[self.indexi + 1][self.indexj] =  newState[self.indexi + 1][self.indexj], newState[self.indexi][self.indexj]
            self.indexi += 1
            
        elif a == "L":
            if newState[self.indexi][self.indexj - 1] == "G":
                newState[self.indexi][self.indexj - 1] = "AG"
                newState[self.indexi][self.indexj] = '.'
            else:
                newState[self.indexi][self.indexj], newState[self.indexi][self.indexj - 1] =  newState[self.indexi ][self.indexj - 1], newState[self.indexi][self.indexj]
            self.indexj -= 1
            
            
class OnlineSearch:
    def __init__(self, initialState):
        indexi,indexj = searchTwoDimention(initialState, 'A')
        self.initial = (Node(initialState, indexi, indexj))

    def gridword(self):
        node = self.initial
        parentNode = None;
        a = None
        result = dict()
        untried = dict()
        unbacktracked = dict()
        traceActions = []
        while True:
            if self.isGoal(node):
                return self.display(traceActions, True)
            if str(node.state) not in untried.keys():
                untried[str(node.state)] = []
                node.validActions(untried[str(node.state)])
                
            if parentNode != None:
                if str(parentNode.state) not in result.keys() :
                    result[str(parentNode.state)] = dict()
                result[str(parentNode.state)][a] = copy.deepcopy(node.state)
                if str(node.state) not in unbacktracked.keys():
                    unbacktracked[str(node.state)] = []
                unbacktracked[str(node.state)].append(copy.deepcopy(parentNode))
            if untried[str(node.state)] == None or len(untried[str(node.state)]) == 0:
                if str(node.state) not in unbacktracked.keys() :
                    return self.display(traceActions, False)
                elif len(unbacktracked[str(node.state)]) == 0:
                    return self.display(traceActions, False)
                
                statePoped = unbacktracked[str(node.state)].pop()
                test = False
                for key in result[str(node.state)]:
                    if str(result[str(node.state)][key]) == str(statePoped.state):
                        test = True
                        a = key
                        traceActions.append(key)
                        parentNode = None 
                        node.setAction(a)
                        break
                if test:
                    continue

            else:
                a = untried[str(node.state)].pop()
                traceActions.append(a)
            parentNode = copy.deepcopy(node)    
            node.setAction(a)
                    
    def isGoal(self, node):
        if node.state[node.indexi][node.indexj] == "AG":
            return True
        else:
            return False
    def display(self, actions, status):
        msg = ''
        for i in actions:
            msg = f"{msg}{i} "
        msg = f"{msg}\nGoal reached" if status else f"{msg}\nstopped"

        return msg
        
x_dimension, y_dimension = [eval(i) for i in input().split(' ')]

state = getInputs(x_dimension)
algorithm  = OnlineSearch(state)
print(algorithm.gridword())