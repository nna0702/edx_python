# We want to write some simple procedures that work on dictionaries to return information.
# 
# First, write a procedure, called how_many, which returns the sum of the number of values associated with a dictionary.


def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    total = 0
    for i in aDict.keys():
        total = total + len(aDict[i])
    return total


if __name__ == '__main__':
    # Defne dictionary

    animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

    animals['d'] = ['donkey']
    animals['d'].append('dog')
    animals['d'].append('dingo')

    print(how_many(animals))