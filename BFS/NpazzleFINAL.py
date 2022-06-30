
import copy
from time import time
from queue  import Queue
def getInputs(dimension, value):
    array = [eval(i) for i in value]
    return [array[i : i + dimension] for i in range(0, dimension * dimension, dimension)] 


class NPazzle:
    def __init__(self, initialState, finalState):
        self.initialState = initialState
        self.finalState = finalState


    def getFinalState(self):
        queue , reach = Queue(),set()
        expandedNode = [0]
        if self.initialState == self.finalState:
            return 0
        
        for indexi, i in enumerate(self.initialState):
            for indexj, j in enumerate(i):
                if j == 0:            
                    queue.put({'data' : self.initialState, 'action': '', 'indexi': indexi, 'indexj': indexj})
                    reach.add(str(self.initialState))
                    break
        
        while(not queue.empty()):
            result = self.__expandNode(queue.get(), queue, reach, expandedNode)
            if(result):
                break
        return self.__DisplayResult(result, expandedNode[0])        
            
    def __expandNode(self, state, queue, reach, expandedNode):
        expandedNode[0] += 1
        newState = copy.deepcopy(state['data'])
        lenState = len(state['data']) - 1
        indexi = state['indexi']
        indexj = state['indexj']
        if indexi > 0 :
            newState[indexi][indexj], newState[indexi - 1][indexj] =  newState[indexi - 1][indexj], newState[indexi][indexj]
            if  "".join(str(newState)) not in reach :                        
                reach.add(str(str(newState)))
                queue.put({'data' : newState , 'action' : state['action'] + 'U ', 'indexi' : indexi - 1, 'indexj':indexj })
                if newState == self.finalState:
                    return {'data' : newState , 'action' : state['action'] + 'U ', 'indexi' : indexi - 1, 'indexj':indexj }
                
            
            
                
        if indexj < lenState :
            newState =copy.deepcopy(state['data'])
            newState[indexi][indexj], newState[indexi ][indexj + 1] =  newState[indexi ][indexj + 1], newState[indexi][indexj]
            
            if  "".join(str(newState)) not in reach :            
                reach.add(str(str(newState)))  
                queue.put({'data' : newState,  'action':state['action'] +  'R ' , 'indexi' : indexi, 'indexj':indexj + 1})              
                if newState == self.finalState:
                    return {'data' : newState,  'action':state['action'] +  'R ' , 'indexi' : indexi, 'indexj':indexj + 1}
                

        if indexi < lenState :
            newState =copy.deepcopy(state['data'])
            newState[indexi][indexj], newState[indexi + 1][indexj] =  newState[indexi + 1][indexj], newState[indexi][indexj]
            if  "".join(str(newState)) not in reach :            
                reach.add(str(str(newState)))
                queue.put({'data' : newState,  'action':  state['action']+ 'D ', 'indexi' : indexi + 1, 'indexj':indexj })
                if newState == self.finalState:
                    return {'data' : newState,  'action':  state['action']+ 'D ', 'indexi' : indexi + 1, 'indexj':indexj }
                
            

            
        if indexj > 0 :
            newState =copy.deepcopy(state['data'])
            newState[indexi][indexj], newState[indexi ][indexj - 1] =  newState[indexi ][indexj- 1], newState[indexi][indexj]
            if  str(str(newState)) not in reach :
                reach.add(str(str(newState)))  
                queue.put({'data' : newState,  'action':  state['action'] + 'L ', 'indexi' : indexi, 'indexj':indexj - 1})
                if newState == self.finalState:
                    return {'data' : newState,  'action':  state['action'] + 'L ', 'indexi' : indexi, 'indexj':indexj - 1}
                
                
        return False
    
    def __DisplayResult(self, stateResult, expadedNode):
        monitor = ''
        if stateResult:
            action = stateResult['action']
            monitor = f'{expadedNode}\n{action}'  
        
        else:
            message = "no solution found"
            monitor = f'{expadedNode}\n{message}' 
                
        return monitor            
                        
dimension = eval(input())
initialStateValue = input().split(' ')
finalStateValue = input().split(' ')

initialState = getInputs(dimension=dimension, value=initialStateValue)
finalState = getInputs(dimension=dimension, value=finalStateValue)
nPazzle = NPazzle(initialState, finalState)
print(nPazzle.getFinalState())
