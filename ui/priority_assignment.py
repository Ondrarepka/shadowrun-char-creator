import tkinter as tk

window = tk.Tk()
window.title("Shadowrun Character Creator")

# priority costs
priority_costs = {
    "A":4,
    "B":3,
    "C":2,
    "D":1,
    "E":0
}
max_cost = 10

def update_total(*args):
    print("Current selections:")
    print("Metatype:", metatype_var.get())
    print("Attributes:", attributes_var.get())
    print("Magic:", magic_var.get())
    print("Skill:", skill_var.get())
    print("Resources:", resources_var.get())
    total_cost = priority_costs[metatype_var.get()] + priority_costs[attributes_var.get()] + priority_costs[magic_var.get()] + priority_costs[skill_var.get()] + priority_costs[resources_var.get()]
    total_label.config(text=f"Total: {total_cost}/{max_cost}")
    if total_cost == max_cost:
        continue_button.config(state='normal')
    else:
        continue_button.config(state='disabled')


# priority values
priority_options = ["A", "B", "C", "D", "E"]
metatype_var = tk.StringVar()
metatype_var.set("C")
metatype_var.trace_add('write', update_total)
attributes_var = tk.StringVar()
attributes_var.set("C")
attributes_var.trace_add('write', update_total)
magic_var = tk.StringVar()
magic_var.set("C")
magic_var.trace_add('write', update_total)
skill_var = tk.StringVar()
skill_var.set("C")
skill_var.trace_add('write', update_total)
resources_var = tk.StringVar()
resources_var.set("C")
resources_var.trace_add('write', update_total)

#Table for the prio select
prio_table = tk.Frame(window, bd=2, relief='groove', padx=10, pady=10)
prio_table.grid(column=0, row=0, padx=10, pady=10, columnspan=2)

# Info box for the priorities on the right
desc_frame = tk.Frame(window, bd=2, relief='groove', padx=10, pady=10)
desc_frame.grid(column=1, row=0, padx=10, pady=10, columnspan=2)

#labels
category_label = tk.Label(prio_table, text="Category")
priority_label = tk.Label(prio_table, text="Priority")
metatype_label = tk.Label(prio_table, text="Metatype")
attributes_label = tk.Label(prio_table, text="Attributes")
magic_label = tk.Label(prio_table, text="Magic")
skill_label = tk.Label(prio_table, text="Skill")
resources_label = tk.Label(prio_table, text="Resources")

# Total down
total_label = tk.Label(window, text="Total: X/10")

# Dropdowns
metatype_dropdown = tk.OptionMenu(prio_table, metatype_var, *priority_options)
attributes_dropdown = tk.OptionMenu(prio_table, attributes_var, *priority_options)
magic_dropdown = tk.OptionMenu(prio_table, magic_var, *priority_options)
skill_dropdown = tk.OptionMenu(prio_table, skill_var, *priority_options)
resources_dropdown = tk.OptionMenu(prio_table, resources_var, *priority_options)

#Buttons down
continue_button = tk.Button(window, text="Continue")
continue_button.config(state='disabled')
validate_button = tk.Button(window, text="Validate")

# GRID
# Header
category_label.grid(column=0, row=0)
priority_label.grid(column=1, row=0) 

# labels on left
metatype_label.grid(column=0, row=1) 
attributes_label.grid(column=0, row=2) 
magic_label.grid(column=0, row=3) 
skill_label.grid(column=0, row=4) 
resources_label.grid(column=0, row=5)
#dropdown A - E
metatype_dropdown.grid(column=1, row=1) 
attributes_dropdown.grid(column=1, row=2) 
magic_dropdown.grid(column=1, row=3) 
skill_dropdown.grid(column=1, row=4) 
resources_dropdown.grid(column=1, row=5)

# total label + buttons
total_label.grid(column=0, row=6, columnspan=2)
continue_button.grid(column=0, row=7, columnspan=2)


window.mainloop()