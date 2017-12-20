'''
Created on Dec 5, 2017
 
@author: Samuel
'''
 
import tkinter as tk
import numpy
 
class TableEff(tk.Frame):
 
 
    def __init__(self, root):
        '''
        Constructor
        '''
        numpy.set_printoptions(suppress = True)
        tk.Frame.__init__(self, root)
        self.current_Row = 1
         
        self.add_top_label()
         
    def add_top_label(self):
        self.Text_Nb = tk.StringVar()
        self.Text_Nb.set("Sim #")
        self.SimNbLabel = tk.Label(self, textvariable=self.Text_Nb ,width = 5)
        self.SimNbLabel.grid(row = 0, column = 0)
         
        self.Text_Eff = tk.StringVar()
        self.Text_Eff.set("Eff w/ moral")
        self.EffLabel = tk.Label(self, textvariable = self.Text_Eff, width = 10)
        self.EffLabel.grid(row = 0, column = 1)
         
    def add_Eff(self, name, eff):
         
        TextName = tk.StringVar()
        TextName.set(name)
        labelName = tk.Label(self, textvariable=TextName, width = 5)
        labelName.grid(row = self.current_Row, column = 0)
         
        TextEff = tk.StringVar()
        TextEff.set(str(eff)[:4])
        labelEff = tk.Label(self, textvariable=TextEff, width = 10)
        labelEff.grid(row = self.current_Row, column = 1)
         
        self.current_Row += 1
     