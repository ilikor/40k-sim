
#! /usr/bin/env python
# -*- coding:Utf-8 -*-

import csv

import tkinter as tk
from DiceSim2 import Attack
from SpecialRules import Special_Rules
class AttackRulesInput():
    
    
   
    
    
    def __init__(self, root, columnInput):
        '''
        Constructor
        '''
        
        self.none_text = "NONE"
        self.one_text = "ONES"
        self.miss_text = "MISS"
        
        self.reroll_list = [self.none_text, self.one_text, self.miss_text]
        
        self.root = root
        self.currentColumn = columnInput
        self.rule_Entry()

            
    def populate_Rules_Listbox(self):
        
        ##noms des règles sur les jets pour toucher
        hit_rules_names_list = Special_Rules.Special_Rules.build_hit_rule_list()
        self.Entry_Hit_Rules.config(height = len(hit_rules_names_list))
        for item in hit_rules_names_list:
            self.Entry_Hit_Rules.insert(tk.END, item)
        
        ##noms des règle sur les jets pour blesser
        wnd_rules_names_list = Special_Rules.Special_Rules.build_wnd_rule_list()
        self.Entry_Wnd_Rules.config(height = len(wnd_rules_names_list))
        for item in wnd_rules_names_list:
            self.Entry_Wnd_Rules.insert(tk.END, item)
        
        ##Noms des autre règles 
            
    
    def rule_Entry(self):
        
        width_text = 10
        
        self.Entry_Hit_Reroll = tk.Listbox(self.root, exportselection=False)
        self.Entry_Hit_Reroll.config(height = 3, width=width_text)
        for item in self.reroll_list:
            self.Entry_Hit_Reroll.insert(tk.END, item)
        
        #self.Entry_Hit_Reroll.insert(tk.END, self.none_text)
        #self.Entry_Hit_Reroll.insert(tk.END, self.one_text)
        #self.Entry_Hit_Reroll.insert(tk.END, self.miss_text)
        self.Entry_Hit_Reroll.grid(row = 0, column = self.currentColumn,sticky=tk.W )
        
        self.Entry_Wnd_Reroll = tk.Listbox(self.root, exportselection=False)
        self.Entry_Wnd_Reroll.config(height = 3, width=width_text)
        for item in self.reroll_list:
            self.Entry_Wnd_Reroll.insert(tk.END, item)
        #self.Entry_Wnd_Reroll.insert(tk.END, self.none_text)
        #self.Entry_Wnd_Reroll.insert(tk.END, self.one_text)
        #self.Entry_Wnd_Reroll.insert(tk.END, self.miss_text)
        self.Entry_Wnd_Reroll.grid(row = 1, column = self.currentColumn,sticky=tk.W)
        
        self.Hit_Rules_Frame = tk.Frame(self.root)
        self.Hit_Rules_Frame.grid(row = 2, column = self.currentColumn)
        self.Hit_Rules_Add = tk.Button(self.Hit_Rules_Frame, text="ADD", command = self.add_Hit_Rule())
        self.Hit_Rules_Add.grid(row = 0, column = 0)
        self.Entry_Hit_Rules = tk.Listbox(self.Hit_Rules_Frame)
        self.Entry_Hit_Rules.grid(row = 0, column = 1)
        
        
        self.Wnd_Rules_Frame = tk.Frame(self.root)
        self.Wnd_Rules_Frame.grid(row = 3, column = self.currentColumn)
        self.Wnd_Rules_Add = tk.Button(self.Wnd_Rules_Frame, text = "ADD", command = self.add_Wnd_Rule)
        self.Wnd_Rules_Add.grid(row = 0, column = 0)
        self.Entry_Wnd_Rules = tk.Listbox(self.Wnd_Rules_Frame)
        self.Entry_Wnd_Rules.grid(row = 0, column = 1)
        
        self.populate_Rules_Listbox()
        
    
    def add_Hit_Rule(self):
        
        pass    
    
    def add_Wnd_Rule(self):
        
        pass
        
        
    def gather_input(self):
        """
        Gathers the rule for the rerolls and return them in string format, the parent will parse and add the right rules to the attack
        hit_reroll, wnd_reroll, hit_rules[], wnd_rules[]
        """
        
        #Gathering hit reroll rule
        hit_reroll_index = self.Entry_Hit_Reroll.curselection()
        hit_reroll_rule = ""
        
        if(hit_reroll_index):
            
            hit_reroll_rule = self.Entry_Hit_Reroll.get(hit_reroll_index)
        else:
            hit_reroll_rule = self.none_text
        
        #Gathering wnd reroll rule
        wnd_reroll_index = self.Entry_Wnd_Reroll.curselection()
        wnd_reroll_rule = ""
        if(wnd_reroll_index):
            
            wnd_reroll_rule = self.Entry_Wnd_Reroll.get(wnd_reroll_index)
        else:
            wnd_reroll_rule = self.none_text
        
        
        
        