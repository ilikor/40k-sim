 
 
from decimal import *
import tkinter as tk
from tkinter import messagebox
 
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy
 
from DiceSim2.Simulation2 import Simulation
from DiceSim2UI import TableEff
from DiceSim2UI import AttackUI
from DiceSim2UI import DefenseUI

matplotlib.use("TkAgg")
numpy.set_printoptions(suppress=True)
numpy.set_printoptions(precision=3, suppress=True)
getcontext().prec = 3


class SimUI:

    def __init__(self):

        self.color_cycle = ["b", "g", "y", "k", "r", "c", "m" ]
        self.color_number = 0
     
        self.root = tk.Tk()
        self.sim = Simulation()
        # Adding canvas to draw on
        self.canvas_global = tk.Frame(self.root, height=300, width=400)
        self.canvas_global.grid(row=1, column=1)
        self.f = Figure(figsize=(4, 2.5), dpi=100)
        self.aaa = self.f.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.f, self.canvas_global)
        # Adding table for eff stats
        self.efficiency_table = TableEff.TableEff(self.root)
        self.efficiency_table.grid(row=2, column=1)
        # Adding frame for attack input
        self.att = AttackUI.AttackUI(self.root)
        self.att.grid(row=1, column=0)
        # Adding frame for defender input
        self.defender = DefenseUI.DefenseUI(self.root)
        self.defender.grid(row=1, column=2)

        # Adding frame with buttons for attack UI
        self.ButtonFrame = tk.Frame(self.root)
        self.ButtonFrame.grid(row=0, column=0, sticky=tk.W + tk.E)
         
        self.Button_Add = tk.Button(self.ButtonFrame, text="Add Shooters", command=self.att.add_input_attackui)
        self.Button_Add.grid(row=0, column=0, sticky=tk.W)
         
        self.Button_Remove = tk.Button(self.ButtonFrame, text="Remove", command=self.att.remove_input_attackui)
        self.Button_Remove.grid(row=0, column=1, sticky=tk.E)
        # Adding frame with buttons for simulation purposes
        self.ButtonSimFrame = tk.Frame(self.root)
        self.ButtonSimFrame.grid(row=0, column=1)
         
        self.Button_Simulation = tk.Button(self.ButtonSimFrame, text="Simulate", command=self.button_simulate)
        self.Button_Simulation.grid(row=0, column=0)
         
        self.Button_Clean = tk.Button(self.ButtonSimFrame, text="Clean", command=self.button_clean_sim)
        self.Button_Clean.grid(row=0, column=1)
        # Adding frame with buttons for defense UI
        self.ButtonDefenderFrame = tk.Frame(self.root)
        self.ButtonDefenderFrame.grid(row=0, column=2)
     
        self.FnP_Add_Button = tk.Button(self.ButtonDefenderFrame, text="Add FnP", command=self.defender.add_FnP)
        self.FnP_Add_Button.grid(row=0, column=0)
         
        self.FnP_Remove_Button = tk.Button(self.ButtonDefenderFrame, text="RIP FnP", command=self.defender.remove_FnP)
        self.FnP_Remove_Button.grid(row=0, column=1)
         
    def button_clean_sim(self):
         
        self.aaa.clear()
        self.color_number = 0
        self.canvas.show()
        self.efficiency_table.destroy()
        self.efficiency_table = TableEff.TableEff(self.root)
        self.efficiency_table.grid(row=2, column=1)
     
    def button_simulate(self):

        try:
            attackers = self.att.gather_input_from_child()
            defende = self.defender.gather_Input()
            self.sim.change_Defender(defende)
            self.sim.add_Attackers(attackers)

            deds, wnd, eff, moral = self.sim.overall_Sim(5000)
             
            dmgav = numpy.average(deds)
             
            effav = numpy.average(eff)
             
            values = numpy.bincount(deds)
            values = values/numpy.sum(values)*100
             
            # print(values)
            print(dmgav)
            # print(effav)
             
            # self.aaa.clear()
            self.aaa.plot([dmgav, dmgav], [0,40],"-", color = self.color_cycle[self.color_number])
            self.aaa.plot(values, "-", color=self.color_cycle[self.color_number], label="Shooting")

            values_m = numpy.bincount(moral)
            values_m = values_m/numpy.sum(values_m)*100
            
            moralav = numpy.average(moral)
             
            self.aaa.plot([moralav, moralav], [0,40], "--", color=self.color_cycle[self.color_number])
            self.aaa.plot(values_m, "--", color=self.color_cycle[self.color_number], label="Avec moral")

            self.aaa.legend(loc=0)
            self.canvas.show()
            self.canvas.get_tk_widget().pack(expand= True)
             
            self.color_number += 1
            self.efficiency_table.add_Eff(self.color_number, effav)
            if self.color_number >= len(self.color_cycle):
                self.color_number = 0
        except ValueError as VE:
             
            print("FUCKK")
            tk.messagebox.showerror(message=str(VE))
             

if __name__ == '__main__':

    sim = SimUI()
    sim.root.mainloop()  