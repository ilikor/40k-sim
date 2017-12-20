

import copy

import numpy

class Autohit():
    


    def __init__(self, params):
        
        
        pass
    
    def rule(self, resultats, attack_type):
        """
        Autohit will create a new shooter for wounding which considers everything hitting :)
        """
        
    
        
        temp = copy.copy(attack_type)
        temp.R = int(numpy.sum(resultats))
        #print(temp.R)
        resultats[:] = 0 
        
        #print("This is implemented - AUTOHIT")
        #print("BETA TEST")
        
        return temp

        
       
        