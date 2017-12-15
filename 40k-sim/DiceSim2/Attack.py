'''
Created on Nov 30, 2017

@author: Samuel
'''

import copy

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
    
    def set_reroll(self, RHTi=0, RWTi = 0):
        
        self.RHT = RHTi
        self.RWT = RWTi
        
    def set_Mods(self, HMi=0, WMi=0, SVi=0):
        
        self.Hit_Mod = HMi
        self.Wound_Mod = WMi
        self.Save_Mod = SVi
    
    def set_Rend(self, Ti, APi):
        
        self.Rend_Target = Ti
        self.Rend_Ap = APi
    
    
    def set_Exploding(self, Ei, EAi):
        
        self.Exploding_Target = Ei
        self.Exploding_Add = EAi
        
    def set_Snipe(self, Si, SDi):
        
        self.Snipe_Target = Si
        self.Snipe_Dmg = SDi
    
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


    
    
    