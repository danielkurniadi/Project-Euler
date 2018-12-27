import numpy as np

def solve_forloop(n):
    f_1 = 1
    f_2 = 1
    sum = 0
    while f_2 <= n:
        if f_2%2==0:
            sum += f_2
        f_1, f_2 = f_2, f_1 + f_2
    return sum

if __name__ == '__main__':
    print(solve_forloop(4000000))