import numpy as np
import math

# TODO: Largest palindrome made from product of two 3-digits numbers
def _largestFactor(n, v):
    v_divisor = v* (n% v ==0)
    return v_divisor.max()

def findLargest_Po3_Palindrome(palindromes, v):
    for p in palindromes:
        max_divisor = _largestFactor(p, v).max()
        square_root = int(math.sqrt(p))

        if max_divisor>square_root:
            print("The largest palindrome which is a product of two 3-digits number: "p)
            print("The two 3-digit factors are:" max_divisor, p//max_divisor)
            break

if __name__ == '__main__':
""" 
  Logical thinking for numbers in vector v:
    - upperbound: 999,999 <= 999x999 = 998001, hence largest palindrom = 997799
    - lowerbound_odd: 99,999 <= 317x317
    - lowerbound_even: 100x100 = 10,000 (no need)  
  The range of number is still hardcoded for factor.n_digit = 3
"""
    v = np.arange(317, 997)[::-1]

    # from v, create u which is a mirror of v, then create palindrome numbers
    u = (v//100) + (v%10 *99) + (v% 100); #print(u);
    palindromes = v*1000 + u

    findLargest_Po3_Palindrome(palindromes, v)

