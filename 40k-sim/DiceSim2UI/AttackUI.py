 
 
import tkinter as tk
from DiceSim2UI import InputAttackUI

 
class AttackUI(tk.Frame):
    """

    """

    def __init__(self, root):
        """

        Parameters
        ----------
        root : tk.Frame
            The parent Frame
        """
        width_text = 10

        tk.Frame.__init__(self, root)
           
        self.attackUIList = []
        self.currentColumn = 1
        self.add_input_attackui()

        self.Label_Hits = tk.StringVar()
        self.Label_Hits.set("Hit")
        self.Text_Hits = tk.Label(self, textvariable=self.Label_Hits,  width=width_text)
        self.Text_Hits.grid(row=1, column=0)

        self.Label_Hits_Mod = tk.StringVar()
        self.Label_Hits_Mod.set("Hit Mod")
        self.Text_Hits_Mod = tk.Label(self, textvariable=self.Label_Hits_Mod, width=width_text)
        self.Text_Hits_Mod.grid(row=2, column=0)

        self.Label_Str = tk.StringVar()
        self.Label_Str.set("Str")
        self.Text_Str = tk.Label(self, textvariable=self.Label_Str,  width=width_text)
        self.Text_Str.grid(row=3, column=0)

        self.Label_Wound_Mod = tk.StringVar()
        self.Label_Wound_Mod.set("Wnd Mod")
        self.Text_Wound_Mod = tk.Label(self, textvariable=self.Label_Wound_Mod, width=width_text)
        self.Text_Wound_Mod.grid(row=4, column=0)

        self.Label_AP = tk.StringVar()
        self.Label_AP.set("AP")
        self.Text_AP = tk.Label(self, textvariable=self.Label_AP,  width=width_text)
        self.Text_AP.grid(row=5, column=0)

        self.Label_Save_Mod = tk.StringVar()
        self.Label_Save_Mod.set("Save Mod")
        self.Text_Save_Mod = tk.Label(self, textvariable=self.Label_Save_Mod, width=width_text)
        self.Text_Save_Mod.grid(row=6, column=0)

        self.Text_DMG = tk.StringVar()
        self.Text_DMG.set("DMG")
        self.Label_DMG = tk.Label(self, textvariable=self.Text_DMG,  width=width_text)
        self.Label_DMG.grid(row=7, column=0)

        self.Text_Atk = tk.StringVar()
        self.Text_Atk.set("Att")
        self.Label_Atk = tk.Label(self, textvariable=self.Text_Atk,  width=width_text)
        self.Label_Atk.grid(row=8, column=0)

        self.Text_Points = tk.StringVar()
        self.Text_Points.set("Points")
        self.Label_Points = tk.Label(self, textvariable=self.Text_Points, width=width_text)
        self.Label_Points.grid(row=9, column=0)

        self.Text_Models = tk.StringVar()
        self.Text_Models.set("Nb Models")
        self.Label_Models = tk.Label(self, textvariable=self.Text_Models, width=width_text)
        self.Label_Models.grid(row=10, column=0)

        self.Text_Hit_Reroll = tk.StringVar()
        self.Text_Hit_Reroll.set("Hit reroll")
        self.Label_Hit_Reroll = tk.Label(self, textvariable=self.Text_Hit_Reroll,  width=width_text)
        self.Label_Hit_Reroll.grid(row=11, column=0, sticky=tk.W)

        self.Text_Wnd_Reroll = tk.StringVar()
        self.Text_Wnd_Reroll.set("Wnd reroll")
        self.Label_Wnd_Reroll = tk.Label(self, textvariable=self.Text_Wnd_Reroll,  width=width_text)
        self.Label_Wnd_Reroll.grid(row=12, column=0, sticky=tk.W)

        self.Text_Hit_Rules = tk.StringVar()
        self.Text_Hit_Rules.set("Hit rules")
        self.Label_Hit_Rules = tk.Label(self, textvariable=self.Text_Hit_Rules,  width=width_text)
        self.Label_Hit_Rules.grid(row=13, column=0, sticky=tk.W)

        self.Text_Wnd_Rules = tk.StringVar()
        self.Text_Wnd_Rules.set("Wnd rules")
        self.Label_Wnd_Rules = tk.Label(self, textvariable=self.Text_Wnd_Rules,  width=width_text)
        self.Label_Wnd_Rules.grid(row=14, column=0, sticky=tk.W)
     
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

