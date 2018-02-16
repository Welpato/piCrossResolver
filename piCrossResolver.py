#coding: utf-8
import numpy as np
import copy
import baseMatrix

def countNumber(resultMatrix, number):
    counter = 0
    if(type(resultMatrix) == int):
        if(resultMatrix == number):
            return 1
        else:
            return 0
    else:
        c = 0
        while( c < len(resultMatrix)):
            counter = counter + countNumber(resultMatrix[c], number)
            c = c + 1
    return counter

def verifyFullLine(matrix, resultMatrix):
    #line
    c = 0
    while(c < len(matrix[0])):
        if(matrix[0][c][0] == len(matrix[1])):
            y = 0
            while(y < len(matrix[0])):
                resultMatrix[y][c] = 1
                y = y + 1
        c = c + 1
    #column
    c = 0
    while(c < len(matrix[1])):
        if(matrix[0][c][0] == len(matrix[0])):
            y = 0
            while(y < len(matrix[0])):
                resultMatrix[c][y] = 1
                y = y + 1
        c = c + 1
    return resultMatrix

def verifyFullSpace(matrix, resultMatrix):
    #THIS METHOD ONLY WORKS USING THE LINES OF THE RESULT MATRIX
    line = 0
    while(line < len(resultMatrix)):
        x = 0
        while(x < len(matrix[line])):
            if(matrix[line][x] == countNumber(resultMatrix[line], 0) or matrix[line][x] == len(resultMatrix[line])):
                column = 0
                while(column < len(resultMatrix[line])):
                    if(resultMatrix[line][column] == 0 or matrix[line][x] == len(resultMatrix[line])):
                        resultMatrix[line][column] = 1
                    column = column + 1
            x = x + 1
        line = line + 1
    return resultMatrix

def scanAllDirections(matrix, resultMatrix):
    #LINE
    resultMatrix = verifyFullSpace(matrix[0], resultMatrix)
    #COLUMN
    resultMatrix = verifyFullSpace(matrix[1], resultMatrix.transpose())

    return resultMatrix.transpose()


def addBlock(resultMatrix, x, y, lenX, lenY):
    if(x >= 0 and x < lenX and y >= 0 and y < lenY):
        if(resultMatrix[x][y] == 0):
            resultMatrix[x][y] = 2
            return resultMatrix
    return resultMatrix


def blockSpaces(resultMatrix):
    x = 0
    while(x < len(resultMatrix)):
        y = 0
        while(y < len(resultMatrix[x])):
            if(resultMatrix[x][y] == 1):
                resultMatrix = addBlock(resultMatrix, x, y+1, len(resultMatrix), len(resultMatrix[x]))
                resultMatrix = addBlock(resultMatrix, x, y-1, len(resultMatrix), len(resultMatrix[x]))
                resultMatrix = addBlock(resultMatrix, x+1, y, len(resultMatrix), len(resultMatrix[x]))
                resultMatrix = addBlock(resultMatrix, x-1, y, len(resultMatrix), len(resultMatrix[x]))
            y = y + 1
        x = x + 1
    return resultMatrix

def verifyMatrix(matrix, resultMatrix):
    line = 0
    while(line < len(resultMatrix)):
        x = 0
        while(x < len(matrix[line])):
            counter = 0
            column = 0
            while(column < len(resultMatrix[line])):
                if(counter < matrix[line][x]):
                    if(resultMatrix[line][column] == 1):
                        counter = counter + 1
                        
                column = column + 1
            x = x + 1
        line = line + 1

def fillMatrix(matrix,resultMatrix):

    return resultMatrix

def resolveProcess(matrix, resultMatrix):
    resultMatrix = blockSpaces(scanAllDirections(matrix, resultMatrix))
    emptyVal = countNumber(resultMatrix, 0)
    if(emptyVal > 0):
        resultMatrix = blockSpaces(scanAllDirections(matrix, resultMatrix))
        if(emptyVal == countNumber(resultMatrix, 0)):
            resultMatrix = resultMatrix
            #Does another process of verification
        else:
            resultMatrix = resolveProcess(matrix, resultMatrix)
    return resultMatrix

def resolvePiCross(matrix):
    resultMatrix = np.zeros((len(matrix[0]), len(matrix[1])), dtype=object)
    resultMatrix = resolveProcess(matrix, resultMatrix)

    return resultMatrix

matrix = baseMatrix.createMatrix(2)
print(matrix)

print(resolvePiCross(matrix))
