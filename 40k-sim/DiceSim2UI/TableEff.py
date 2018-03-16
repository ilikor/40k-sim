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
        numpy.set_printoptions(suppress=True)
        tk.Frame.__init__(self, root)
        self.current_Row = 1

        self.add_top_label()
        self.text_nb = tk.StringVar()
        self.sim_nb_label = tk.Label(self, textvariable=self.text_nb, width=5)
        self.eff_label = tk.Label(self, textvariable=self.text_eff, width=10)
        self.text_eff = tk.StringVar()

    def add_top_label(self):

        self.text_nb.set("Sim #")
        self.sim_nb_label.grid(row=0, column=0)

        self.text_eff.set("Eff w/ moral")
        self.eff_label.grid(row=0, column=1)

    def add_eff(self, name, eff):

        name_text = tk.StringVar()
        name_text.set(name)
        name_label = tk.Label(self, textvariable=name_text, width=5)
        name_label.grid(row=self.current_Row, column=0)

        eff_text = tk.StringVar()
        eff_text.set(str(eff)[:4])
        eff_label = tk.Label(self, textvariable=TextEff, width=10)
        eff_label.grid(row=self.current_Row, column=1)

        self.current_Row += 1
