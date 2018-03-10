#! /usr/bin/env python
# -*- coding:Utf-8 -*-

"""
Ce module applique la règle spécial ambush of blade de wh40k
Elle représente une règle spéciale de la forme
si dé pour toucher est x+, l'attaque améliore l'ap de Y

la function importante est special_rule

"""

from copy import copy
from copy import deepcopy
import numpy
import DiceSim2.RollingFunctions as RF
from SpecialRules import SpecialRuleHelper as SR
from SpecialRules.SpecialRule import SpecialRule


class AmbushOfBlade(SpecialRule):
    """
    La classe AmbushOfBlade encapsule la condition d'application et l'effet
    Elle l'applique à l'aide de special_rule(...)
    """
    def __init__(self, params):
        """
        params: [target_number as string, modification AP as string, name]
        """
        self.name = params[2]
        self.target_number = int(params[0].strip("+"))
        self.add_attacks = int(params[1])
        self.priorite = 3
    
    def special_rule(self, results, attack):
        """
        Result: list of dice from rolling
        Attack: Who is currently shooting
        
        We create a need shooter without the ambush of blade special hit rule
        with better AP
        We also modify both the incoming dice results to remove the modified dices
        and create a new results list with the modified dices 
        """
        rtarget_number = self.target_number - attack.hit_mod
        ambush_results = numpy.zeros(6)
        ambush_results[rtarget_number - 1:] = results[(rtarget_number - 1):]
        results[rtarget_number - 1:] = 0
        
        temp = deepcopy(attack)
        temp.AP = temp.AP - self.add_attacks
        
        list_rules = SR.remove_rule_from_list(self.name, temp.hit_rules)
        #temp.hit_rules = list_rules
        return ambush_results, temp
    
    def rule(self, resultats, attack_type):
        """
        Cette regle special ajoute un nouveau type d'attaque
        donc elle a un retour non nul.
        Elle modifie directement les resultats qui lui sont passer
        """
        target = self.target_number - attack_type.Hit_Mod
        
        ambush = copy(resultats[(target - 1):])
        resultats[(target - 1):] = 0
        
        sum_ambush = int(numpy.sum(ambush))
        
        temp = copy(attack_type)
        temp.R = sum_ambush
        temp.AP = temp.AP - 1
        
        return temp  # ambush