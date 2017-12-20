import copy
import numpy

class Sniper():



    def __init__(self, params):
        
        self.target_number = int(params[0].strip("+"))
        self.add_dmg = params[1]
        self.priorite = 3
        
    
    
    def rule(self, resultats, attack_type):
        """
        Cette regle special ajoute un nouveau type d'attaque, donc elle a un retour non nul.
        """
        
        
        target = self.target_number - attack_type.Hit_Mod
        snipe = copy.copy(resultats[(target-1):])
        
        sum_snipe = int(numpy.sum(snipe))
        temp = copy.copy(attack_type)
        temp.R = sum_snipe
        temp.D = self.add_dmg
        temp.AP = "MW"
        
        return temp
        