#! /usr/bin/env python
# -*- coding:Utf-8 -*-


import tkinter as tk
from functools import partial

from DiceSim2UI import Input_AttackUI

class AttackRuleUI(tk.Frame):
    '''
    This class is meant to hold the text and the labels of the associated Entry mechanism in AttackRuleEntryUI
    
    '''


    def __init__(self, root):
        '''
        Constructor
        '''
            
        tk.Frame.__init__(self, root)    
        self.ruleUI()
        
    def ruleUI(self):
        
        width_text = 10
        
        self.Text_Hit_Reroll = tk.StringVar()
        self.Text_Hit_Reroll.set("Hit reroll")
        self.Label_Hit_Reroll = tk.Label(self, textvariable=self.Text_Hit_Reroll,  width = width_text)
        self.Label_Hit_Reroll.grid(row = 0, column = 0,sticky=tk.W)
        
        self.Text_Wnd_Reroll = tk.StringVar()
        self.Text_Wnd_Reroll.set("Wnd reroll")
        self.Label_Wnd_Reroll = tk.Label(self, textvariable=self.Text_Wnd_Reroll,  width = width_text)
        self.Label_Wnd_Reroll.grid(row = 1, column = 0,sticky=tk.W)
        
        self.Text_Hit_Rules = tk.StringVar()
        self.Text_Hit_Rules.set("Hit rules")
        self.Label_Hit_Rules = tk.Label(self, textvariable=self.Text_Hit_Rules,  width = width_text)
        self.Label_Hit_Rules.grid(row = 2, column = 0,sticky=tk.W)
        
        self.Text_Wnd_Rules = tk.StringVar()
        self.Text_Wnd_Rules.set("Wnd rules")
        self.Label_Wnd_Rules = tk.Label(self, textvariable=self.Text_Wnd_Rules,  width = width_text)
        self.Label_Wnd_Rules.grid(row = 3, column = 0,sticky=tk.W)
        
    def addingRuleUI(self):
       
        pass 
    