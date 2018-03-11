import tkinter as tk

from DiceSim2 import Defense


class DefenseUI(tk.Frame):

    def __init__(self, root):

        width_text = 10
        tk.Frame.__init__(self, root)

        self.fnp_list = []

        self.tough_text = tk.StringVar()
        self.tough_text.set("T")
        self.tough_label = tk.Label(self, textvariable=self.tough_text, width=width_text)
        self.tough_label.grid(row=0, column=0)

        self.wounds_text = tk.StringVar()
        self.wounds_text.set("W")
        self.wounds_label = tk.Label(self, textvariable=self.wounds_text, width=width_text)
        self.wounds_label.grid(row=1, column=0)

        self.save_text = tk.StringVar()
        self.save_text.set("Sv")
        self.save_label = tk.Label(self, textvariable=self.save_text, width=width_text)
        self.save_label.grid(row=2, column=0)

        self.isave_text = tk.StringVar()
        self.isave_text.set("ISv")
        self.isave_label = tk.Label(self, textvariable=self.isave_text, width=width_text)
        self.isave_label.grid(row=3, column=0)

        self.hit_mod_text = tk.StringVar()
        self.hit_mod_text.set("Hit_Mod")
        self.hit_mod_label = tk.Label(self, textvariable=self.hit_mod_text, width=width_text)
        self.hit_mod_label.grid(row=4, column=0)

        self.wnd_mod_text = tk.StringVar()
        self.wnd_mod_text.set("Wnd Mod")
        self.wnd_mod_label = tk.Label(self, textvariable=self.wnd_mod_text, width=width_text)
        self.wnd_mod_label.grid(row=5, column=0)

        self.save_mod_text = tk.StringVar()
        self.save_mod_text.set("Save Mod")
        self.save_mod_label = tk.Label(self, textvariable=self.save_mod_text, width=width_text)
        self.save_mod_label.grid(row=6, column=0)

        self.moral_text = tk.StringVar()
        self.moral_text.set("Moral")
        self.moral_label = tk.Label(self, textvariable=self.moral_text, width=width_text)
        self.moral_label.grid(row=7, column=0)

        self.moral_rule_text = tk.StringVar()
        self.moral_rule_text.set("Moral Rule")
        self.moral_rule_label = tk.Label(self, textvariable=self.moral_rule_text, width=width_text)
        self.moral_rule_label.grid(row=8, column=0)

        self.points_text = tk.StringVar()
        self.points_text.set("Points")
        self.points_label = tk.Label(self, textvariable=self.points_text, width=width_text)
        self.points_label.grid(row=9, column=0)

        self.max_model_text = tk.StringVar()
        self.max_model_text.set("Unit size")
        self.max_model_label = tk.Label(self, textvariable=self.max_model_text, width=width_text)
        self.max_model_label.grid(row=10, column=0)

        self.fnp_text = tk.StringVar()
        self.fnp_text.set("FnP")
        self.fnp_label = tk.Label(self, textvariable=self.fnp_text, width=width_text)
        self.fnp_label.grid(row=11, column=0)

        width_text = 8

        self.tough_entry_text = tk.StringVar()
        self.tough_entry_text.set("4")
        self.tough_entry = tk.Entry(self, textvariable=self.tough_entry_text, width=width_text)
        self.tough_entry.grid(row=0, column=1)

        self.wounds_entry_text = tk.StringVar()
        self.wounds_entry_text.set("1")
        self.wounds_entry = tk.Entry(self, textvariable=self.wounds_entry_text, width=width_text)
        self.wounds_entry.grid(row=1, column=1)

        self.save_entry_text = tk.StringVar()
        self.save_entry_text.set("3+")
        self.save_entry = tk.Entry(self, textvariable=self.save_entry_text, width=width_text)
        self.save_entry.grid(row=2, column=1)

        self.isave_entry_text = tk.StringVar()
        self.isave_entry_text.set("--")
        self.isave_entry = tk.Entry(self, textvariable=self.isave_entry_text, width=width_text)
        self.isave_entry.grid(row=3, column=1)

        self.hit_mod_entry_text = tk.StringVar()
        self.hit_mod_entry_text.set("+0")
        self.hit_mod_entry = tk.Entry(self, textvariable=self.hit_mod_entry_text, width=width_text)
        self.hit_mod_entry.grid(row=4, column=1)

        self.wnd_mod_entry_text = tk.StringVar()
        self.wnd_mod_entry_text.set("+0")
        self.wnd_mod_entry = tk.Entry(self, textvariable=self.wnd_mod_entry_text, width=width_text)
        self.wnd_mod_entry.grid(row=5, column=1)

        self.save_mod_entry_text = tk.StringVar()
        self.save_mod_entry_text.set("+0")
        self.save_mod_entry = tk.Entry(self, textvariable=self.save_mod_entry_text, width=width_text)
        self.save_mod_entry.grid(row=6, column=1)

        self.moral_entry_text = tk.StringVar()
        self.moral_entry_text.set("7")
        self.moral_entry = tk.Entry(self, textvariable=self.moral_entry_text, width=width_text)
        self.moral_entry.grid(row=7, column=1)

        self.moral_rule_entry = tk.Listbox(self, exportselection=False)
        self.moral_rule_entry.config(height=6, width=width_text)
        for item in ["NONE", "CAN", "MUST", "COMMI", "KNIFE", "AUTO"]:
            self.moral_rule_entry.insert(tk.END, item)

        self.moral_rule_entry.grid(row=8, column=1)
        self.moral_rule_entry.selection_set(0, last=None)

        self.points_entry_text = tk.StringVar()
        self.points_entry_text.set("14")
        self.points_entry = tk.Entry(self, textvariable=self.points_entry_text, width=width_text)
        self.points_entry.grid(row=9, column=1)

        self.max_model_entry_text = tk.StringVar()
        self.max_model_entry_text.set("10")
        self.max_model_entry = tk.Entry(self, textvariable=self.max_model_entry_text, width=width_text)
        self.max_model_entry.grid(row=10, column=1)

        self.fnp_frame = tk.Frame(self)
        self.fnp_frame.grid(row=11, column=1)

    def add_fnp(self):

        fnp_entry_text = tk.StringVar()
        fnp_entry_text.set("5+")

        fnp_entry = tk.Entry(self.fnp_frame, textvariable=fnp_entry_text, width=6)
        fnp_entry.grid(row=len(self.fnp_list), column=0)

        self.fnp_list.append(fnp_entry)

    def remove_fnp(self):

        if len(self.fnp_list) > 0:
            self.fnp_list.pop().destroy()

    def gather_input(self):
        try:
            t = clean_input(self.tough_entry.get())
            w = clean_input(self.wounds_entry.get())

            sv = clean_input(self.save_entry.get())

            isv = clean_isv(self.isave_entry.get())

            hm = clean_input(self.hit_mod_entry.get())
            wm = clean_input(self.wnd_mod_entry.get())
            sm = clean_input(self.save_mod_entry.get())
            moral = clean_input(self.moral_entry.get())
            pts = clean_input(self.points_entry.get())
            fnp_input = []

            moral_rule_selection = self.moral_rule_entry.curselection()
            if moral_rule_selection:
                moral_rule = self.moral_rule_entry.get(moral_rule_selection)
            else:
                moral_rule = "NONE"
            for fnp in self.fnp_list:
                next_fnp = clean_input(fnp.get())
                fnp_input.append(next_fnp)

            us = clean_input(self.max_model_entry.get())

            defender = Defense.Defense(t, w, sv, isv, fnp_input, moral, pts)
            defender.moral_rule = moral_rule
            defender.unit_size = us

        except ValueError as Ve:

            raise Ve

        return defender


def clean_input(input_string):

    input_string = input_string.strip("+")
    if input_string.isnumeric():
        retour = int(input_string)
    else:
        raise ValueError("Valeur doit être numerique")
    return retour


def clean_isv(input_string):
    """

    Parameters
    ----------
    input_string

    Returns
    -------

    """

    input_string = input_string.strip("+")
    if input_string.isnumeric():
        return int(input_string)
    else:
        return None
