import tkinter as tk
import os
from tkmacosx import Button

#window configuration

window = tk.Tk()
window.title("To-Do List")
window.geometry("400x500")
window.configure(bg="#F9E8ED")


header = tk.Label(window, text="My To-Do List")
header.configure(bg="#F9E8ED", fg="#794B60", font=("Georgia", 25, "bold"))
header.pack(pady=10)

#assignment input
assignment_entry = tk.Entry(window, width=30)
assignment_entry.configure(bg="#FFF9FB", fg="#493840", font=("Georgia", 12), highlightthickness=0, borderwidth=0)
assignment_entry.pack(pady=10, padx=20, fill="x")

#add assignment
def add_assignment():
    assignment = assignment_entry.get().strip()
    if assignment:
        assignment_list.insert(tk.END, assignment)
        assignment_entry.delete(0, tk.END)
        save_assignments()

add_button = Button(window, text="Add Assignment", command = add_assignment, width=180)
add_button.configure(bg="#E5BDD0", fg="#493840", borderless=True, highlightthickness=0, highlightbackground="#F9E8ED")
add_button.pack(pady=5)

assignment_list = tk.Listbox(window, width=30, height=10)
assignment_list.configure(bg="#EACBD9", font=("Georgia", 12), highlightthickness=0, borderwidth=0)
assignment_list.pack(pady=10)

#delete assignment
def delete_assignment():
    selected = assignment_list.curselection()
    if selected:
        assignment_list.delete(selected[0])
        save_assignments()

delete_button = Button(window, text="Delete Assignment", command=delete_assignment, width=180)
delete_button.configure(bg="#E5BDD0", fg="#493840", borderless=True, highlightthickness=0, highlightbackground="#F9E8ED")
delete_button.pack(pady=5)

#complete assignment
def complete_assignment():
    selected = assignment_list.curselection()
    if selected:
        assignment = assignment_list.get(selected[0])
        if not assignment.startswith("Completed: "):
            assignment_list.delete(selected[0])
            assignment_list.insert(selected[0], "Completed: " + assignment)   
            save_assignments()

complete_button = Button(window, text="Mark as Complete", command=complete_assignment, width=180)
complete_button.configure(bg="#E5BDD0", fg="#493840", borderless=True, highlightthickness=0, highlightbackground="#F9E8ED")
complete_button.pack(pady=5)

def save_assignments():
    with open("assignment.txt", "w") as file:
        for item in assignment_list.get(0, tk.END):
            file.write(item + "\n")
        

#file handling
def load_assignments():
    if os.path.exists("assignment.txt"):
        with open("assignment.txt", "r") as file:
            for item in file:
                assignment_list.insert(tk.END, item.strip())
load_assignments()  
window.mainloop()