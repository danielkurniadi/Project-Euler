import math 

def twoPointerSearch(arr, n, k=None):
    if len(arr) ==0:
        return []
    i = 0
    j = len(arr)-1
    if k:
        j = k-1
    args_sols = [] #index of solution pairs
    while(i<=j):
        a_2 = arr[i]
        b_2 = arr[j]
        if a_2 + b_2 == n:
            args_sols.append((i, j))
            i += 1
            j -= 1
        elif a_2 + b_2 > n:
            j -= 1
        else:
            i += 1
    return args_sols

def pythagorean_brute(n):
    k = n
    squares = [i**2 for i in range(0, k+1)]
    triplet = []
    while k > 0:
        c_2 = squares[k]
        py_pairs = twoPointerSearch(squares, c_2, k)
        for pair in py_pairs:
            i, j = pair
            if n== i+j+k:
                return (i, j, k)
        k -= 1
    else:
        return (-1, -1, -1)

def pythagorean_fast(n=1000):
    k = n//2
    for b in range(1, n//2+1):
        if (500-b)*1000%(1000-b) ==0 :
            a = (500-b)*1000/(1000-b)
            c = 1000-b-a
            return a, b, c

def main():
    # triplet = pythagorean_brute(1000)
    triplet = pythagorean_fast()
    i, j, k = triplet
    print(triplet, i*j*k)

if __name__ == '__main__':
    main()