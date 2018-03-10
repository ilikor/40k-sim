import os
from os import path

from SpecialRules import Autohit
from SpecialRules import AmbushOfBlade
from SpecialRules import Exploding
from SpecialRules import Tesla

from SpecialRules import Rending
from SpecialRules import Sniper
from SpecialRules import Haywire


def remove_rule_from_list(name, list_rules):
    for rule in list_rules:
        if(rule.name == name):
            list_rules.remove(rule)
    return list_rules
  

def find_hit_rule_from_name(name):
    # Name is a string which needs to be translated to a new object
    
    rule_dict = {
                "Exploding": Exploding.Exploding,
                "Tesla": Tesla.Tesla,
                "Ambush of Blades": AmbushOfBlade.AmbushOfBlade,
                "Autohit": Autohit.Autohit}
    
    return rule_dict.get(name)
    
    
def find_wnd_rule_from_name(name):
    
    rule_dict = {
                 "Rending" : Rending.Rending,
                 "Sniper" : Sniper.Sniper,
                 "Haywire" : Haywire.Haywire,
                 "MoreDamage" : "lol",
                 "MurderSword" : "lol",
                 }
    
    return rule_dict.get(name)
    
    
def build_hit_rule_list():
    
    basepath = path.dirname(__file__)
    hitRulesNames = []
    nomFichier = "HitRulesList.txt"
    os.chdir(basepath)
    file = open(nomFichier, newline='')
    for row in file:
        hitRulesNames.append(row)
        
    return hitRulesNames


def build_wnd_rule_list():
    basepath = path.dirname(__file__)
    wndRulesNames = []
    nomFichier = "WndRulesList.txt"
    os.chdir(basepath)
    file = open(nomFichier, newline='')
    for row in file:
        wndRulesNames.append(row)
    
    return wndRulesNames
