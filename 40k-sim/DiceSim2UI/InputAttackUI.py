import tkinter as tk
from DiceSim2UI import RuleFrame
from DiceSim2 import Attack
from SpecialRules import SpecialRuleHelper
from DiceSim2UI.Helper_UI import clean_hit_input


class AtkInput:

    def __init__(self, root, column_input):

        self.none_text = "NONE"
        self.one_text = "ONES"
        self.miss_text = "MISS"
        self.reroll_list = [self.none_text, self.one_text, self.miss_text]

        self.Hit_Rules = []
        self.Wnd_Rules = []

        self.Hit_Row = 0
        self.Wnd_Row = 0
        self.CI = column_input
        self.root = root

        self.width_text = 8

        self.attack_text = tk.StringVar()
        self.attack_label = tk.Label(self.root, textvariable=self.attack_text, height=2, width=self.width_text)
        self.hit_entry_text = tk.StringVar()
        self.hit_entry = tk.Entry(self.root, textvariable=self.hit_entry_text, width=self.width_text)
        self.hit_mod_entry_text = tk.StringVar()
        self.hit_mod_entry = tk.Entry(self.root, textvariable=self.hit_mod_entry_text, width=self.width_text)
        self.str_entry_text = tk.StringVar()
        self.str_entry = tk.Entry(self.root, textvariable=self.str_entry_text, width=self.width_text)
        self.wnd_mod_entry_text = tk.StringVar()
        self.wnd_mod_entry = tk.Entry(self.root, textvariable=self.wnd_mod_entry_text, width=self.width_text)
        self.ap_entry_text = tk.StringVar()
        self.ap_entry = tk.Entry(self.root, textvariable=self.ap_entry_text, width=self.width_text)
        self.sv_mod_entry_text = tk.StringVar()
        self.sv_mod_entry = tk.Entry(self.root, textvariable=self.sv_mod_entry_text, width=self.width_text)
        self.dmg_entry_text = tk.StringVar()
        self.dmg_entry = tk.Entry(self.root, textvariable=self.dmg_entry_text, width=self.width_text)
        self.atk_entry_text = tk.StringVar()
        self.atk_entry = tk.Entry(self.root, textvariable=self.atk_entry_text, width=self.width_text)
        self.points_entry_text = tk.StringVar()
        self.points_entry = tk.Entry(self.root, textvariable=self.points_entry_text, width=self.width_text)
        self.models_entry_text = tk.StringVar()
        self.models_entry = tk.Entry(self.root, textvariable=self.models_entry_text, width=self.width_text)

        self.hit_reroll_entry = tk.Listbox(self.root, exportselection=False)
        self.wnd_reroll_entry = tk.Listbox(self.root, exportselection=False)
        self.hit_rules_frame = tk.Frame(self.root)
        self.hit_rules_add = tk.Button(self.hit_rules_frame, text="+", command=self.add_hit_rule)
        self.hit_rules_entry = tk.Listbox(self.hit_rules_frame, width=self.width_text)
        self.wnd_rules_frame = tk.Frame(self.root)
        self.wnd_rules_add = tk.Button(self.wnd_rules_frame, text="+", command=self.add_wnd_rule)
        self.wnd_rules_entry = tk.Listbox(self.wnd_rules_frame, width=self.width_text)

        self.attack_entry()
        self.rule_entry()

    def populate_rules_listbox(self):

        # noms des regles sur les jets pour toucher
        hit_rules_names_list = SpecialRuleHelper.build_hit_rule_list()
        self.hit_rules_entry.config(height=len(hit_rules_names_list))
        for item in hit_rules_names_list:
            self.hit_rules_entry.insert(tk.END, item)

        # noms des regle sur les jets pour blesser
        wnd_rules_names_list = SpecialRuleHelper.build_wnd_rule_list()
        self.wnd_rules_entry.config(height=len(wnd_rules_names_list))
        for item in wnd_rules_names_list:
            self.wnd_rules_entry.insert(tk.END, item)

        # Noms des autre regles

    def attack_entry(self):

        self.attack_text.set("Shooter")

        self.attack_label.grid(row=0, column=0)

        self.hit_entry_text.set("4+")
        self.hit_entry.grid(row=1, column=self.CI, sticky=tk.W + tk.E, padx=10)

        self.hit_mod_entry_text.set("+0")
        self.hit_mod_entry.grid(row=2, column=self.CI, sticky=tk.W + tk.E, padx=10)

        self.str_entry_text.set("3")
        self.str_entry.grid(row=3, column=self.CI, sticky=tk.W + tk.E, padx=10)

        self.wnd_mod_entry_text.set("+0")
        self.wnd_mod_entry.grid(row=4, column=self.CI, sticky=tk.W + tk.E, padx=10)

        self.ap_entry_text.set("0")
        self.ap_entry.grid(row=5, column=self.CI, sticky=tk.W + tk.E, padx=10)

        self.sv_mod_entry_text.set("+0")
        self.sv_mod_entry.grid(row=6, column=self.CI, sticky=tk.W + tk.E, padx=10)

        self.dmg_entry_text.set("1")
        self.dmg_entry.grid(row=7, column=self.CI, sticky=tk.W + tk.E, padx=10)

        self.atk_entry_text.set("2")
        self.atk_entry.grid(row=8, column=self.CI, sticky=tk.W + tk.E, padx=10)

        self.points_entry_text.set("4")
        self.points_entry.grid(row=9, column=self.CI, sticky=tk.W + tk.E, padx=10)

        self.models_entry_text.set("10")
        self.models_entry.grid(row=10, column=self.CI, sticky=tk.W + tk.E, padx=10)

    def rule_entry(self):

        self.hit_reroll_entry.config(height=3, width=self.width_text)
        for item in self.reroll_list:
            self.hit_reroll_entry.insert(tk.END, item)
        self.hit_reroll_entry.grid(row=11, column=self.CI, sticky=tk.W + tk.E, padx=10)

        self.wnd_reroll_entry.config(height=3, width=self.width_text)
        for item in self.reroll_list:
            self.wnd_reroll_entry.insert(tk.END, item)
        self.wnd_reroll_entry.grid(row=12, column=self.CI, sticky=tk.W + tk.E, padx=10)

        self.hit_rules_frame.grid(row=13, column=self.CI, sticky=tk.W + tk.E, padx=10)
        self.hit_rules_add.grid(row=0, column=0)
        self.hit_rules_entry.grid(row=0, column=1)

        self.wnd_rules_frame.grid(row=14, column=self.CI, sticky=tk.W + tk.E, padx=10)
        self.wnd_rules_add.grid(row=0, column=0)
        self.wnd_rules_entry.grid(row=0, column=1)

        self.populate_rules_listbox()

    def add_hit_rule(self):

        if self.hit_rules_entry.curselection():
            csel = self.hit_rules_entry.curselection()
            mf = self.hit_rules_entry.get(csel[0]).rstrip()
            self.Hit_Row += 1

            rule = RuleFrame.RuleFrame(self.hit_rules_frame, mf)
            rule.grid(row=self.Hit_Row, column=0, columnspan=2)

            self.Hit_Rules.append(rule)
            self.hit_rules_entry.delete(csel)

    def add_wnd_rule(self):

        if self.wnd_rules_entry.curselection():
            csel = self.wnd_rules_entry.curselection()
            mf = self.wnd_rules_entry.get(csel[0]).rstrip()
            self.Wnd_Row += 1

            rule = RuleFrame.RuleFrame(self.wnd_rules_frame, mf)
            rule.grid(row=self.Wnd_Row, column=0, columnspan=2)

            self.Wnd_Rules.append(rule)
            self.wnd_rules_entry.delete(csel)

    def gather_input(self):

        hit = clean_hit_input(self.hit_entry.get())

        hit_mod = clean_hit_input(self.hit_mod_entry.get())
        stre = clean_hit_input(self.str_entry.get())
        wnd_mod = clean_hit_input(self.wnd_mod_entry.get())
        ap = clean_hit_input(self.ap_entry.get())
        sv_mod = clean_hit_input(self.sv_mod_entry.get())
        dmg = self.dmg_entry.get()

        attks = self.atk_entry.get()
        pts = self.points_entry.get()
        models = self.models_entry.get()
        rate = int(models) * int(attks[0])
        if len(attks) > 0:
            rate = str(rate) + attks[1:]

        attk = Attack.Attack(rate, hit, stre, ap, dmg)

        attk.models = int(models)
        attk.points = int(pts)
        attk.hit_mod = hit_mod
        attk.wnd_mod = wnd_mod
        attk.sv_mod = sv_mod

        hitrules, wndrules = self.gather_rule_input()
        attk.add_hit_rules(hitrules)
        attk.add_wnd_rules(wndrules)

        return attk

    def gather_rule_input(self):

        hit_rules = []
        if len(self.Hit_Rules) > 0:
            for rule_input in self.Hit_Rules:
                hit_rules.append(rule_input.gather_input())

        wnd_rules = []
        if self.Wnd_Rules:
            for rule_input in self.Wnd_Rules:
                wnd_rules.append(rule_input.gather_input())

        return hit_rules, wnd_rules

    def destroy(self):

        self.attack_label.destroy()
        self.hit_entry.destroy()
        self.hit_mod_entry.destroy()
        self.str_entry.destroy()
        self.wnd_mod_entry.destroy()
        self.ap_entry.destroy()
        self.sv_mod_entry.destroy()
        self.dmg_entry.destroy()
        self.atk_entry.destroy()
        self.points_entry.destroy()
        self.models_entry.destroy()

        self.hit_reroll_entry.destroy()
        self.wnd_reroll_entry.destroy()
        self.hit_rules_frame.destroy()
        self.wnd_rules_frame.destroy()
