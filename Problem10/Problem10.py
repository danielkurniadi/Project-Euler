import numpy as np
import math

def sieve_primes(n):
    if n < 20:
        return np.array([2, 3, 5, 7], dtype = "int64")
    sqr_n = int(math.sqrt(n))
    v_primes = sieve_primes(sqr_n)
    v_numb = np.arange(sqr_n, n+1)
    u_primes = np.array([ np.all(k % v_primes != 0) for k in v_numb])*v_numb
    u_primes = u_primes[u_primes!=0]
    u_primes = np.concatenate((v_primes, u_primes), axis=None)
    return(u_primes)

def main():
    primes = sieve_primes(2000000)
    sum_prime = primes.sum()
    print(sum_prime)
    np.savetxt("primes_list.txt", primes, fmt="%d", delimiter=' ')

if __name__ == '__main__':
    main()