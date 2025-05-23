import tkinter as tk

class PriorityAssigmentUI:
    def __init__(self, parent):
        self.frame = tk.Frame(parent)
        self.frame.grid(column=0, row=0, padx=10, pady=10)
        # priority values
        self.priority_options = ["A", "B", "C", "D", "E"]
        self.metatype_var = tk.StringVar()
        self.metatype_var.set("C")
        self.metatype_var.trace_add('write', self.update_total)
        self.attributes_var = tk.StringVar()
        self.attributes_var.set("C")
        self.attributes_var.trace_add('write', self.update_total)
        self.magic_var = tk.StringVar()
        self.magic_var.set("C")
        self.magic_var.trace_add('write', self.update_total)
        self.skill_var = tk.StringVar()
        self.skill_var.set("C")
        self.skill_var.trace_add('write', self.update_total)
        self.resources_var = tk.StringVar()
        self.resources_var.set("C")
        self.resources_var.trace_add('write', self.update_total)

        #Table for the prio select
        self.prio_table = tk.Frame(self.frame, bd=2, relief='groove', padx=10, pady=10)
        self.prio_table.grid(column=0, row=0, padx=10, pady=10, columnspan=2)

        # Info box for the priorities on the right
        self.desc_frame = tk.Frame(self.frame, bd=2, relief='groove', padx=10, pady=10)
        self.desc_frame.grid(column=1, row=0, padx=10, pady=10, columnspan=2)

        #labels
        self.category_label = tk.Label(self.prio_table, text="Category")
        self.priority_label = tk.Label(self.prio_table, text="Priority")
        self.metatype_label = tk.Label(self.prio_table, text="Metatype")
        self.attributes_label = tk.Label(self.prio_table, text="Attributes")
        self.magic_label = tk.Label(self.prio_table, text="Magic")
        self.skill_label = tk.Label(self.prio_table, text="Skill")
        self.resources_label = tk.Label(self.prio_table, text="Resources")

        # Total down
        self.total_label = tk.Label(self.frame, text="Total: X/10")

        # Dropdowns
        self.metatype_dropdown = tk.OptionMenu(self.prio_table, self.metatype_var, *self.priority_options)
        self.attributes_dropdown = tk.OptionMenu(self.prio_table, self.attributes_var, *self.priority_options)
        self.magic_dropdown = tk.OptionMenu(self.prio_table, self.magic_var, *self.priority_options)
        self.skill_dropdown = tk.OptionMenu(self.prio_table, self.skill_var, *self.priority_options)
        self.resources_dropdown = tk.OptionMenu(self.prio_table, self.resources_var, *self.priority_options)

        #Buttons down
        self.continue_button = tk.Button(self.frame, text="Continue")
        self.continue_button.config(state='disabled')
        self.validate_button = tk.Button(self.frame, text="Validate")

        # GRID
        # Header
        self.category_label.grid(column=0, row=0)
        self.priority_label.grid(column=1, row=0) 

        # labels on left
        self.metatype_label.grid(column=0, row=1) 
        self.attributes_label.grid(column=0, row=2) 
        self.magic_label.grid(column=0, row=3) 
        self.skill_label.grid(column=0, row=4) 
        self.resources_label.grid(column=0, row=5)
        #dropdown A - E
        self.metatype_dropdown.grid(column=1, row=1) 
        self.attributes_dropdown.grid(column=1, row=2) 
        self.magic_dropdown.grid(column=1, row=3) 
        self.skill_dropdown.grid(column=1, row=4) 
        self.resources_dropdown.grid(column=1, row=5)

        # total label + buttons
        self.total_label.grid(column=0, row=6, columnspan=2)
        self.continue_button.grid(column=0, row=7, columnspan=2)

        # priority costs
        self.priority_costs = {
            "A":4,
            "B":3,
            "C":2,
            "D":1,
            "E":0
        }
        self.max_cost = 10


    def update_total(self,*args):
        print("Current selections:")
        print("Metatype:", self.metatype_var.get())
        print("Attributes:", self.attributes_var.get())
        print("Magic:", self.magic_var.get())
        print("Skill:", self.skill_var.get())
        print("Resources:", self.resources_var.get())
        self.total_cost = self.priority_costs[self.metatype_var.get()] + self.priority_costs[self.attributes_var.get()] + self.priority_costs[self.magic_var.get()] + self.priority_costs[self.skill_var.get()] + self.priority_costs[self.resources_var.get()]
        self.total_label.config(text=f"Total: {self.total_cost}/{self.max_cost}")
        if self.total_cost == self.max_cost:
            self.continue_button.config(state='normal')
        else:
            self.continue_button.config(state='disabled')


    

window = tk.Tk()
window.title("Shadowrun Character Creator")
priority_ui = PriorityAssigmentUI(window)
window.mainloop()