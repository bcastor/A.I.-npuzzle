'''
COURSE:        CS-550 Artificial Intelligence
SECTION:       01-MW 4:00-5:!5pm
DATE:          02 March 2020
ASSIGNMENT:    03
@author Mariano Hernandez & Brandon Castor

'''

from collections import deque
from explored import Explored
from basicsearch_lib02.queues import PriorityQueue
from basicsearch_lib02.searchrep import (Node, Problem)



def graph_search(problem, verbose=False, debug=False):
    """graph_search(problem, verbose, debug) --
    Given a problem representation (instance of basicsearch_lib02.representation.
    Problem or derived class), attempt to solve the problem.
    
    If debug is True, debugging information will be displayed.
    
    if verbose is True, the following information will be displayed:
        
        Number of moves to solution
        List of moves and resulting puzzle states
        Example:
        
            Solution in 25 moves        
            Initial state
                  0        1        2    
            0     4        8        7    
            1     5        .        2    
            2     3        6        1    
            Move 1 -  [0, -1]
                  0        1        2    
            0     4        8        7    
            1     .        5        2    
            2     3        6        1    
            Move 2 -  [1, 0]
                  0        1        2    
            0     4        8        7    
            1     3        5        2    
            2     .        6        1    
            
            ... more moves ...
            
                  0        1        2    
            0     1        3        5    
            1     4        2        .    
            2     6        7        8    
            Move 22 -  [-1, 0]
                  0        1        2    
            0     1        3        .    
            1     4        2        5    
            2     6        7        8    
            Move 23 -  [0, -1]
                  0        1        2    
            0     1        .        3    
            1     4        2        5    
            2     6        7        8    
            Move 24 -  [1, 0]
                  0        1        2    
            0     1        2        3    
            1     4        .        5    
            2     6        7        8    
        
        If no solution were found (not possible with the puzzles we
        are using), we would display:
        
            No solution found
    
    Returns a tuple (path, nodes_explored) where:
    path - list of actions to solve the problem or None if no solution was found
    nodes_explored - Number of nodes explored (dequeued from frontier)
    """
    
    # PriorityQueue should be used to maintain the order of the queue.
    frontier = PriorityQueue()
    
    frontier.append(Node(problem, problem.initial))
    
    current_node = frontier.pop()
    
    p = True
    #depth first search
    if current_node.expand(current_node.problem)[0].g < 0:
        
        frontier = deque()
        frontier.append(Node(problem, problem.initial))
    #breadth first search
    elif current_node.expand(current_node.problem)[0].h < 2:
        
        p = False
        frontier = deque()
        frontier.append(Node(problem, problem.initial))
    #manhattan
    else:
        
        frontier.append(current_node)

    f_hash = Explored()
    f_hash.add(problem.initial.state_tuple())
    done = False
    n_explored = 0
    explored = Explored()

    #graph_search
    while not done:
        
        if p:
            current_node = frontier.pop()
        else:
            current_node = frontier.popleft()
        explored.add(current_node.state.state_tuple())
        n_explored = n_explored + 1 #inc the number of explored nodes

        if current_node.state.solved():
            path = current_node.path()
            done = True
            return path, n_explored
        #if not found in the tree return none and number of nodes explored
        else:
            
            for child in current_node.expand(current_node.problem):
                if not explored.exists(child.state.state_tuple()) and not \
                        f_hash.exists(child.state.state_tuple()):
                    frontier.append(child)
                    f_hash.add(child)
            done = len(frontier) == 0

    return None, n_explored
