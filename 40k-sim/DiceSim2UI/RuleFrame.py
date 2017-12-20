'''
Created on Dec 17, 2017

@author: Samuel
'''
import tkinter as tk

class RuleFrame(tk.Frame):
    
    def __init__(self, root, name_init):
        
        tk.Frame.__init__(self, root)
        self.name = name_init
        self.root = root
        self.wt = 6
        
        self.fillFrame()
        self.layoutFrame()
        
        
    def fillFrame(self):
        """
        ICI ON FAIT LA CREATION DES OBJETS QUI SERONT PLACER DANS LE FRAME
        """
        
        self.label_text = tk.StringVar()
        self.label_text.set(self.name)
        self.label = tk.Label(self, textvariable=self.label_text, width=self.wt*2)
        
        self.target_text = tk.StringVar()
        self.target_text.set("target")
        self.target_entry = tk.Entry(self, textvariable=self.target_text, width=self.wt)
        
        self.rule_text = tk.StringVar()
        self.rule_text.set("effect")
        self.rule_entry = tk.Entry(self, textvariable=self.rule_text, width=self.wt)

        
    def layoutFrame(self):
        """
        ICI ON FAIT LE PLACEMENT DES ELEMENTS DANS LE FRAME
        """
        
        self.label.grid(row=0, column=0, columnspan = 2)
        self.target_entry.grid(row = 1, column = 0)
        self.rule_entry.grid(row = 1, column = 1)
       
    def gather_input(self):
        
        target = self.target_entry.get().strip("+")
        rule = self.rule_entry.get().strip("+")
        
        return [target, rule, self.name] 

if __name__ == '__main__':
    pass