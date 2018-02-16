import numpy as np

def createMatrix(matrixNumber):
    #The matrix will be always 2 x Y
    #Where the Y will be the size of the matrix
    matrix = np.zeros((2,4), dtype=object)
    if(matrixNumber == 1):
        matrix = np.zeros((2,4), dtype=object)
        matrix[0][0] = np.array([4])
        matrix[0][1] = np.array([1, 1])
        matrix[0][2] = np.array([1, 1])
        matrix[0][3] = np.array([4])
        matrix[1][0] = np.array([4])
        matrix[1][1] = np.array([1, 1])
        matrix[1][2] = np.array([1, 1])
        matrix[1][3] = np.array([4])

    elif(matrixNumber == 2):
        matrix = np.zeros((2,10), dtype=object)
        #LINE
        matrix[0][0] = np.array([10])
        matrix[0][1] = np.array([1,1])
        matrix[0][2] = np.array([1, 1, 1])
        matrix[0][3] = np.array([1, 3, 1])
        matrix[0][4] = np.array([1, 1])
        matrix[0][5] = np.array([1,3,1])
        matrix[0][6] = np.array([1,1])
        matrix[0][7] = np.array([1,3,1])
        matrix[0][8] = np.array([1,1])
        matrix[0][9] = np.array([10])
        #COLUM
        matrix[1][0] = np.array([10])
        matrix[1][1] = np.array([1, 1])
        matrix[1][2] = np.array([1, 1, 1, 1, 1])
        matrix[1][3] = np.array([1, 1, 1, 1, 1])
        matrix[1][4] = np.array([1, 1, 1, 1, 1])
        matrix[1][5] = np.array([1,1])
        matrix[1][6] = np.array([1,1])
        matrix[1][7] = np.array([1,1,1])
        matrix[1][8] = np.array([1,1])
        matrix[1][9] = np.array([10])


    """elif(matrixNumber == 3):

    elif(matrixNumber == 4):

    elif(matrixNumber == 5):

    elif(matrixNumber == 6):"""


    return matrix
