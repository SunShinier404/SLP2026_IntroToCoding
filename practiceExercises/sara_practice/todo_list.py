import tkinter as tk
import os

window = tk.Tk()
window.title("To-Do List")
window.geometry("400x500")


header = tk.Label(window, text="My To-Do List")
header.pack(pady=10)

assignment_entry = tk.Entry(window, width=30)
assignment_entry.pack(pady=10)

def add_assignment():
    assignment = assignment_entry.get().strip()
    if assignment:
        assignment_list.insert(tk.END, assignment)
        assignment_entry.delete(0, tk.END)
        save_assignments()

add_button = tk.Button(window, text="Add Assignment", command = add_assignment)
add_button.pack(pady=5)

assignment_list = tk.Listbox(window, width=40, height=10)
assignment_list.pack(pady=10)


def delete_assignment():
    selected = assignment_list.curselection()
    if selected:
        assignment_list.delete(selected[0])
        save_assignments()

delete_button = tk.Button(window, text="Delete Assignment", command=delete_assignment)
delete_button.pack(pady=5)

def complete_assignment():
    selected = assignment_list.curselection()
    if selected:
        assignment = assignment_list.get(selected[0])
        if not assignment.startswith("Completed:"):
            assignment_list.delete(selected[0])
            assignment_list.insert(selected[0], "Completed: " + assignment)   
            save_assignments()

complete_button = tk.Button(window, text="Mark as Complete", command=complete_assignment)
complete_button.pack(pady=5)

def save_assignments():
    with open("assignment.txt", "w") as file:
        for item in assignment_list.get(0, tk.END):
            file.write(item + "\n")
        

def load_assignments():
    if os.path.exists("assignment.txt"):
        with open("assignment.txt", "r") as file:
            for item in file:
                assignment_list.insert(tk.END, item.strip())
load_assignments()  
window.mainloop()