import pandas as pd 



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