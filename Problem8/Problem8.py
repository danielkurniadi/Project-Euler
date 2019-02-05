import string

def str_to_prod(ser):
    prod = 1.0
    for s in ser:
        prod *= int(s)
    return prod

def largest_prod(num_str, w):
    # prep
    m = len(num_str)
    prod = str_to_prod(num_str[:w])
    max_prod = prod
    # windowing
    i = 0
    k = w
    while k < m:
        if num_str[i]=='0':
            prod = str_to_prod(num_str[i+1:k+1])
        else:
            prod = prod*int(num_str[k])/int(num_str[i])
        
        if prod > max_prod:
            max_prod = prod
        i += 1
        k += 1
    return max_prod

def read_file_toNumb(infile):
    with open(infile, 'r') as fh:
        bad_chars = '\n\r'
        data = fh.read().replace('\n', '')
        return data

def main(filepath):
    num_str = read_file_toNumb(filepath)
    x = largest_prod(num_str, 13)
    print(x) #23514624000


if __name__ == '__main__':
    filepath = './matrix_p8.txt'
    main(filepath)
