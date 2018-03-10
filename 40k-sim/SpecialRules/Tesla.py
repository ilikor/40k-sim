#! /usr/bin/env python
# -*- coding:Utf-8 -*-

# TODO: Module Docstring

from copy import copy
from copy import deepcopy
import numpy
import DiceSim2.RollingFunctions as RF
from SpecialRules.SpecialRule import SpecialRule


class Tesla(SpecialRule):
    # TODO: Class Docstring
    def __init__(self, params):
        
        print(params[0])
        
        self.target_number = int(params[0].strip("+"))
        self.add_attacks = int(params[1])
        self.priorite = 2 #La priorite sera utilise pour savoir l'ordre que les regles sont applique, placeholder
        
    def special_rule(self, results, attack):
        rtarget_number = self.target_number - attack.hit_mod
        tesla_results = numpy.zeros(6)
        tesla_results[rtarget_number - 1:] = results[(rtarget_number - 1):]
        tesla_results = tesla_results * self.add_attacks
        
        results = results + tesla_results
        
        return numpy.array([]), None
    
    def rule(self, resultats, attack_type):
        
        
        target = self.target_number - attack_type.Hit_Mod
        #print(resultats)
        tesla = copy(resultats[(target-1):]) 
        #print(tesla)
        sum_tesla = int(numpy.sum(tesla)) * self.add_attacks
        
        resultats[-1] += sum_tesla
        
        
        
        
        #print("This is implemented - Tesla")
        #print("BETA TEST")
        
        return None