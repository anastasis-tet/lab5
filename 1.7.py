import tkinter as tk

def exit_app():
    root.quit()

root = tk.Tk()
root.title("Меню с выходом")

menubar = tk.Menu(root)
root.config(menu=menubar)

# Меню File
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=exit_app)

# Текст на окне
label = tk.Label(root, text="Выберите File -> Exit для выхода")
label.pack(pady=50)

root.geometry("300x200")
root.mainloop()