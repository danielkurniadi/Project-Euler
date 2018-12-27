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
            print(p)
            break

if __name__ == '__main__':
# Logics for numbers in vector v_even:
    # upperbound: 999,999 <= 999x999 = 998001, hence largest palindrom = 997799
    # lowerbound_odd: 99,999 <= 317x317
    # lowerbound_even: 100x100 = 10,000 (no need)
    v_even = np.arange(317, 997)[::-1]

    # from v_even, create u_even which is a mirror of v_even, then create palindrome numbers
    u_even = (v_even//100) + (v_even%10 *99) + (v_even% 100); #print(u_even);
    palindromes = v_even*1000 + u_even

    findLargest_Po3_Palindrome(palindromes, v_even)

