#! /usr/bin/env python
# -*- coding:Utf-8 -*-

"""
Ce module contient le nécessaire pour appliquer la règle spécial autohit de wh40k
la function importante est special_rule de l'objet Autohit
"""

import numpy

from SpecialRules.SpecialRule import SpecialRule


class Autohit(SpecialRule):
    """ 
    encapsule special_rule pour permettre polymorphisme 
    Elle change le hit_rate de l'attaquant
    """
 
    def __init__(self, params):
        
        self.name = params[2]
    
    def special_rule(self, results, attack):
        """
        Modifie attack pour changer son hit_rate
        """
        attack.hit_rate = "AUTO"
        
        return numpy.array([]), None