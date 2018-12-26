import numpy as np

def sqrt_int(n):
    # bin search
    start, end = 1, n
    mid = (1+n)//2
    while(start<=end):
        mid = (start+end)//2
        if (mid-1)*(mid+1)<=n and mid*mid>=n:
            return mid
        elif mid*mid<n:
            start = mid+1
        else:
            end = mid-1
    return mid

def solve(n):
    for i in range(sqrt_ceil(n), 1, -1):
        #TODO: if all is False, then confirm this is prime.
        if 1*(i % np.arange(2, sqrt_int(i)) ==0).all():
            return i


if __name__ == '__main__':
    tests = [2, 3, 4, 5, 16, 20, 36, 139, 1025]
    for t in tests:
        print(t, sqrt_int(t))