

import copy
import numpy
import DiceSim2.RollingFunctions as RF

class Tesla():



    def __init__(self, params):
        
        print(params[0])
        
        self.target_number = int(params[0].strip("+"))
        self.add_attacks = int(params[1])
        self.priorite = 2 #La priorite sera utilise pour savoir l'ordre que les regles sont applique, placeholder
        
    def rule(self, resultats, attack_type):
        
        
        target = self.target_number - attack_type.Hit_Mod
        #print(resultats)
        tesla = copy.copy(resultats[(target-1):]) 
        #print(tesla)
        sum_tesla = int(numpy.sum(tesla)) * self.add_attacks
        
        resultats[-1] += sum_tesla
        
        
        
        
        #print("This is implemented - Tesla")
        #print("BETA TEST")
        
        return None