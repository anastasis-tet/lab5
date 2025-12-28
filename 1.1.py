import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Привет")

tk.Button(root, text="Привет", 
          command=lambda: messagebox.showinfo("", "Привет!")).pack(pady=50)

root.mainloop()