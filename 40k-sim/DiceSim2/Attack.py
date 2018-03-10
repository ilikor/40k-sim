#! /usr/bin/env python
# -*- coding:Utf-8 -*-


from SpecialRules import SpecialRuleHelper as SR


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

        self.set_Mods(0, 0)
        self.hit_rules = []
        self.wnd_rules = []
        
        self.points = 13
        self.models = 10
        
        self.hit_rate = Hi
        self.s = Si
        self.ap = APi
        
        self.hit_reroll = None
        self.wnd_reroll = None
        
    @property
    def hit_rate(self):
        return self._hit_rate
    @hit_rate.setter
    def hit_rate(self, hit_rate_init):
        if(hit_rate_init == "AUTO"):
            self._hit_rate = hit_rate_init
        elif(type(hit_rate_init) is not int):
            raise TypeError("La valeur pour toucher doit être un entier")
        elif(hit_rate_init < 2):
            raise ValueError("La valeur pour toucher ne peut pas être inférieur à 2")
        self._hit_rate = hit_rate_init
    @property
    def s(self):
        return self._s
    @s.setter
    def s(self, s_init):
        if(type(s_init) is not int):
            raise TypeError("La force doit être un entier")
        if(s_init < 1):
            raise ValueError("La force ne peut pas être inférieur à 1")
        self._s = s_init
    @property
    def ap(self):
        return self._ap
    @ap.setter
    def ap(self, ap_init):
        if(ap_init == "MW"):
            self._ap = ap_init
        elif(type(ap_init) is not int):
            raise TypeError("L'AP doit être un entier")
        elif(ap_init > 0):
            raise ValueError("L'AP ne peut pas être positif")
        self._ap = ap_init
    
    @property
    def hit_reroll(self):
        return self._hit_reroll
    @hit_reroll.setter
    def hit_reroll(self, hit_reroll_init):
        if(hit_reroll_init is None):
            self._hit_reroll = hit_reroll_init
        elif(type(hit_reroll_init) is not int):
            raise TypeError("La valeur de maximale des rerolls doit être entière")
        elif(hit_reroll_init < 1):
            raise ValueError("La valeur des dés maximales à reroll ne peut pas être inférieur à 1")
        self._hit_reroll = hit_reroll_init

    def set_reroll(self, RHTi=0, RWTi=0):
        self.hit_reroll = RHTi
        self.wnd_reroll = RWTi

        self.RHT = RHTi
        self.RWT = RWTi
        
    def set_mods(self, hit_m_init=0, wnd_m_init=0, sv_m_init=0):
        
        self.hit_mod = hit_m_init
        self.wnd_mod = wnd_m_init
        self.sv_mod = sv_m_init

    def set_Mods(self, HMi=0, WMi=0, SVi=0):

        self.Hit_Mod = HMi
        self.hit_mod = HMi
        self.Wound_Mod = WMi
        self.wnd_mod = WMi
        self.Save_Mod = SVi
        self.sv_mod = SVi

    def add_hit_rules(self, list_rules):

        for element in list_rules:
            self.add_hit_rule(element)

    def add_hit_rule(self, params):

        target, effect, name = params
        ruleclass = SR.find_hit_rule_from_name(name)
        rule = ruleclass(params)
        self.hit_rules.append(rule)

    def add_wnd_rules(self, list_rules):
        print(list_rules)
        for element in list_rules:
            self.add_wnd_rule(element)

    def add_wnd_rule(self, params):

        target, effect, name = params
        ruleclass = SR.find_wnd_rule_from_name(name)
        rule = ruleclass(params)
        self.wnd_rules.append(rule)

    def marine(self):
        self.R = 10
        self.H = 3
        self.S = 4
        self.AP = 0
        self.D = 1

        self.set_reroll()
        self.set_Mods(0, 0)
    
    def __repr__(self):
        sr = ""
        sr += "Number of Dices : " + str(self.R) + "\n"
        sr += "hit rate : " + str(self.hit_rate) + "\n"
        sr += "S : " + str(self.S) + "\n"
        sr += "AP : " + str(self.AP) + "\n"
        return sr
