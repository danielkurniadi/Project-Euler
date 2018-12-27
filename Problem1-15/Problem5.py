import numpy as np
import math

def checkPrime(n):
    if n==2 or n==3 or n==5:
        return True
    if n==4:
        return False
    upper_bound = int(math.sqrt(n))+1
    return np.all(1* (n% np.arange(2, upper_bound) !=0))

def main(a, b):
    """
    Problem 5:
        2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
        What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    """
    if a==1:
        a = 2
    v_divisors = np.arange(a, b+1)
    v_primes = np.array([x for x in v_divisors if checkPrime(x)])
    v_exponents = np.floor(np.log(b)/np.log(v_primes))
    result_factors = np.power(v_primes, v_exponents)
    result = np.prod(result_factors)
    print(result)

if __name__ == '__main__':
    a = 1 #from 1
    b = 20 # to 20
    main(a, b)