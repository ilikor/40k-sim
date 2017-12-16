
import os
from os import path

class SpecialRules(object):
    """
    Classe de base avec une fonction rule qui ne fait rien. Principalement pour faire du polymorphisme � partir des classes enfants de celle-ci
    """


    def __init__(self):
        """
        Constructor
        """
        
        
        
        
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