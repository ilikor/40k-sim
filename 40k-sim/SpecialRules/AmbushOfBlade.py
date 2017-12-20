'''
Created on Dec 16, 2017

@author: Samuel
'''

import copy
import numpy
import DiceSim2.RollingFunctions as RF



class AmbushOfBlade():


    def __init__(self, params):

        
        self.target_number = int(params[0].strip("+"))
        self.add_attacks = params[1]
        self.priorite = 3
    
    
    def rule(self, resultats, attack_type):
        """
        Cette regle special ajoute un nouveau type d'attaque, donc elle a un retour non nul.
        Elle modifie directement les resultats qui lui sont passer
        """
        target = self.target_number - attack_type.Hit_Mod
        
        ambush = copy.copy(resultats[(target-1):])
        resultats[(target-1):] = 0
        
        sum_ambush = int(numpy.sum(ambush))
        
        temp = copy.copy(attack_type)
        temp.R = sum_ambush
        temp.AP = temp.AP - 1
        
        return temp