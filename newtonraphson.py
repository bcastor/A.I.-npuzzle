'''
COURSE:        CS-550 Artificial Intelligence
SECTION:       01-MW 4:00-5:15pm
DATE:          02 March 2020
ASSIGNMENT:    03
@author Mariano Hernandez & Brandon Castor

'''

def NewtonRaphson(fpoly, a, tolerance = .00001):
    """
    Given a set of polynomial coefficients fpoly
    for a univariate polynomial function,
    e.g. (3, 6, 0, -24) for 3x^3 + 6x^2 +0x^1 -24x^0,
    find the real roots of the polynomial (if any)
    using the Newton-Raphson method.
    
    a is the initial estimate of the root and
    starting state of the search
    
    This is an iterative method that stops when the
    change in estimators is less than tolerance.
    """
    #divide the polynomial by its derivative with an input a
    n = (polyval(fpoly,a) / polyval(derivative(fpoly),a))

    #stop when n is less than the tolerance, root has been found
    while abs(n) >= tolerance:
        n = (polyval(fpoly,a) / polyval(derivative(fpoly),a))
        a = a - n  #x0 - n
        
    print(a)
    
    
def polyval(fpoly, x):
    """FUNCTION polyval
    Returns the value of the a polynomial function of a given
    set of polynomial coefficients (fpoly) in order from highest order to x^0,
    compute the value of the polynomial at x. We assume zero
    coefficients are present in the coefficient list/tuple.
    
    Args:
        fpoly -- list or tuple of coefficients  
        x -- variable to be computed for the function
    
    Returns:
        result -- the 
    
    Ex.: f(x) = 4x^3 + 0x^2 + 9x^1 + 3 evaluated at x=5
    polyval([4, 0, 9, 3], 5)
    returns 548
    
    """
    # retrieve the highest degree polynomial into exp
    exp = len(fpoly)-1
    
    # retrieve the result of the polynomial function,
    # given a value x
    result = 0 
    for i in range(len(fpoly)):
        result = result + fpoly[i]*pow(x,exp)
        exp = exp-1
    
    return result
    
    
def derivative(fpoly):
    """
    Given a set of polynomial coefficients from highest order to x^0,
    compute the derivative polynomial. We assume zero coefficients
    are present in the coefficient list/tuple.
    
    Returns polynomial coefficients for the derivative polynomial.
    Example:
    derivative((3,4,5)) # 3 * x**2 + 4 * x**1 + 5 * x**0
    returns: [6,4] #6*x**1+4*x**0
    """
    
    # return value result
    # exp value
    result = []
    exp = len(fpoly)-1
    
    # loop until it reaches the end of the list 
    #     n = fpoly[i] * exp
    #     result.append(n)
    #     exp--
    #     if n == 0 {do not append}
    # return result
    for i in range(len(fpoly)):
        n = fpoly[i]*exp
        if n == 0:
            return result
        result.append(n)
        exp = exp -1
    return result
    
    
