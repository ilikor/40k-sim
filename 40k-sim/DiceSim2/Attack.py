#! /usr/bin/env python
# -*- coding:Utf-8 -*-


from SpecialRules import SpecialRuleHelper as SR


class Attack(object):
    """

    """

    def __init__(self, ri=20, hi=3, si=4, api=0, dmgi=1):
        """

        Parameters
        ----------
        ri
        hi
        si
        api
        dmgi
        """
        self.set_mods(0, 0)
        self.hit_rules = []
        self.wnd_rules = []
        
        self.points = 13
        self.models = 10

        self._attack = ri
        self._hit_rate = hi
        self._str = si
        self._ap = api
        self._dmg = dmgi
        self._hit_reroll = None
        self._wnd_reroll = None

        self._hit_mod = 0
        self._wnd_mod = 0
        self._sv_mod = 0

    @property
    def attack(self):
        return self._attack

    @attack.setter
    def attack(self, attack_init):
        self._attack = attack_init

    @property
    def hit_rate(self):
        return self._hit_rate

    @hit_rate.setter
    def hit_rate(self, hit_rate_init):
        if hit_rate_init == "AUTO":
            self._hit_rate = hit_rate_init
        elif type(hit_rate_init) is not int:
            raise TypeError("La valeur pour toucher doit être un entier")
        elif hit_rate_init < 2:
            raise ValueError("La valeur pour toucher ne peut pas être inférieur à 2")
        self._hit_rate = hit_rate_init

    @property
    def str(self):
        return self._str

    @str.setter
    def str(self, str_init):
        if type(str_init) is not int:
            raise TypeError("La force doit être un entier")
        if str_init < 1:
            raise ValueError("La force ne peut pas être inférieur à 1")
        self._str = str_init

    @property
    def ap(self):
        return self._ap

    @ap.setter
    def ap(self, ap_init):
        if ap_init == "MW":
            self._ap = ap_init
        elif type(ap_init) is not int:
            raise TypeError("L'AP doit être un entier")
        elif ap_init > 0:
            raise ValueError("L'AP ne peut pas être positif")
        self._ap = ap_init

    @property
    def dmg(self):
        return self._dmg

    @dmg.setter
    def dmg(self, dmg_init):
        self._dmg = dmg_init

    @property
    def hit_reroll(self):
        return self._hit_reroll

    @hit_reroll.setter
    def hit_reroll(self, hit_reroll_init):
        if hit_reroll_init is None:
            self._hit_reroll = hit_reroll_init
        elif type(hit_reroll_init) is not int:
            raise TypeError("La valeur de maximale des rerolls doit être entière")
        elif hit_reroll_init < 1:
            raise ValueError("La valeur des dés maximales à reroll ne peut pas être inférieur à 1")
        self._hit_reroll = hit_reroll_init

    @property
    def wnd_reroll(self):
        return self._hit_reroll

    @wnd_reroll.setter
    def wnd_reroll(self, wnd_reroll_init):
        if wnd_reroll_init is None:
            self._wnd_reroll = wnd_reroll_init
        elif type(wnd_reroll_init) is not int:
            raise TypeError("La valeur de maximale des rerolls doit être entière")
        elif wnd_reroll_init < 1:
            raise ValueError("La valeur des dés maximales à reroll ne peut pas être inférieur à 1")
        self._wnd_reroll = wnd_reroll_init

    @property
    def hit_mod(self):
        return self._hit_mod

    @hit_mod.setter
    def hit_mod(self, hit_mod_init):
        self._hit_mod = hit_mod_init

    @property
    def wnd_mod(self):
        return self._wnd_mod

    @wnd_mod.setter
    def wnd_mod(self, wnd_mod_init):
        self._wnd_mod = wnd_mod_init

    @property
    def sv_mod(self):
        return self._sv_mod

    @sv_mod.setter
    def sv_mod(self, sv_mod_init):
        self._sv_mod = sv_mod_init

    def set_reroll(self, rhti=0, rwti=0):
        self.hit_reroll = rhti
        self.wnd_reroll = rwti

    def set_mods(self, hmi=0, wmi=0, svi=0):

        self.hit_mod = hmi
        self.wnd_mod = wmi
        self.sv_mod = svi

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
        self.r = 10
        self.hit = 3
        self.str = 4
        self.ap = 0
        self.dmg = 1

        self.set_reroll()
        self.set_mods(0, 0, 0)
    
    def __repr__(self):
        sr = ""
        sr += "Number of Dices : " + str(self.r) + "\n"
        sr += "hit rate : " + str(self.hit_rate) + "\n"
        sr += "S : " + str(self.str) + "\n"
        sr += "AP : " + str(self.ap) + "\n"
        return sr
