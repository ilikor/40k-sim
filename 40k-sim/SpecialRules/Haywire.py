#! /usr/bin/env python
# -*- coding:Utf-8 -*-

# TODO: Module Docstring

from copy import copy, deepcopy
import numpy

from SpecialRules.SpecialRule import SpecialRule
from DiceSim2 import Attack as Att


class Haywire(SpecialRule):
    """
    La classe Haywire encapsule la condition d'application et l'effet
    Elle l'applique à l'aide de special_rule(...)
    """
    def __init__(self, params):
        """
        params[0] = targets_numbers sous la forme "tn1+,tn2+"
        params[1] = dmg "dmg1, dmg2"
        params[2] = nom
        """
        temp = params[0].split(",")
        nom = params[2]
        self.target_number =  [int(temp[0].strip("+")), int(temp[1].strip("+"))]
        temp = params[1].split(",")
        self.add_dmg = [temp[0], temp[1]]
        self.priorite = 3
        
    def special_rule(self, results, attack):
        
        # sup pour le meilleur haywire
        # inf pour le moins bon haywire
        target_sup = self.target_number[1] - attack.wnd_mod
        target_inf = self.target_number[0] - attack.wnd_mod
        
        sum_super_hay = numpy.sum(results[(target_sup - 1):])
        sum_normal_hay = numpy.sum(results[(target_inf - 1):(target_sup - 1)])
        sum_dmg_haywire = 0
        
        # la somme des dmg des haywire low
        num, dX = self.dmg_helper(self.add_dmg[0])
        roll = numpy.random.randint(1, dX + 1, num * sum_normal_hay)
        sort, count = numpy.unique(roll, return_counts=True)
        sum_dmg_haywire += numpy.dot(sort, count)
        
        # la somme des dmg haywire max
        num, dX = self.dmg_helper(self.add_dmg[1])
        roll = numpy.random.randint(1, dX + 1, num * sum_super_hay)
        sort, count = numpy.unique(roll, return_counts=True)
        sum_dmg_haywire += numpy.dot(sort, count)
        
        temp = Att.Attack()
        temp.ap = "MW"
        return numpy.array([sum_dmg_haywire]), temp
    
    
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
        
        #print(resultats)
        targetSup = self.target_number[1] - attack_type.Hit_Mod
        targetHay = self.target_number[0] - attack_type.Hit_Mod
        #snipe = copy.copy(resultats[(target-1):])
        
        superHaywire = copy(resultats[(targetSup-1):])
        #print(superHaywire)
        sum_supHay = int(numpy.sum(superHaywire))
        temp1 = copy.copy(attack_type)
        temp1.R = sum_supHay
        temp1.D = self.add_dmg[1]
        temp1.AP = "MW"
        
        
        Haywire = copy(resultats[(targetHay-1):(targetSup-1)])
        sum_Hay = int(numpy.sum(Haywire))
        temp2 = copy.copy(attack_type)
        temp2.R = sum_Hay
        temp2.D = self.add_dmg[0]
        temp2.AP = "MW"
        #sum_snipe = int(numpy.sum(snipe))
        temp = copy.copy(attack_type)
        #temp.R = sum_snipe
        #temp.D = self.add_dmg
        #temp.AP = "MW"
        
        return [temp1, temp2]