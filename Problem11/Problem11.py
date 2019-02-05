import numpy as np

def sliding_Window(Mat, f_size, func):
    maxprod = 1
    maxmat = np.zeros((f_size,f_size))
    m, n = Mat.shape #rows, cols
    mm, nn = m-f_size+1, n-f_size+1 #bounds
    for j in range(0, mm):
        for i in range(0, nn):
            mat = (Mat[j:j+f_size, i:i+f_size])
            x = func(mat) #apply callbacks function
            if x > maxprod:
                maxprod = x
                maxmat = mat
    return maxprod, maxmat

def apply2dMaxProd(mat):
    maxprod = 1
    m, n = mat.shape
    #horizontals prod
    for j in range(0, m):
        x = np.prod(mat[j,:])
        if x > maxprod:
            maxprod = x
    #vertical prod
    for i in range(0, n):
        y = np.prod(mat[:,i])
        if y > maxprod:
            maxprod = y
    #diagonal
    x = np.prod(mat.diagonal())
    if x > maxprod:
        maxprod = x
    #2nd diagonal
    x = np.prod(np.diag(np.fliplr(mat)))
    if x > maxprod:
        maxprod = x
    
    return maxprod

def read_file_toMat(infile):
    def cleanData(numstr):
        if numstr[0]=='0':
            return int(numstr[1])
        else:
            return int(numstr)

    with open(infile, 'r') as fh:
        data = [list(map(lambda numstr: cleanData(numstr),
                 line.split(' '))) for line in fh.read().split('\n')]
        return np.matrix(data, dtype='int')

def main(filepath):
    Mat = read_file_toMat(filepath)
    maxprod, mat = sliding_Window(Mat, 4, apply2dMaxProd)

    print("maxprod:", maxprod) #answer: 70600674
    print("maxmat:\n", mat)
    print("matric:\n", Mat)

if __name__ == "__main__":
    filepath = 'matrix_p11.txt'
    main(filepath)


    