import numpy as np
import time
import math

def solve(n):
    upper_bound = int(math.sqrt(n))+1
    for i in range(upper_bound, 1, -1):
        if (n%i ==0) and checkPrime(i):
            return i
    
def checkPrime(n):
    if n==2 or n==3 or n==5:
        return True
    if n==4:
        return False
    upper_bound = int(math.sqrt(n))+1
    return (1* (n% np.arange(2, upper_bound) !=0))

def test_solution(n, func): 
    x = func(n)
    print(x)

if __name__ == '__main__':
    test_solution(600851475143, solve)
