

import tkinter as tk
from DiceSim2 import Attack

class AtkInput():
    '''
    classdocs
    '''


    def __init__(self, root, columnInput):
        '''
        Constructor
        '''
        self.CI = columnInput
        self.root = root
        self.attack_Entry()
        
    def attack_Entry(self):
        
        #self.Entry_Points_Text = tk.StringVar()
        #self.Entry_Points_Text.set("130")
        #self.Entry_Points = tk.Entry(self, textvariable=self.Entry_Points_Text, width=10)
        #self.Entry_Points.grid(row = next_row, column = 1)
        
        self.Text_Attk = tk.StringVar()
        self.Text_Attk.set("Shooter")
        self.Label_Attk = tk.Label(self.root, textvariable=self.Text_Attk, height = 2, width = 6)
        self.Label_Attk.grid(row=0, column=0)
        
        
        self.Entry_Hit_Text = tk.StringVar()
        self.Entry_Hit_Text.set("4+")
        self.Entry_Hit = tk.Entry(self.root, textvariable=self.Entry_Hit_Text, width=6)
        self.Entry_Hit.grid(row = 1, column = self.CI)
        
        
        self.Entry_Hit_Mod_Text = tk.StringVar()
        self.Entry_Hit_Mod_Text.set("+0")
        self.Entry_Hit_Mod = tk.Entry(self.root, textvariable=self.Entry_Hit_Mod_Text, width=6)
        self.Entry_Hit_Mod.grid(row = 2, column = self.CI)
        
        
        self.Entry_Str_Text = tk.StringVar()
        self.Entry_Str_Text.set("3")
        self.Entry_Str = tk.Entry(self.root, textvariable=self.Entry_Str_Text, width=6)
        self.Entry_Str.grid(row = 3, column = self.CI)
        
        
        self.Entry_Wnd_Mod_Text = tk.StringVar()
        self.Entry_Wnd_Mod_Text.set("+0")
        self.Entry_Wnd_Mod = tk.Entry(self.root, textvariable=self.Entry_Wnd_Mod_Text, width=6)
        self.Entry_Wnd_Mod.grid(row = 4, column = self.CI)
        
        
        self.Entry_AP_Text = tk.StringVar()
        self.Entry_AP_Text.set("0")
        self.Entry_AP = tk.Entry(self.root, textvariable=self.Entry_AP_Text, width=6)
        self.Entry_AP.grid(row = 5, column = self.CI)
        
        
        self.Entry_Sv_Mod_Text = tk.StringVar()
        self.Entry_Sv_Mod_Text.set("+0")
        self.Entry_Sv_Mod = tk.Entry(self.root, textvariable=self.Entry_Sv_Mod_Text, width=6)
        self.Entry_Sv_Mod.grid(row = 6, column = self.CI)
        
        
        self.Entry_Dmg_Text = tk.StringVar()
        self.Entry_Dmg_Text.set("1")
        self.Entry_Dmg = tk.Entry(self.root, textvariable=self.Entry_Dmg_Text, width=6)
        self.Entry_Dmg.grid(row = 7, column = self.CI)
        
        
        self.Entry_Atk_Text = tk.StringVar()
        self.Entry_Atk_Text.set("2")
        self.Entry_Atk = tk.Entry(self.root, textvariable=self.Entry_Atk_Text, width=6)
        self.Entry_Atk.grid(row = 8, column = self.CI)
        
        
        self.Entry_Points_Text = tk.StringVar()
        self.Entry_Points_Text.set("4")
        self.Entry_Points = tk.Entry(self.root, textvariable=self.Entry_Points_Text, width=6)
        self.Entry_Points.grid(row = 9, column = self.CI)
        
        
        self.Entry_Models_Text = tk.StringVar()
        self.Entry_Models_Text.set("10")
        self.Entry_Models = tk.Entry(self.root, textvariable=self.Entry_Models_Text, width=6)
        self.Entry_Models.grid(row = 10, column = self.CI, )
        pass
    
    def gather_input(self):
        
        hit = self.Entry_Hit.get()
        
        if(len(hit) != 2):
            
            raise ValueError("The hit rate isn't in the right format")
        
        hit = int(hit[0])
        
        hit_mod = int(self.Entry_Hit_Mod.get()[1])
        
        stre = self.Entry_Str.get()
        
        stre = int(stre)
        
        wnd_mod = int(self.Entry_Wnd_Mod.get()[1])
        
        AP = self.Entry_AP.get()
        AP = int(AP)
        
        sv_mod = int(self.Entry_Sv_Mod.get()[1])
        
        dmg = self.Entry_Dmg.get()
        dmg = int(dmg)
        
        attks = self.Entry_Atk.get()
        pts = self.Entry_Points.get()   
        models = self.Entry_Models.get()
        
        
        rate = int(models)*int(attks[0])
        
        if(len(attks) > 0):
            
            rate = str(rate) + attks[1:]
            
        
        #print(rate)
        print(models)
        print(pts)
        
        
        attk = Attack.Attack(rate, hit, stre, AP, dmg)
        attk.set_Models(int(models))
        attk.set_Points(int(pts))
        attk.set_Mods(hit_mod, wnd_mod, sv_mod)
        
        return attk
        
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

        