'''
COURSE:        CS-550 Artificial Intelligence
SECTION:       01-MW 4:00-5:15pm
DATE:          02 March 2020
ASSIGNMENT:    03
@author Mariano Hernandez & Brandon Castor

'''
import newtonraphson as nr

def nrapshondriver():
    print("Newton Raphson:")
    print()
    
    print("The closest root when inputting an estimate value of 5")
    print("into the function: 7x^4 + 3x^3 - 5x^2 + 32x - 7, is")
    nr.NewtonRaphson([7, 3, -5, 32, -7], 5)
    
    print("The closest root when inputting an estimate value of -50")
    print("into the function: 7x^4 + 3x^3 - 5x^2 + 32x - 7, is")
    nr.NewtonRaphson([7, 3, -5, 32, -7], -50)
    

if __name__ == '__main__':
    nrapshondriver()

