'''
Created on Dec 4, 2017

@author: Samuel
'''
import SpecialRules.SpecialRules as SpecialRules
import copy
import numpy
import DiceSim2.RollingFunctions as RF

class Exploding(SpecialRules):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        
        self.target_number = params[0]
        self.add_attacks = params[1]
        
        
    def rule(self, resultats, attack_type):
        
        
        target = self.target_number - attack_type.Hit_Mod
        
        exploding = copy(resultats[(target-1):]) 
        sum_explode = int(numpy.sum(exploding)) * self.add_attacks
        
        explode_result = RF.rollingd6s(sum_explode, attack_type.RHT)
        
        resultats += explode_result
        
        print("This is implemented - Exploding")
        
        