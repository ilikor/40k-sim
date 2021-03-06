'''
Created on Dec 4, 2017

@author: Samuel
'''


import copy
import numpy
import DiceSim2.RollingFunctions as RF

class Exploding():



    def __init__(self, params):

        
        self.target_number = int(params[0].strip("+"))
        self.add_attacks = int(params[1])
        self.priorite = 1
        
        
    def rule(self, resultats, attack_type):
        
        
        target = self.target_number - attack_type.Hit_Mod
        
        exploding = copy.copy(resultats[(target-1):]) 
        sum_explode = int(numpy.sum(exploding)) * self.add_attacks
        
        explode_result = RF.rollingd6s(sum_explode, attack_type.RHT)
        
        resultats += explode_result
        
        #print("This is implemented - Exploding")
        #print("BETA TEST")
        
        return None