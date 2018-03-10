'''
Created on Dec 4, 2017

@author: Samuel
'''

import numpy


def rollingd6s(number, reroll=None):
    """

    :param number: nombre de dé à rouler
    :param reroll: Value under which you reroll
    :param fast: True or False -> Uses fast rolling or not (Should be true)
    :return: [#1, #2, #3, #4, #5, #6]
    """

    base = [0, 1, 2, 3, 4, 5]
    base_counts = [1, 1, 1, 1, 1, 1]
    roll = numpy.append(numpy.random.randint(0, 6, number), base)
    counts = numpy.bincount(roll)
    counts -= base_counts
    if reroll is not None:

        reroll_counts = reroll_d6s(counts, reroll)
        counts[:reroll] = 0
        counts += reroll_counts

    results = counts
    return results


def reroll_d6s(values, reroll):

    if reroll < 1:
        raise ValueError("Valeur de reroll négative")
    reroll_count = numpy.sum(values[:reroll])
    counts = rollingd6s(reroll_count)
    return counts


def rollingd3s(number, reroll = 0):

    results = numpy.zeros(3)
    
    for i in range(number):
        
        roll = numpy.random.randint(1,4)
        results[roll-1] += 1
    
    return results

def rollingdXs(number, dX):

    """
    Result is the count of [0,1,...,dX ]
    1,2,5,5,6 give result [1,1,0,0,2,1]
    """
    results = numpy.zeros(dX)
    
    base = range(0,dX)
    _, base_count = numpy.unique(base, return_counts=True)

    roll = numpy.random.randint(1, dX + 1, (number, 1))
    roll = numpy.append(roll, base)
    _, counts = numpy.unique(roll, return_counts=True)
    #roll = numpy.random.randint(1,dX+1)
    results = counts - base_count

    return results

def rollingdXs_time_dependant(number, dX):
    """
    This is mostly used for damage rolls as the roll most be done 1 after the other because of multi-wounds models and FnP and shit like that
    """
    
    results = numpy.random.randint(1, dX + 1, (number, 1))
    
    return results

if __name__ == '__main__':
    
    pass