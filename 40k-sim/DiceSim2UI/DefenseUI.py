

import tkinter as tk

from DiceSim2 import Defense

class DefenseUI(tk.Frame):


    def __init__(self, root):
        '''
        '''
       # self.Text_Hits = tk.Label(self, textvariable=self.Label_Hits,  width = width_text)
       # self.Text_Hits.grid(row = 1, column = 0)
       
        tk.Frame.__init__(self, root)
       
        self.defenseLabel()
        self.defenseEntry()
        self.FnP_List = []
        
    def defenseLabel(self):
        
        width_text = 10
        
        self.Text_Tough = tk.StringVar()
        self.Text_Tough.set("T")
        self.Label_Tough = tk.Label(self, textvariable=self.Text_Tough, width = width_text )
        self.Label_Tough.grid(row = 0, column = 0)
        
        self.Text_Wounds = tk.StringVar()
        self.Text_Wounds.set("W")
        self.Label_Wounds = tk.Label(self, textvariable=self.Text_Wounds, width = width_text)
        self.Label_Wounds.grid(row = 1, column = 0)
        
        self.Text_Save = tk.StringVar()
        self.Text_Save.set("Sv")
        self.Label_Save = tk.Label(self, textvariable=self.Text_Save, width = width_text)
        self.Label_Save.grid(row = 2, column = 0)
        
        self.Text_ISave = tk.StringVar()
        self.Text_ISave.set("ISv")
        self.Label_ISave = tk.Label(self, textvariable=self.Text_ISave, width = width_text)
        self.Label_ISave.grid(row = 3, column = 0)
        
        self.Text_Hit_Mod = tk.StringVar()
        self.Text_Hit_Mod.set("Hit_Mod")
        self.Label_Hit_Mod = tk.Label(self, textvariable=self.Text_Hit_Mod, width = width_text)
        self.Label_Hit_Mod.grid(row = 4, column = 0)
        
        self.Text_Wnd_Mod = tk.StringVar()
        self.Text_Wnd_Mod.set("Wnd Mod")
        self.Label_Wnd_Mod = tk.Label(self, textvariable=self.Text_Wnd_Mod, width=width_text)
        self.Label_Wnd_Mod.grid(row = 5, column = 0)
        
        self.Text_Save_Mod = tk.StringVar()
        self.Text_Save_Mod.set("Save Mod")
        self.Label_Save_Mod = tk.Label(self, textvariable=self.Text_Save_Mod, width=width_text)
        self.Label_Save_Mod.grid(row = 6, column = 0)
        
        self.Text_Morale_Text = tk.StringVar()
        self.Text_Morale_Text.set("Moral")
        self.Label_Morale = tk.Label(self, textvariable=self.Text_Morale_Text, width=width_text)
        self.Label_Morale.grid(row = 7, column = 0)
        
        self.Text_Moral_Rule = tk.StringVar()
        self.Text_Moral_Rule.set("Moral Rule")
        self.Label_Moral_Rule = tk.Label(self, textvariable=self.Text_Moral_Rule, width=width_text)
        self.Label_Moral_Rule.grid(row = 8, column = 0)
        
        self.Text_Points = tk.StringVar()
        self.Text_Points.set("Points")
        self.Label_Points = tk.Label(self, textvariable=self.Text_Points, width=width_text)
        self.Label_Points.grid(row = 9, column = 0)
        
        
        
        self.Text_FnP = tk.StringVar()
        self.Text_FnP.set("FnP")
        self.Label_FnP = tk.Label(self, textvariable=self.Text_FnP, width=width_text)
        self.Label_FnP.grid(row = 10, column = 0)
 
    
    def defenseEntry(self):
        
         
        #self.Entry_Hit_Text = tk.StringVar()
        #self.Entry_Hit_Text.set("4+")
        #self.Entry_Hit = tk.Entry(self.root, textvariable=self.Entry_Hit_Text, width=6)
        #self.Entry_Hit.grid(row = 1, column = self.CI)
        
        
        width_text = 8
        
        self.Entry_Tough_Text = tk.StringVar()
        self.Entry_Tough_Text.set("4")
        self.Entry_Tough = tk.Entry(self, textvariable=self.Entry_Tough_Text, width=width_text)
        self.Entry_Tough.grid(row =0 , column = 1)
        
        self.Entry_Wounds_Text = tk.StringVar()
        self.Entry_Wounds_Text.set("1")
        self.Entry_Wounds = tk.Entry(self, textvariable=self.Entry_Wounds_Text, width=width_text)
        self.Entry_Wounds.grid(row = 1, column = 1)
        
        self.Entry_Save_Text = tk.StringVar()
        self.Entry_Save_Text.set("3+")
        self.Entry_Save = tk.Entry(self, textvariable=self.Entry_Save_Text, width=width_text)
        self.Entry_Save.grid(row = 2, column = 1)
        
        self.Entry_ISave_Text = tk.StringVar()
        self.Entry_ISave_Text.set("--")
        self.Entry_ISave = tk.Entry(self, textvariable=self.Entry_ISave_Text, width=width_text)
        self.Entry_ISave.grid(row = 3, column = 1)
        
        self.Entry_Hit_Mod_Text = tk.StringVar()
        self.Entry_Hit_Mod_Text.set("+0")
        self.Entry_Hit_Mod = tk.Entry(self, textvariable=self.Entry_Hit_Mod_Text, width=width_text)
        self.Entry_Hit_Mod.grid(row = 4, column = 1)
        
        self.Entry_Wnd_Mod_Text = tk.StringVar()
        self.Entry_Wnd_Mod_Text.set("+0")
        self.Entry_Wnd_Mod = tk.Entry(self, textvariable=self.Entry_Wnd_Mod_Text, width=width_text)
        self.Entry_Wnd_Mod.grid(row = 5, column = 1)
        
        self.Entry_Save_Mod_Text = tk.StringVar()
        self.Entry_Save_Mod_Text.set("+0")
        self.Entry_Save_Mod = tk.Entry(self, textvariable=self.Entry_Save_Mod_Text, width=width_text)
        self.Entry_Save_Mod.grid(row = 6, column = 1)
        
        self.Entry_Morale_Text = tk.StringVar()
        self.Entry_Morale_Text.set("7")
        self.Entry_Morale = tk.Entry(self, textvariable=self.Entry_Morale_Text, width=width_text)
        self.Entry_Morale.grid(row = 7, column = 1)
        
        #self.Entry_Text_Moral_Rule = tk.StringVar()
        # self.Entry_Moral_Rule.set("Moral Rule")
        #self.Label_Moral_Rule = tk.Label(self, textvariable=self.Label_Moral_Rule, width=width_text)
        #self.Label_Moral_Rule.grid(row = 8, column = 0)
        
        self.Entry_Moral_Rule = tk.Listbox(self, exportselection=False)
        self.Entry_Moral_Rule.config(height = 5, width=width_text)
        for item in ["NONE", "CAN", "MUST", "COMMI", "KNIFE"]:
            self.Entry_Moral_Rule.insert(tk.END, item)
        #self.Entry_Moral_Rule.insert(tk.END, "NONE")
        #self.Entry_Moral_Rule.insert(tk.END, "CAN")
        #self.Entry_Moral_Rule.insert(tk.END, "MUST")
        #self.Entry_Moral_Rule.insert(tk.END, "COMMI")
        #self.Entry_Moral_Rule.insert(tk.END, "KNIFE")
        self.Entry_Moral_Rule.grid(row = 8, column = 1)
        
        self.Entry_Moral_Rule.selection_set(0, last=None)
        
        self.Entry_Points_Text = tk.StringVar()
        self.Entry_Points_Text.set("14")
        self.Entry_Points = tk.Entry(self, textvariable=self.Entry_Points_Text, width=width_text)
        self.Entry_Points.grid(row = 9, column = 1)
        
        
        self.FnP_Frame = tk.Frame(self)
        self.FnP_Frame.grid(row = 10, column = 1)
    
    
    def add_FnP(self):
        
        FnP_Entry_Text = tk.StringVar()
        FnP_Entry_Text.set("5+")
        
        FnP_Entry = tk.Entry(self.FnP_Frame, textvariable=FnP_Entry_Text, width=6)
        FnP_Entry.grid(row = len(self.FnP_List), column = 0)
        
        self.FnP_List.append(FnP_Entry)
        pass
    
    def remove_FnP(self):
        
        if(len(self.FnP_List) > 0):
            self.FnP_List.pop().destroy()
        
        pass
    
    def gather_Input(self):
        try:
            T = self.clean_input(self.Entry_Tough.get())
            W = self.clean_input(self.Entry_Wounds.get())
            
            Sv = self.clean_input(self.Entry_Save.get())
            
            ISv = self.clean_ISV(self.Entry_ISave.get())
            
            HM = self.clean_input(self.Entry_Hit_Mod.get())
            WM = self.clean_input(self.Entry_Wnd_Mod.get())
            SM = self.clean_input(self.Entry_Save.get())
            moral = self.clean_input(self.Entry_Morale.get())
            pts = self.clean_input(self.Entry_Points.get())
            FnP = []
            
            moral_rule_selection = self.Entry_Moral_Rule.curselection()
            print(moral_rule_selection)
            moral_rule = ""
            if(moral_rule_selection):
                
                moral_rule = self.Entry_Moral_Rule.get(moral_rule_selection)
                print(moral_rule)
            else:
                
                moral_rule = "NONE"
            
            D = Defense.Defense(T,W,Sv,ISv, FnP, moral, pts )
            D.moral_rule = moral_rule
            
            for FnP in self.FnP_List:
                
                nextFnP = self.clean_input(FnP.get())
        
        except ValueError as Ve:
        
            raise Ve
        
        
        
        
        
        return D
        
    def clean_input(self, input):
      
        retour = 0
        input = input.strip("+")
      #  print(input)
        if(input.isnumeric()): ##Is input est un nombre, alors on regarde s'il est >0
            
            
                
            retour = int(input)
            
            
                
        else: raise ValueError("Valeur doit être numerique")       
        return retour

    def clean_ISV(self, input):
        ##Il est probable qu'une unité n'ait pas de save invuln, dans ce cas on vérifie si la save invuln est un nombre, autrement on retourne NONE
        
        
        input = input.strip("+")
        if(input.isnumeric()):
            
            return int(input)
        
        else:
            
            return None
 
        