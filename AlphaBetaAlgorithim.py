#implements the alpha beta algorithim for 
# tic tac toe playing


import copy


class node: #creates the tic tac toe node 
    
    def __init__(self,config,turn):
        self.config = config
        self.turn = turn
        
    def isTerminal(self): #determine if the game is finished 

        
        if self.config[0] =='X' and self.config[1]=='X' and self.config[2]=='X': #top three
            self.heuristicValue = 1
            return True
        elif self.config[3] =='X' and self.config[4]=='X' and self.config[5]=='X': #middle three
            self.heuristicValue = 1
            return True
        elif self.config[6] =='X' and self.config[7]=='X' and self.config[8]=='X': #bottom three
            self.heuristicValue = 1
            return True
            
            # vertical wins
        elif self.config[0] =='X' and self.config[3]=='X' and self.config[6]=='X': #first three
            self.heuristicValue = 1
            return True
        elif self.config[1] =='X' and self.config[4]=='X' and self.config[7]=='X': #second three
            self.heuristicValue = 1
            return True
        elif self.config[2] =='X' and self.config[5]=='X' and self.config[8]=='X': #last three
            self.heuristicValue = 1
            return True
        
              # Diagonal wins
        elif self.config[0] =='X' and self.config[4]=='X' and self.config[8]=='X': 
            self.heuristicValue = 1
            return True
        elif self.config[2] =='X' and self.config[4]=='X' and self.config[6]=='X':
            self.heuristicValue = 1
            return True
        
                #check if O wins
            # horizontal wins
        elif self.config[0] =='O' and self.config[1]=='O' and self.config[2]=='O': #top three
            self.heuristicValue = -1
            return True
        elif self.config[3] =='O' and self.config[4]=='O' and self.config[5]=='O': #middle three
            self.heuristicValue = -1
            return True
        elif self.config[6] =='O' and self.config[7]=='O' and self.config[8]=='O': #bottom three
            self.heuristicValue = -1
            return True
            
            # vertical wins
        elif self.config[0] =='O' and self.config[3]=='O' and self.config[6]=='O': #first three
            self.heuristicValue = -1
            return True
        elif self.config[1] =='O' and self.config[4]=='O' and self.config[7]=='O': #second three
            self.heuristicValue = -1
            return True
        elif self.config[2] =='O' and self.config[5]=='O' and self.config[8]=='O': #last three
            self.heuristicValue = -1
            return True
        
              # Diagonal wins
        elif self.config[0] =='O' and self.config[4]=='O' and self.config[8]=='O': 
            self.heuristicValue = -1
            return True
        elif self.config[2] =='O' and self.config[4]=='O' and self.config[6]=='O':
            self.heuristicValue = -1
            return True
        
        elif self.config.count('b') == 0: #cats game
            self.heuristicValue = 0
            return True
        else:
            return False


    def printBoard(self):
        string = ""
        index = -1
        for row in range(0,3):
            string+='\n'
            for col in range(0,3):
                index+=1
                if self.config[index] == 'b':
                    string+='|_|'
                else:
                    string+="|"+self.config[index]+"|"
                    
        print string
                
                



def createChildren(config,turn):

    copy_node = copy.copy(config)
    newChildren = []
    closedList = []
    returnList = []
    
    if turn == 'X':
        newTurn = 'O'
    if turn == 'O':
        newTurn = 'X'
    
    numChildren = config.count('b')
    
    for j in range(0,numChildren):
        copy_node = copy.copy(config)
        for i in range(0,9): #loop through board
            if copy_node[i] == 'b' and i not in closedList:
                closedList.append(i)
                if turn == 'X':
                    copy_node[i] = 'X'
                if turn == 'O':
                    copy_node[i] = 'O'  
                newChildren.append(copy_node)
                break
    
    #return as node object
    for child in newChildren:
        returnList.append(node(child,newTurn))
    
    return returnList
                
            
        




path = []

#implements the alpha beta algorithim
def alphaBeta(node,alpha,beta,maximizingPlayer):
    global path

    if node.isTerminal() == True:
        return node.heuristicValue
    if maximizingPlayer:
        #bestMove = None
        v = -100000000
        children = createChildren(node.config,node.turn)
        for child in children:
            v = alphaBeta(child,alpha,beta,False)
            if v > alpha:
                alpha = v
                bestMove = path.append(child.config)
            if alpha >= beta:
                break
            
        return alpha
    
    else:
        #bestMove = None
        v = 100000000
        children = createChildren(node.config,node.turn)
        for child in children:
            v = alphaBeta(child,alpha,beta,True)
            if v < beta:
                beta = v
                
            if alpha >= beta:
                break

        return beta
            


initialState = "b,b,b,X,O,b,b,b,b" #initial board configuration

initialTurn = 'X' #who plays first
initialState = initialState.split(',')
board = node(initialState,initialTurn)

newChildren = createChildren(board.config,board.turn)


a = alphaBeta(board,-100000000,100000000,True)
print 'initial board/state'
board.printBoard() #print initial board
b2 = node(path[len(path)-1],'X')
print '\nend game state'
b2.printBoard() #print final board