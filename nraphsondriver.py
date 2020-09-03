'''
Created on Feb 21, 2020

@author: marianohernandez
'''
import newtonraphson as nr

def nrapshondriver():
    print("Newton Raphson:")
    print()

    nr.NewtonRaphson([3,6,0,-24], 20)
    #print("Returns: ",n)

if __name__ == '__main__':
    nrapshondriver()