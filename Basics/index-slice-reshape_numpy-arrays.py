# -*- coding: utf-8 -*-

# From lists to Arrays

# One-dimensional list to array

# Convert a one-dimensional list of data to an array by calling the array() NumPy function
# one dimensional example
from numpy import array
from numpy import reshape

def oneDimensionalListToArray():    
    """one dimensional example"""
    # list of data 
    data = [11, 22, 33, 44, 55]
    # array of data
    data = array(data)
    
    print(data)
    print(type(data))
    return

    
def twoDimensionalListToArray():
    '''two dimensional example'''
    # list of data
    data = [[11, 22],
    		[33, 44],
    		[55, 66]]
    # array of data
    data = array(data)
    print(data)
    print(type(data))
    return

def oneDimensionalIndexing():
    '''one dimensional indexing'''
    # define array
    data = array([11, 22, 33, 44, 55])
    # index data
    print(data[0])
    print(data[4])
    return

def twoDimensionalIndexing():
    '''two dimensional indexing'''
    data = array([[11, 22], [33, 44], [55, 66]])
    print(data[0,0])
    print(data[0][0])
    print(data[0,])
    return

def oneDimensionalSlicing():
    '''one dimensional slicing'''
    data = array([11, 22, 33, 44, 55])
    print(data[:])
    print(data[2:4])
    print(data[-2:])
    return

def twoDimensionalSlicing():
    '''two dimensional slicing'''
    data = array([[11, 22, 33],
        		  [44, 55, 66],
        		  [77, 88, 99]])
    x = data[:, :2] # print [[11 22] [44 55] [77 88]]
    y = data[:, 2] #prints [33 66 99]
    z = data[:, 1] #prints [22 55 88]
    w = data[:, 1:2] # prints [[22] [55] [88]]
    print(x)
    print(y)
    print(z)
    print(w)
    return

def splitInputOutput():
    '''Split input and output rows'''
    data = array([[11, 22, 33],
    		[44, 55, 66],
    		[77, 88, 99]])
    # separate data
    inputX, outputY = data[:, :-1], data[:, -1]
    print(inputX)
    print(outputY)     
    return

def splitTrainTest():
    '''Split data into training and test data'''
    data = array([[11, 22, 33],
                  [44, 55, 66],
                  [77, 88, 99]])
    # seperate data
    split = 2
    train, test = data[:split, :], data[split:, :]
    print(train) #prints [[11 22 33] [44 55 66]]
    print(test) #print [[77 88 99]]
    return

def arrayShape():
    
    data1 = array([11, 22, 33, 44, 55])
    print(data1.shape) # prints tuple: (5,)
    # list of data
    data2 = [[11, 22],
            [33, 44],
            [55, 66]]
    # array of data
    data2 = array(data2)
    print('Rows: %d' % data2.shape[0]) #prints Rows: 3
    print('Columns: %d' % data2.shape[1]) #prints Columns: 2
    return


def arrayReshaping1Dto2D():
    '''Reshape 1D to 2D array'''    
    #define array
    data = array([11, 22, 33, 44, 55])
    print(data.shape) #prints (5,)
    #reshape
    data = data.reshape((data.shape[0], 1))
    print(data.shape)    
    print(data)
    return

def arrayReshaping2Dto3D():
    '''Reshape 2D to 3D array'''    
    data = [[11, 22],
            [33, 44],
            [55, 66]]
    #array of data
    data = array(data)
    print(data.shape)
    print(data)
    print('--------')
    #reshape
    data = data.reshape((data.shape[0], data.shape[1], 1))
    print(data.shape)
    print(data)
    return

def arrayReshaping1Dto3D():
    data = array([11, 22, 33, 44, 55, 66])
    data = array(data)
    print(data.shape)
    print(data)
    print('---------')    
    data = reshape(data, (2, 3))    
    print(data.shape) # prints (2, 3)
    print(data) #prints [[11 22 33] [44 55 66]]
    print('---------')    
    data = reshape(data, (3, 2))    
    print(data.shape)# prints (3, 2)
    print(data) #print [[11 22] [33 44] [55 66]]
    print('---------')
    return
#print("one dimensional example")
#oneDimensionalListToArray()
#print("two dimensional example")
#twoDimensionalListToArray()
#oneDimensionalIndexing()
#twoDimensionalIndexing()
#oneDimensionalSlicing()
#twoDimensionalSlicing()
#splitInputOutput()
#splitTrainTest()
#arrayShape()
#array1Dto2DReshaping()
#arrayReshaping2Dto3D()
arrayReshaping1Dto3D()