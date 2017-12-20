'''
Created on Nov 30, 2017

@author: Samuel
'''

import copy
import SpecialRules

class Attack(object):
    '''
    classdocs
    '''


    def __init__(self, Ri=20, Hi=3, Si=4, APi=0, DMGi=1):
        '''
        Constructor
        '''
        
        
        self.R = Ri
        self.H = Hi
        self.S = Si
        self.AP = APi
        self.D = DMGi
        
        self.set_reroll()
        self.set_Mods(0,0)
        self.hit_rules = []
        self.wnd_rules = []
    
    def set_reroll(self, RHTi=0, RWTi = 0):
        
        self.RHT = RHTi
        self.RWT = RWTi
        
    def set_Mods(self, HMi=0, WMi=0, SVi=0):
        
        self.Hit_Mod = HMi
        self.Wound_Mod = WMi
        self.Save_Mod = SVi
    
    def add_hit_rules(self, list):
        
        for element in list:
            
            self.add_hit_rule(element)
    
    def add_hit_rule(self, params):
        
        target, effect, name = params
        
        ruleclass = SpecialRules.SpecialRule.SpecialRule.find_hit_rule_from_name(name)
        
        rule = ruleclass(params)
        self.hit_rules.append(rule)
    
    def add_wnd_rules(self, list):
        
        print(list)
        for element in list:
            
            self.add_wnd_rule(element)
    
    def add_wnd_rule(self, params):
        
        target, effect, name = params
        
        ruleclass = SpecialRules.SpecialRule.SpecialRule.find_wnd_rule_from_name(name)
        
        rule = ruleclass(params)
        self.wnd_rules.append(rule)
    
    def set_Points(self, points_init):
        
        self.points = points_init
    
    def set_Models(self, models_init):
        
        self.models = models_init
        
    def set_Attacks(self, attack_init):
        
        self.attacks = attack_init
    
    def marine(self):
        
        self.R = 10
        self.H = 3
        self.S = 4
        self.AP = 0
        self.D = 1
        
        self.set_reroll()
        self.set_Mods(0,0)


    
    
    