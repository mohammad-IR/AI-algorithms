import copy
from queue import LifoQueue

def getInputs(dimension, value):
    array = [eval(i) for i in value]
    return [array[i : i + dimension] for i in range(0, dimension * dimension, dimension)] 


class IDS:
    def __init__(self, initialState, finalState):
        self.initialState = initialState
        self.finalState = finalState
    
    
    def __getIndexZero(self, state):
        for indexi, i in enumerate(state):
            for indexj, j in enumerate(i):
                if j == 0:
                    return (indexi, indexj)
    
    def getSloution(self):
        depth = 0
        expandedNode = [0]
        indexi, indexj = self.__getIndexZero(self.initialState)
        while(True):
            reach = set()
            result = self.__depthFirstSearch(depth, indexi, indexj, expandedNode)
            if result == "depth limited":
                depth += 1 
            elif result == "not found":
                return self.__DisplayResult(None, expadedNode=expandedNode[0])
            else:
                return self.__DisplayResult(result, expadedNode=expandedNode[0])
    
    def __depthFirstSearch(self, depth, indexi, indexj, expandedNode):
        frontier = LifoQueue()
        frontier.put({'data' : self.initialState, 'action' : '','parent': set() ,'indexi' : indexi, 'indexj' : indexj, 'depth' : 0})
        cuttof = False
        reach = set()
        while(not(frontier.empty())):
            node = frontier.get()
            if node['data'] == self.finalState: 
                return node
            if node['depth'] > depth:
                cuttof = True
            elif str(node['data']) not in node['parent']:
                reach.add(str(node['data']))
                self.__expandNode(node, frontier, depth=depth)
                expandedNode[0] +=1
        if cuttof:
            return "depth limited"
        
        return "not found"
            
    def __expandNode(self, state, queue, depth):
        lenState = len(state['data']) - 1
        indexi = state['indexi']
        indexj = state['indexj']

        if indexi > 0 :
            newState =copy.deepcopy(state['data'])
            newState[indexi][indexj], newState[indexi - 1][indexj] =  newState[indexi - 1][indexj], newState[indexi][indexj]
            newState = {'data' : newState , 'action' : state['action'] + 'U ', 'indexi' : indexi - 1, 'indexj':indexj , 'depth' : state['depth'] + 1}
            newState['parent'] =  state['parent'].union({str(state['data'])})
            queue.put(newState)
                
        if indexj < lenState :
            newState =copy.deepcopy(state['data'])
            newState[indexi][indexj], newState[indexi ][indexj + 1] =  newState[indexi ][indexj + 1], newState[indexi][indexj]
            newState = {'data' : newState, 'action':state['action'] +  'R ' , 'indexi' : indexi, 'indexj':indexj + 1, 'depth' : state['depth'] + 1}
            newState['parent'] =   state['parent'].union({str(state['data'])})
            queue.put(newState)              
                
                
        if indexi < lenState :
            newState =copy.deepcopy(state['data'])
            newState[indexi][indexj], newState[indexi + 1][indexj] =  newState[indexi + 1][indexj], newState[indexi][indexj]
            newState = {'data' : newState, 'action':  state['action']+ 'D ', 'indexi' : indexi + 1, 'indexj':indexj, 'depth' : state['depth'] + 1 }
            newState['parent'] =   state['parent'].union({str(state['data'])})
            queue.put(newState)              
        
        if indexj > 0 :
            newState = copy.deepcopy(state['data'])
            newState[indexi][indexj], newState[indexi ][indexj - 1] =  newState[indexi ][indexj- 1], newState[indexi][indexj]
            newState = {'data' : newState, 'action':  state['action'] + 'L ', 'indexi' : indexi, 'indexj':indexj - 1, 'depth' : state['depth'] + 1}
            newState['parent'] =   state['parent'].union({str(state['data'])})
            queue.put(newState)
                

    
    def __DisplayResult(self, stateResult, expadedNode):
        monitor = ''
        if stateResult:
            action = stateResult['action']
            monitor = f'{expadedNode}\n{action}'  
        
        else:
            message = "No solution found"
            monitor = f'{expadedNode}\n{message}' 
                
        return monitor            
 
    def __cycle(self, node):
        parent = copy.deepcopy(node)
        parent = parent['parent']
        while parent != None:
            if parent['data'] == node['data'] :
                return False
            parent = parent['parent']
        return True
                


dimension = eval(input())
initialState = input().split(' ')
finalState = input().split(' ')
initialState = getInputs(dimension=dimension, value=initialState)
finalState = getInputs(dimension=dimension, value=finalState)

nPazzle = IDS(initialState, finalState)
print(nPazzle.getSloution())

