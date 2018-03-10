import tkinter as tk
from DiceSim2UI import RuleFrame
from DiceSim2 import Attack
from SpecialRules import SpecialRuleHelper

class AtkInput():
    '''
    classdocs
    '''


    def __init__(self, root, columnInput):
        '''
        Constructor
        '''

        self.none_text = "NONE"
        self.one_text = "ONES"
        self.miss_text = "MISS"
        self.reroll_list = [self.none_text, self.one_text, self.miss_text]

        self.Hit_Rules = []
        self.Wnd_Rules = []

        self.Hit_Row = 0
        self.Wnd_Row = 0
        self.CI = columnInput
        self.root = root
        self.attack_Entry()
        self.rule_Entry()

    def populate_Rules_Listbox(self):

        ##noms des regles sur les jets pour toucher
        hit_rules_names_list = SpecialRuleHelper.build_hit_rule_list()
        self.Entry_Hit_Rules.config(height = len(hit_rules_names_list))
        for item in hit_rules_names_list:
            self.Entry_Hit_Rules.insert(tk.END, item)

        ##noms des regle sur les jets pour blesser
        wnd_rules_names_list = SpecialRuleHelper.build_wnd_rule_list()
        self.Entry_Wnd_Rules.config(height = len(wnd_rules_names_list))
        for item in wnd_rules_names_list:
            self.Entry_Wnd_Rules.insert(tk.END, item)

        ##Noms des autre r�gles

    def attack_Entry(self):

        width_text = 8

        # self.Entry_Points_Text = tk.StringVar()
        # self.Entry_Points_Text.set("130")
        # self.Entry_Points = tk.Entry(self, textvariable=self.Entry_Points_Text, width=10)
        # self.Entry_Points.grid(row = next_row, column = 1)

        self.Text_Attk = tk.StringVar()
        self.Text_Attk.set("Shooter")
        self.Label_Attk = tk.Label(self.root, textvariable=self.Text_Attk, height = 2, width = width_text)
        self.Label_Attk.grid(row=0, column=0)


        self.Entry_Hit_Text = tk.StringVar()
        self.Entry_Hit_Text.set("4+")
        self.Entry_Hit = tk.Entry(self.root, textvariable=self.Entry_Hit_Text, width=width_text)
        self.Entry_Hit.grid(row = 1, column = self.CI, sticky=tk.W + tk.E, padx=10)


        self.Entry_Hit_Mod_Text = tk.StringVar()
        self.Entry_Hit_Mod_Text.set("+0")
        self.Entry_Hit_Mod = tk.Entry(self.root, textvariable=self.Entry_Hit_Mod_Text, width=width_text)
        self.Entry_Hit_Mod.grid(row = 2, column = self.CI, sticky=tk.W + tk.E ,padx=10)

        self.Entry_Str_Text = tk.StringVar()
        self.Entry_Str_Text.set("3")
        self.Entry_Str = tk.Entry(self.root, textvariable=self.Entry_Str_Text, width=width_text)
        self.Entry_Str.grid(row=3, column=self.CI, sticky=tk.W + tk.E, padx=10)

        self.Entry_Wnd_Mod_Text = tk.StringVar()
        self.Entry_Wnd_Mod_Text.set("+0")
        self.Entry_Wnd_Mod = tk.Entry(self.root, textvariable=self.Entry_Wnd_Mod_Text, width=width_text)
        self.Entry_Wnd_Mod.grid(row=4, column=self.CI, sticky=tk.W + tk.E, padx=10)

        self.Entry_AP_Text = tk.StringVar()
        self.Entry_AP_Text.set("0")
        self.Entry_AP = tk.Entry(self.root, textvariable=self.Entry_AP_Text, width=width_text)
        self.Entry_AP.grid(row=5, column=self.CI, sticky=tk.W + tk.E, padx=10)

        self.Entry_Sv_Mod_Text = tk.StringVar()
        self.Entry_Sv_Mod_Text.set("+0")
        self.Entry_Sv_Mod = tk.Entry(self.root, textvariable=self.Entry_Sv_Mod_Text, width=width_text)
        self.Entry_Sv_Mod.grid(row=6, column=self.CI, sticky=tk.W + tk.E, padx=10)

        self.Entry_Dmg_Text = tk.StringVar()
        self.Entry_Dmg_Text.set("1")
        self.Entry_Dmg = tk.Entry(self.root, textvariable=self.Entry_Dmg_Text, width=width_text)
        self.Entry_Dmg.grid(row=7, column=self.CI, sticky=tk.W + tk.E, padx=10)

        self.Entry_Atk_Text = tk.StringVar()
        self.Entry_Atk_Text.set("2")
        self.Entry_Atk = tk.Entry(self.root, textvariable=self.Entry_Atk_Text, width=width_text)
        self.Entry_Atk.grid(row=8, column=self.CI, sticky=tk.W + tk.E, padx=10)

        self.Entry_Points_Text = tk.StringVar()
        self.Entry_Points_Text.set("4")
        self.Entry_Points = tk.Entry(self.root, textvariable=self.Entry_Points_Text, width=width_text)
        self.Entry_Points.grid(row=9, column=self.CI, sticky=tk.W + tk.E, padx=10)

        self.Entry_Models_Text = tk.StringVar()
        self.Entry_Models_Text.set("10")
        self.Entry_Models = tk.Entry(self.root, textvariable=self.Entry_Models_Text, width=width_text)
        self.Entry_Models.grid(row=10, column=self.CI, sticky=tk.W + tk.E, padx=10)
        pass

    def rule_Entry(self):

        width_text = 8

        self.Entry_Hit_Reroll = tk.Listbox(self.root, exportselection=False)
        self.Entry_Hit_Reroll.config(height=3, width=width_text)
        for item in self.reroll_list:
            self.Entry_Hit_Reroll.insert(tk.END, item)

        self.Entry_Hit_Reroll.grid(row=11, column=self.CI, sticky=tk.W + tk.E, padx=10)

        self.Entry_Wnd_Reroll = tk.Listbox(self.root, exportselection=False)
        self.Entry_Wnd_Reroll.config(height=3, width=width_text)
        for item in self.reroll_list:
            self.Entry_Wnd_Reroll.insert(tk.END, item)

        self.Entry_Wnd_Reroll.grid(row=12, column=self.CI, sticky=tk.W + tk.E, padx=10)

        self.Hit_Rules_Frame = tk.Frame(self.root)
        self.Hit_Rules_Frame.grid(row=13, column=self.CI, sticky=tk.W + tk.E, padx=10)
        self.Hit_Rules_Add = tk.Button(self.Hit_Rules_Frame, text="+", command=self.add_Hit_Rule)
        self.Hit_Rules_Add.grid(row=0, column=0)
        self.Entry_Hit_Rules = tk.Listbox(self.Hit_Rules_Frame, width=width_text)
        self.Entry_Hit_Rules.grid(row=0, column=1)

        self.Wnd_Rules_Frame = tk.Frame(self.root)
        self.Wnd_Rules_Frame.grid(row=14, column=self.CI, sticky=tk.W + tk.E, padx=10)
        self.Wnd_Rules_Add = tk.Button(self.Wnd_Rules_Frame, text="+", command=self.add_Wnd_Rule)
        self.Wnd_Rules_Add.grid(row=0, column=0)
        self.Entry_Wnd_Rules = tk.Listbox(self.Wnd_Rules_Frame, width=width_text)
        self.Entry_Wnd_Rules.grid(row=0, column=1)

        self.populate_Rules_Listbox()

    def add_Hit_Rule(self):

        if (self.Entry_Hit_Rules.curselection()):
            csel = self.Entry_Hit_Rules.curselection()
            mf = self.Entry_Hit_Rules.get(csel[0]).rstrip()
            self.Hit_Row += 1

            rule = RuleFrame.RuleFrame(self.Hit_Rules_Frame, mf)
            rule.grid(row=self.Hit_Row, column=0, columnspan=2)

            self.Hit_Rules.append(rule)

            #             test_frame = tk.Frame(self.Hit_Rules_Frame)
            #
            #             label_text = tk.StringVar()
            #             label_text.set(mf)
            #             label= tk.Label(test_frame, textvariable=label_text)
            #
            #             testbutton = tk.Button(test_frame, text=mf)
            #             testbutton.config(relief=tk.SUNKEN)
            #
            #             entry_text = tk.StringVar()
            #             entry_text.set("6+")
            #             entry_rule = tk.Entry(test_frame, textvariable=entry_text, width=4)
            #
            #             entry_text2 = tk.StringVar()
            #             entry_text2.set("1")
            #             entry_rule2 = tk.Entry(test_frame, textvariable=entry_text2, width=4)
            #
            #             test_frame.grid(row = self.Hit_Row, column = 0, columnspan = 2, pady=1)
            #             label.grid(row=0, column = 0, columnspan=2)
            #             #testbutton.grid(row = 0, column = 0, columnspan=2)
            #             entry_rule.grid(row = self.Hit_Row+1, column = 0, sticky=tk.W + tk.E)
            #             entry_rule2.grid(row = self.Hit_Row+1, column = 1, sticky=tk.W + tk.E )
            #

            self.Entry_Hit_Rules.delete(csel)
        # self.Hit_Rules_Add.grid(row = self.Hit_Row, column = 0, sticky=tk.N )
        # self.Entry_Hit_Rules.grid(row = 1, column = 1, sticky=tk.N)

        # for widget in self.Hit_Rules_Frame.grid_slaves():

        #   print(widget.grid_info())

    def add_Wnd_Rule(self):

        if (self.Entry_Wnd_Rules.curselection()):
            csel = self.Entry_Wnd_Rules.curselection()
            mf = self.Entry_Wnd_Rules.get(csel[0]).rstrip()
            self.Wnd_Row += 1

            rule = RuleFrame.RuleFrame(self.Wnd_Rules_Frame, mf)
            rule.grid(row=self.Wnd_Row, column=0, columnspan=2)

            self.Wnd_Rules.append(rule)
            self.Entry_Wnd_Rules.delete(csel)

    def gather_input(self):

        hit = self.Entry_Hit.get().strip("+")

        # if(len(hit) != 2):

        # raise ValueError("The hit rate isn't in the right format")

        hit = int(hit)
        hit_mod = int(self.Entry_Hit_Mod.get().strip("+"))
        stre = self.Entry_Str.get()
        stre = int(stre)
        wnd_mod = int(self.Entry_Wnd_Mod.get().strip("+"))
        AP = self.Entry_AP.get()
        AP = int(AP)
        sv_mod = int(self.Entry_Sv_Mod.get().strip("+"))
        dmg = self.Entry_Dmg.get()

        attks = self.Entry_Atk.get()
        pts = self.Entry_Points.get()
        models = self.Entry_Models.get()
        rate = int(models) * int(attks[0])
        if (len(attks) > 0):
            rate = str(rate) + attks[1:]

        # print(rate)
        # print(models)
        # print(pts)

        attk = Attack.Attack(rate, hit, stre, AP, dmg)

        attk.models = int(models)
        attk.points = int(pts)
        attk.hit_mod = hit_mod
        attk.wnd_mod = wnd_mod
        attk.sv_mod = sv_mod

        # attk.set_Models(int(models))
        # attk.set_Points(int(pts))
        # attk.set_Mods(hit_mod, wnd_mod, sv_mod)

        hitrules, wndrules = self.gather_rule_input(attk)
        attk.add_hit_rules(hitrules)
        attk.add_wnd_rules(wndrules)

        return attk

    def gather_rule_input(self, attack):

        hit_rules = []
        # print(self.Hit_Rules)
        if (len(self.Hit_Rules) > 0):
            for rule_input in self.Hit_Rules:
                hit_rules.append(rule_input.gather_input())

        wnd_rules = []
        if (self.Wnd_Rules):
            for rule_input in self.Wnd_Rules:
                wnd_rules.append(rule_input.gather_input())

        return hit_rules, wnd_rules

    def destroy(self):

        self.Label_Attk.destroy()
        self.Entry_Hit.destroy()
        self.Entry_Hit_Mod.destroy()
        self.Entry_Str.destroy()
        self.Entry_Wnd_Mod.destroy()
        self.Entry_AP.destroy()
        self.Entry_Sv_Mod.destroy()
        self.Entry_Dmg.destroy()
        self.Entry_Atk.destroy()
        self.Entry_Points.destroy()
        self.Entry_Models.destroy()

        self.Entry_Hit_Reroll.destroy()
        self.Entry_Wnd_Reroll.destroy()
        self.Hit_Rules_Frame.destroy()
        self.Wnd_Rules_Frame.destroy()

