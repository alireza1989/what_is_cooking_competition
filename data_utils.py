import pandas as pd
import numpy as np



def readJson(path):
    '''
    Function reads a JSON file and creates a Pandas data frame.

    Arguments: 
    path -- path to the JSON file on disk

    Returns:
    df -- A pandas datafame containing the JSON data
    '''
    # read json file  
    jsonFile = open(path, 'r').read()
    # create a panda data frame
    df = pd.read_json(jsonFile, orient='columns')

    return df


def dataDistributionMap(column):
    '''
    Fucntion cretaes a map of data distribution in a column of Pandas data frame

    Arguments:
    column -- A pandas series representing a column

    Returns:
    map -- a python ditionary of data and number of repetition of that data {'data' : x}
    '''

    # initializing the map
    map = {}

    print(type(column[0]))
    if type(column[0]) == list:
        for i in range (0, len(column)):
            for j in range (0, len(column[i])):
        
                item = column[i][j]

                if item in map:
                    map[item] += 1
                else: 
                    map[item] = 1
    else:
        for i in range (0, len(column)):
            
            item = column[i]

            if item in map:
                map[item] += 1
            else:
                map[item] = 1
    return map


def wordsToMap(wordsList):
    '''
    Function cretaes two maps of a list of words -  word to index and index to words

    Arguments:
    wordsList -- A python list of words

    Returns:
    w2i -- A python map of words to index
    i2w -- A python map of index to corresponding word
    '''

    w2i = {val : index for index, val in enumerate(wordsList)}
    i2w = {index : val for index, val in enumerate(wordsList)}
    return w2i, i2w


def convertToInputMatrix(recipes, wordToIndex):
    '''
    Function creates a large input matrix that has the recipes encoded -- each row is a recipe

    Arguments:
    recipes -- A list of all recipes
    wordToIndex -- A python map that contains the index of each ingredients

    Returns:
    encodedRecipes -- A big numpy matrix that has all the rcipes encoded with zero padding
    '''
    # find the size of longest recipe in the list
    longestRecipe = max(len(recipe) for recipe in recipes)


    # make a matrix of zeros
    encodedRecipes = np.zeros((recipes.shape[0], longestRecipe), dtype=int)
    
    for i in range(0, len(recipes)):
        for j in range(0, len(recipes[i])):
            encodedRecipes[i][j] = wordToIndex[recipes[i][j]]

    return encodedRecipes


def convertToOutputMatrix(cuisines, cuisineToIndex):
    '''
    Fucntion creates a matrix of expected out put lables (cuisine types)

    Arguments:
    cuisines -- An ordered list of cuisines in the training set

    cuisineToIndex -- A map of cuisine to an index

    Returns:
    cuisine1H -- A one hot embedding of cuisines type associates with each recipe
    '''

    # create the output matrix with zeros
    cuisine1H = np.zeros((len(cuisines), len(cuisineToIndex)), dtype=int)

    
    for i in range(0, len(cuisines)):
        cuisine1H[i][cuisineToIndex[cuisines[i]]] =  1

    return cuisine1H