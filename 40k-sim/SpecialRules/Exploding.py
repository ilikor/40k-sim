#! /usr/bin/env python
# -*- coding:Utf-8 -*-


from copy import copy
import numpy

import DiceSim2.RollingFunctions as RF
from SpecialRules.SpecialRule import SpecialRule


class Exploding(SpecialRule):

    def __init__(self, params):
        self.name = params[2]
        self.target_number = int(params[0].strip("+"))
        self.add_attacks = int(params[1])
        self.priorite = 1
    

    def special_rule(self, resultats, attack):
        
        target = self.target_number - attack.hit_mod
        exploding = copy(resultats[target - 1:])
        sum_explode = int(numpy.sum(exploding)) * self.add_attacks
        explode_result = RF.rollingd6s(sum_explode, attack.hit_reroll)
        resultats += explode_result
        
        return numpy.array([]), None
        
    def rule(self, resultats, attack_type):
        target = self.target_number - attack_type.Hit_Mod
        exploding = copy(resultats[(target - 1):])
        sum_explode = int(numpy.sum(exploding)) * self.add_attacks
        explode_result = RF.rollingd6s(sum_explode, attack_type.RHT)
        resultats += explode_result
        
        #print("This is implemented - Exploding")
        #print("BETA TEST")
        return None