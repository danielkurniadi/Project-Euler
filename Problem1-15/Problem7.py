def nth_prime(n):
    count = 2
    i = 3
    while i:
        k = 1
        while k*k < i:
            k+= 2
            if i%k==0:
                break
        else:
            count+= 1
            if count== n:
                return i
        i+= 2

def main():
    x = nth_prime(10001)
    print(x)
if __name__ == '__main__':
    main()