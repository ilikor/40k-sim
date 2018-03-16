#! /usr/bin/env python
# -*- coding:Utf-8 -*-

from DiceSim2.RollingFunctions import rollingd6s
import numpy

class Defense(object):
    '''
    classdocs
    '''

    def __init__(self, Ti, Wi, SVi, ISVi=None, FnPi=[], morale_init=7, Points_Init=13):
        
        # Old Attribute without property, also CAPS instead of lowercase
        self.T = Ti
        self.W = Wi
        self.SV = SVi
        self.ISV = ISVi
        self.FnP = FnPi
        self.f_n_p = FnPi
        self.Points = Points_Init
        self.moral = morale_init
        self.moral_rule = "None"
        self.unit_size = 10
        
        # New Attributes for property, also lowercase for pep8
        
        self._t = Ti
        self._w = Wi
        self._rem_w = self.w
        self._sv = SVi
        self._isv = ISVi
        self._points = Points_Init

        
    @property
    def t(self):
        return self._t
    
    @t.setter
    def t(self, t_value):
        if(type(t_value) is not int):
            raise TypeError("La toughness doit être un nombre entier")
        if(t_value < 1):
            raise ValueError("La toughness doit être supérieur à 1")
        self._t = t_value
    
    @property
    def w(self):
        return self._w
    
    @w.setter
    def w(self, w_value):
        if(type(w_value) is not int):
            raise TypeError("Le nombre de wound doit être un nombre entier")
        if(w_value < 0):
            raise ValueError("Le nombre de wound doit être un positif")
        self._w = w_value
            
    @property
    def sv(self):
        return self._sv
    
    @sv.setter
    def sv(self, sv_value):
        if(type(sv_value) is not int):
            raise TypeError("Une save doit �tre un nombre entier")
        if(sv_value < 2):
            raise ValueError("Une sauvegarde ne peut pas �tre inf�rieur � 2")
        self._sv = sv_value
            
    @property
    def isv(self):
        return self._isv
    
    @isv.setter
    def isv(self, isv_value):
        if(isv_value is None):
            self._isv = isv_value
        elif(type(isv_value) is not int):
            raise TypeError("Une isave doit �tre un nombre entier")
        elif(isv_value < 2):
            raise ValueError("Une isave ne peut pas �tre inf�rieur � 2")
        else:
            self._isv = isv_value
        
    @property
    def points(self):
        return self._points
    
    @points.setter
    def points(self, points_value):
        if type(points_value) is not int:
            raise TypeError("La valeur en point d'une figurine doit �tre enti�re")
        if points_value < 1:
            raise ValueError("La valeur en point d'une figurine doit �tre sup�rieur � 1")
        self._points = points_value

    @property
    def rem_w(self):
        return self._rem_w

    @rem_w.setter
    def rem_w(self, w_left):
        self._rem_w = w_left

    def feel_no_pain(self, dmg):
        for fnp in self.f_n_p:
            fnp_result = rollingd6s(dmg)
            fnp_result[:fnp - 1] = 0
            dmg -= numpy.sum(fnp_result)
        return dmg

    def deal_wounds(self, ap, dmg):
        dead = 0

        if ap == "MW":
            dead += dmg//self.w
            if self._rem_w <= dmg % self.w:
                dead += 1
                dmg -= self._rem_w
                self._rem_w = self.w
            self._rem_w -= dmg % self.w
        else:
            if dmg > self._rem_w:
                dead += 1
                self._rem_w = self.w
            else:
                self._rem_w -= dmg
