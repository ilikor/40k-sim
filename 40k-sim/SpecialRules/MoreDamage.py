#! /usr/bin/env python
# -*- coding:Utf-8 -*-

# TODO: Module Docstring

import copy
import numpy


class MoreDamage():
    # TODO: Class Docstring
    def __init__(self, params):
        
        self.target_number = int(params[0].strip("+"))
        self.add_dmg = params[1]
        self.priorite = 3
        
    
    def special_rule(self, results, attack):
        
        # TODO: Implement Me and make this a child of special rule
        pass
    
    def rule(self, resultats, attack_type):
        """
        Cette regle special ajoute un nouveau type d'attaque, donc elle a un retour non nul.
        """
        
        
        target = self.target_number - attack_type.Hit_Mod
        rending = copy.copy(resultats[(target-1):])
        resultats[(target-1):] = 0
        sum_rending = int(numpy.sum(rending))
        temp = copy.copy(attack_type)
        temp.R = sum_rending
        temp.AP = self.new_AP
        
        return temp