#! /usr/bin/env python
# -*- coding:Utf-8 -*-

# TODO: Module Docstring

from copy import copy, deepcopy
import numpy
from SpecialRules.SpecialRule import SpecialRule
from DiceSim2 import Attack as Att


class Sniper(SpecialRule):
    # TODO: Class Docstring
    def __init__(self, params):
        
        self.target_number = int(params[0].strip("+"))
        self.add_dmg = params[1]
        self.priorite = 3
    
    def special_rule(self, results, attack):

        target_number = self.target_number - attack.wnd_mod
        
        sum_snipe = numpy.sum(results[(target_number - 1):])
        sum_dmg_snipe = 0
        
        # la somme des dmg haywire max
        num, dX = self.dmg_helper(self.add_dmg)
        roll = numpy.random.randint(1, dX + 1, num * sum_snipe)
        sort, count = numpy.unique(roll, return_counts=True)
        sum_dmg_snipe += numpy.dot(sort, count)
        
        temp = Att.Attack()
        temp.ap = "MW"
        return numpy.array([sum_dmg_snipe]), temp
    
    def dmg_helper(self, dmg):
        
        split = dmg.split("d")
        dX = 0
        numba = int(split[0])
        if (len(split) == 1):
            dX = 1
        else:
            dX = int(split[1])
        return numba, dX
    
    def rule(self, resultats, attack_type):
        """
        Cette regle special ajoute un nouveau type d'attaque, donc elle a un retour non nul.
        """
        
        
        target = self.target_number - attack_type.Hit_Mod
        snipe = copy(resultats[(target-1):])
        
        sum_snipe = int(numpy.sum(snipe))
        temp = copy(attack_type)
        temp.R = sum_snipe
        temp.D = self.add_dmg
        temp.AP = "MW"
        
        return temp
    
if __name__ == '__main__':
    
    tn = "6"
    dmg = "1"
    name = "Sniper"
    Rule = Sniper([tn,dmg,name])
    
        