

import copy

import numpy

class Rending():
    


    def __init__(self, params):

        self.target_number = int(params[0].strip("+"))
        self.new_AP = int(params[1])
        self.priorite = 3
        
    
    def rule(self, resultats, attack_type):
        """
        Cette regle special ajoute un nouveau type d'attaque, donc elle a un retour non nul.
        Elle modifie directement les resultats qui lui sont passer
        """
        target = self.target_number - attack_type.Hit_Mod
        rending = copy.copy(resultats[(target-1):])
        resultats[(target-1):] = 0
        sum_rending = int(numpy.sum(rending))
        temp = copy.copy(attack_type)
        temp.R = sum_rending
        temp.AP = self.new_AP
        
        return temp