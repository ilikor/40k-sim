
import os
from os import path
import SpecialRules
from SpecialRules import Autohit
from SpecialRules import AmbushOfBlade
from SpecialRules import Exploding
from SpecialRules import Tesla

from SpecialRules import Rending
from SpecialRules import Sniper

class SpecialRule(object):
    """
    Classe de base avec une fonction rule qui ne fait rien. Principalement pour faire du polymorphisme � partir des classes enfants de celle-ci
    """


    def __init__(self, params):
        """
        Constructor
        """
        
        
    @staticmethod
    def find_hit_rule_from_name(name):
        #Name is a string which needs to be translated to a new object
        
        rule_dict = {
                     "Exploding" : Exploding.Exploding,
                     "Tesla" : Tesla.Tesla,
                     "Ambush of Blades" : AmbushOfBlade.AmbushOfBlade,
                     "Autohit" : Autohit.Autohit
                     }
        #print(name)
        
        return rule_dict.get(name)
        
    @staticmethod
    def find_wnd_rule_from_name(name):
        
        rule_dict = {
                     "Rending" : Rending.Rending,
                     "Sniper" : Sniper.Sniper,
                     "Haywire" : "lol",
                     "MoreDamage" : "lol",
                     "MurderSword" : "lol",
                     }
        
        return rule_dict.get(name)
        
    @staticmethod
    def build_hit_rule_list():
        
        basepath = path.dirname(__file__)
        hitRulesNames = []
        nomFichier = "HitRulesList.txt"
        os.chdir(basepath)
        file = open( nomFichier, newline='' )
        for row in file:
            hitRulesNames.append(row)
            
        return hitRulesNames 
    
    @staticmethod
    def build_wnd_rule_list():
        basepath = path.dirname(__file__)
        wndRulesNames = []
        nomFichier = "WndRulesList.txt"
        os.chdir(basepath)
        file = open(nomFichier, newline='')
        for row in file:
            wndRulesNames.append(row)
        
        return wndRulesNames
        
    def rule(self, resultats, attacker):
        
        raise Exception("This is not implemented REEEEEE")