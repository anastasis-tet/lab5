import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Котик и Пёсик")


notebook = ttk.Notebook(root)
notebook.pack()


tab1 = tk.Frame(notebook)
img1 = Image.open("cat.jpg").resize((400, 250))
photo1 = ImageTk.PhotoImage(img1)
tk.Label(tab1, image=photo1).pack()
tk.Label(tab1, text="Котик").pack()
notebook.add(tab1, text="Котик")


tab2 = tk.Frame(notebook)
img2 = Image.open("dog.jpg").resize((250, 350))
photo2 = ImageTk.PhotoImage(img2)
tk.Label(tab2, image=photo2).pack()
tk.Label(tab2, text="Пёсик").pack()
notebook.add(tab2, text="Пёсик")

root.mainloop()