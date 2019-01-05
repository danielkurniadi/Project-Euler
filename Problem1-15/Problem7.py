def nth_prime(n):
    count = 2
    i = 3
    while i: #brute force through
        k = 1
        while k*k < i: #check prime
            k+= 2
            if i%k==0: #number with divisor is not a prime
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