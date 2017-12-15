'''
Created on Dec 4, 2017

@author: Samuel
'''

import numpy

def rollingd6s(number, reroll = 0):
    
    results = numpy.zeros(6)
    
    for i in range(number):
        
        roll = numpy.random.randint(1,7)
        
        if(reroll != None):
            if(roll <= reroll):
            
                roll = numpy.random.randint(1,7)
        
        results[roll-1] += 1
        
    return results

def rollingd3s(number, reroll = 0):

    results = numpy.zeros(3)
    
    for i in range(number):
        
        roll = numpy.random.randint(1,4)
        results[roll-1] += 1
    
    return results

def rollingdXs(number, dX):

    results = numpy.zeros(dX)
    
    for i in range(number):
        
        roll = numpy.random.randint(1,dX+1)
        results[roll-1] += 1        
    
    return results

def rollingdXs_time_dependant(number, dX):
    """
    This is mostly used for damage rolls as the roll most be done 1 after the other because of multi-wounds models and FnP and shit like that
    """
    
    results = numpy.zeros(number)
    
    for i in range(number):
        
        roll = numpy.random.randint(1, dX+1)
        results[i] = roll
    
    return results

if __name__ == '__main__':
    pass