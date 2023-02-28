import tkinter as tk

root = tk.Tk()
root.geometry("436x436")
label = tk.Label(root, text="AKTUELLE MÅLINGER")
label.grid(columnspan=4)

text = tk.Text(root, height=20, width=30)
text.grid(row=4,column=2)
text.insert(tk.END, "SpO2")
text = tk.Text(root, height=4, width=30)
text.grid(row=5,column=2)
text.insert(tk.END, "grænseværdier")

text = tk.Text(root, height=20, width=30)
text.grid(row=4,column=3)
text.insert(tk.END, "HR")
text = tk.Text(root, height=4, width=30)
text.grid(row=5,column=3)
text.insert(tk.END, "grænseværdier")

def handle_button_click():
    new_window = tk.Toplevel(root)
    new_window.geometry("436x436")
    new_window.title("Sæt Grænseværdier SpO2")
    label = tk.Label(new_window, text="This is a new window")
    label.pack()

button = tk.Button(root, text="Ændre Grænseværdier SpO2", command=handle_button_click)
button.grid(row=6, column=2)

button = tk.Button(root, text="Ændre Grænseværdier HR", command=handle_button_click)
button.grid(row=6, column=3)

button = tk.Button(root, text="Tidligere Målinger", command=handle_button_click)
button.grid(columnspan=4,sticky=tk.N)

button = tk.Button(root, text="Statistik", command=handle_button_click)
button.grid(columnspan=4, sticky=tk.S)



root.mainloop()