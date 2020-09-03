'''
COURSE:        CS-550 Artificial Intelligence
SECTION:       01-MW 4:00-5:!5pm
DATE:          02 March 2020
ASSIGNMENT:    03
@author Mariano Hernandez & Brandon Castor

'''

from statistics import (mean, stdev)  # Only available in Python 3.4 and newer

from npuzzle import NPuzzle
from basicsearch_lib02.tileboard import TileBoard
from searchstrategies import (BreadthFirst, DepthFirst, A_Manhattan)
from problemsearch import graph_search
import collections
import time

TRIAL = 31
BOARD_SIZE = 8
SEARCH_METHODS = [BreadthFirst, DepthFirst, A_Manhattan]


      


def driver():

    p_size = dict()
    n_size = dict()
    t = dict()

    for method in SEARCH_METHODS:
        t[method] = list()
        n_size[method] = list()
        p_size[method] = list()
        
       

    for i in range(TRIAL):

        board_layout = TileBoard(BOARD_SIZE).state_tuple()

        for method in SEARCH_METHODS:

            p = NPuzzle(BOARD_SIZE, g=method.g,h=method.h, force_state=board_layout)

            start_time = time.perf_counter()
                                      
            path, nodes_explored = graph_search(p)
                        
            dur = time.perf_counter() - start_time
            
            n_size[method].append(nodes_explored)
            
            t[method].append(dur)
            
            p_size[method].append(len(path))
            
            print('Trial %d via %s - plan %d node %d in %d seconds' %((i+1), method.__name__, len(path), nodes_explored, dur))



    for method in SEARCH_METHODS:
        
        print('Plan Method %s Mean %f Std %f' %(method.__name__, mean(p_size[method]), stdev(p_size[method])))
        print('Nodes Method %s Mean %f Std %f' %(method.__name__, mean(n_size[method]), stdev(n_size[method])))
        print('Time Method %s Mean %f Std %f' %(method.__name__, mean(t[method]), stdev(t[method])))
    


if __name__ == '__main__':
    driver()