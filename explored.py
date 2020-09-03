'''
COURSE:        CS-550 Artificial Intelligence
SECTION:       01-MW 4:00-5:!5pm
DATE:          02 March 2020
ASSIGNMENT:    03
@author Mariano Hernandez & Brandon Castor

'''


class Explored(object):
    "Maintain an explored set.  Assumes that states are hashable"
    
    def __init__(self):
        "__init__() - Create an empty explored set"
        self.explored_set = {}
    
    
    def exists(self, state):
        """exists(state) --
        Determine whether or not a state has been explored
        
        Argument - hashable state
        Return - True if state in explored_set; or False if not
        """
        
        try:
            return state in self.explored_set[state.__hash__()]
        except KeyError:
            return False
    
    
    def add(self, state):
        """add(state) - add given state to the explored set.  
        state must be hashable and we asssume that it is not already in set
        """
        # The hash function is a Python builtin that generates
        # a hash value from its argument.  Use this to create
        # a dictionary key.  Handle collisions by storing 
        # states that hash to the same key in a bucket list.
        # Note that when you access a Python dictionary by a
        # non existant key, it throws a KeyError
        
        # if the hash key of the given state is not in this
        # explored instance's set of keys
        if state.__hash__() not in self.explored_set.keys():
            # create a new set for the particular hash key
            self.explored_set[state.__hash__()] = set()
        # then just add the state to the set of the
        # particular hash key
        self.explored_set[state.__hash__()].add(state)
        
        