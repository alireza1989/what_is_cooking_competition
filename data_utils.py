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
