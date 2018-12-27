import math

def faulhaber_3(n, a=1):
    if n==0 or n==1:
        return n
    if a==1 or a==0:
        return (n*(n+1)*(2*n+1))/6
    else:
        a = a-1
        return (n*(n+1)*(2*n+1))/6 - (a*(a+1)*(2*a+1))/6

def faulhaber_2(n, a=1):
    if n==0 or n==1:
        return n
    if a==1 or a==0:
        return (n*(n+1))/2
    else:
        a = a-1
        return (n*(n+1))/2 - (a*(a+1))/2

def main():
"""
    The sum of the squares of the first ten natural numbers is,
        12 + 22 + ... + 102 = 385
        The square of the sum of the first ten natural numbers is,
        (1 + 2 + ... + 10)2 = 552 = 3025
        Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

    Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
    # solutions:
    b=100
    f_2 = faulhaber_2(b, a=1)
    f_3 = faulhaber_3(b, a=1)
    print(f_2**2 - f_3)

if __name__ == '__main__':
    main()