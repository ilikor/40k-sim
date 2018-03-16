 
 
import tkinter as tk
from DiceSim2UI import InputAttackUI

 
class AttackUI(tk.Frame):
    """

    """

    def __init__(self, root):
        """

        Parameters
        ----------
        root : tk.tk
            The top level controller
        """
        width_text = 10

        tk.Frame.__init__(self, root)
           
        self.attackUIList = []
        self.currentColumn = 1
        self.add_input_attackui()

        self.hits_label = tk.StringVar()
        self.hits_label.set("Hit")
        self.hits_text = tk.Label(self, textvariable=self.hits_label, width=width_text)
        self.hits_text.grid(row=1, column=0)

        self.hits_mod_label = tk.StringVar()
        self.hits_mod_label.set("Hit Mod")
        self.hits_mod_text = tk.Label(self, textvariable=self.hits_mod_label, width=width_text)
        self.hits_mod_text.grid(row=2, column=0)

        self.str_label = tk.StringVar()
        self.str_label.set("Str")
        self.str_text = tk.Label(self, textvariable=self.str_label, width=width_text)
        self.str_text.grid(row=3, column=0)

        self.wnd_mod_label = tk.StringVar()
        self.wnd_mod_label.set("Wnd Mod")
        self.wnd_mod_text = tk.Label(self, textvariable=self.wnd_mod_label, width=width_text)
        self.wnd_mod_text.grid(row=4, column=0)

        self.ap_label = tk.StringVar()
        self.ap_label.set("AP")
        self.ap_text = tk.Label(self, textvariable=self.ap_label, width=width_text)
        self.ap_text.grid(row=5, column=0)

        self.save_mod_label = tk.StringVar()
        self.save_mod_label.set("Save Mod")
        self.save_mod_text = tk.Label(self, textvariable=self.save_mod_label, width=width_text)
        self.save_mod_text.grid(row=6, column=0)

        self.dmg_text = tk.StringVar()
        self.dmg_text.set("DMG")
        self.dmg_label = tk.Label(self, textvariable=self.dmg_text, width=width_text)
        self.dmg_label.grid(row=7, column=0)

        self.atk_text = tk.StringVar()
        self.atk_text.set("Att")
        self.atk_label = tk.Label(self, textvariable=self.atk_text, width=width_text)
        self.atk_label.grid(row=8, column=0)

        self.points_text = tk.StringVar()
        self.points_text.set("Points")
        self.points_label = tk.Label(self, textvariable=self.points_text, width=width_text)
        self.points_label.grid(row=9, column=0)

        self.models_text = tk.StringVar()
        self.models_text.set("Nb Models")
        self.models_label = tk.Label(self, textvariable=self.models_text, width=width_text)
        self.models_label.grid(row=10, column=0)

        self.hit_reroll_text = tk.StringVar()
        self.hit_reroll_text.set("Hit reroll")
        self.hit_reroll_label = tk.Label(self, textvariable=self.hit_reroll_text, width=width_text)
        self.hit_reroll_label.grid(row=11, column=0, sticky=tk.W)

        self.wnd_reroll_text = tk.StringVar()
        self.wnd_reroll_text.set("Wnd reroll")
        self.wnd_reroll_label = tk.Label(self, textvariable=self.wnd_reroll_text, width=width_text)
        self.wnd_reroll_label.grid(row=12, column=0, sticky=tk.W)

        self.hit_rules_text = tk.StringVar()
        self.hit_rules_text.set("Hit rules")
        self.hit_rules_label = tk.Label(self, textvariable=self.hit_rules_text, width=width_text)
        self.hit_rules_label.grid(row=13, column=0, sticky=tk.W)

        self.wnd_rules_text = tk.StringVar()
        self.wnd_rules_text.set("Wnd rules")
        self.wnd_rules_label = tk.Label(self, textvariable=self.wnd_rules_text, width=width_text)
        self.wnd_rules_label.grid(row=14, column=0, sticky=tk.W)

    def gather_input_from_child(self):
         
        attacker_list = []
         
        for shooters in self.attackUIList:
            attacker_list.append(shooters.gather_input())
             
        return attacker_list

    def add_input_attackui(self):
 
        new_atkui = InputAttackUI.AtkInput(self, self.currentColumn)
        self.attackUIList.append(new_atkui)
        self.currentColumn += 1
         
    def remove_input_attackui(self):
        if len(self.attackUIList) > 0:
            self.attackUIList.pop().destroy()
