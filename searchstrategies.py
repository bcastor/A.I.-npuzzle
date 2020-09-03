'''
COURSE:        CS-550 Artificial Intelligence
SECTION:       01-MW 4:00-5:!5pm
DATE:          02 March 2020
ASSIGNMENT:    03
@author Mariano Hernandez & Brandon Castor

'''

from basicsearch_lib02.searchrep import Node
from basicsearch_lib02.tileboard import TileBoard


class BreadthFirst:
    k = 0
    @classmethod
    def g(cls, parentnode, action, childnode):
        
        return len(childnode.path())
    
    
    @classmethod
    def h(cls, state):
        return cls.k

class DepthFirst:

    @classmethod
    def g(cls, parentnode, action, childnode):
        
        return (-1 * parentnode.depth - 1)

    @classmethod
    def h(cls, state):
        return 0
    

class A_Manhattan:
    @classmethod
    def g(cls, parentnode, action, childnode):
                
        return (2 + parentnode.depth)
    
    @classmethod
    def h(cls, state):
      
        return 1
    