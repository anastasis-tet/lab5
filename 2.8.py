import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class GuessAnimalGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Угадай животное")
        self.root.geometry("400x300")
        
        self.secret_animal = "котик"
        self.hints = [
            "Это животное домашнее",
            "Оно любит спать",
            "Говорит 'Мяу'",
            "Ловит мышей",
            "Любит молоко"
        ]
        self.current_hint = 0
        
        self.cat_image = ImageTk.PhotoImage(Image.open("cat2.jpg").resize((150, 150)))
        self.wrong_image = ImageTk.PhotoImage(Image.open("cat3.jpg").resize((150, 150)))
        
        self.show_main_screen()
    
    def show_main_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Label(self.root, text='Игра "Угадай животное"', 
                font=("Arial", 18, "bold"), fg="blue").pack(pady=30)
        
        tk.Label(self.root, text="Попробуй угадать, какое животное загадано!", 
                font=("Arial", 12)).pack(pady=10)
        
        tk.Button(self.root, text="Начать игру", command=self.show_game_screen,
                 font=("Arial", 14), bg="green", fg="white", 
                 width=15, height=2).pack(pady=30)
        
        tk.Button(self.root, text="Выйти", command=self.root.quit,
                 font=("Arial", 10), width=10).pack()
    
    def show_game_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Label(self.root, text=f"Подсказка {self.current_hint + 1}:", 
                font=("Arial", 12, "bold")).pack(pady=10)
        
        tk.Label(self.root, text=self.hints[self.current_hint], 
                font=("Arial", 14), fg="darkblue").pack(pady=10)
        
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=30)
        
        tk.Button(btn_frame, text="Я знаю ответ!", command=self.show_answer_screen,
                 font=("Arial", 12), bg="orange", fg="black",
                 width=15, height=2).pack(side="left", padx=10)
        
        if self.current_hint < len(self.hints) - 1:
            tk.Button(btn_frame, text="Ещё подсказка", command=self.next_hint,
                     font=("Arial", 12), bg="lightblue",
                     width=15, height=2).pack(side="left", padx=10)
        else:
            tk.Label(btn_frame, text="Подсказки кончились!", 
                    font=("Arial", 10), fg="red").pack(side="left", padx=10)
        
        tk.Button(self.root, text="Назад в меню", command=self.back_to_menu,
                 font=("Arial", 10)).pack(pady=10)
    
    def next_hint(self):
        self.current_hint += 1
        self.show_game_screen()
    
    def back_to_menu(self):
        self.current_hint = 0
        self.show_main_screen()
    
    def show_answer_screen(self):
        answer_window = tk.Toplevel(self.root)
        answer_window.title("Выбери ответ")
        answer_window.geometry("350x300")
        
        tk.Label(answer_window, text="Кто это?", font=("Arial", 16, "bold")).pack(pady=20)
        
        animals = ["котик", "собачка", "жираф", "хомяк", "попугай"]
        
        for animal in animals:
            tk.Button(answer_window, text=animal, 
                     command=lambda a=animal: self.check_answer(a, answer_window),
                     font=("Arial", 12), width=15).pack(pady=5)
        
        tk.Button(answer_window, text="Отмена", 
                 command=answer_window.destroy).pack(pady=10)
    
    def check_answer(self, guess, window):
        window.destroy()
        
        result_window = tk.Toplevel(self.root)
        result_window.title("Результат")
        result_window.geometry("350x400")
        
        if guess == self.secret_animal:
            tk.Label(result_window, text="ПРАВИЛЬНО!", 
                    font=("Arial", 16, "bold"), fg="green").pack(pady=10)
            tk.Label(result_window, text=f"Да, это {self.secret_animal}!", 
                    font=("Arial", 14)).pack(pady=5)
            
            tk.Label(result_window, image=self.cat_image).pack(pady=10)
            
        else:
            tk.Label(result_window, text="НЕПРАВИЛЬНО!", 
                    font=("Arial", 16, "bold"), fg="red").pack(pady=10)
            tk.Label(result_window, text=f"Это был {self.secret_animal}, а не {guess}!", 
                    font=("Arial", 14)).pack(pady=5)
            
            tk.Label(result_window, image=self.wrong_image).pack(pady=10)
        
        btn_frame = tk.Frame(result_window)
        btn_frame.pack(pady=20)
        
        tk.Button(btn_frame, text="Играть снова", 
                 command=lambda: self.restart_game(result_window)).pack(side="left", padx=10)
        tk.Button(btn_frame, text="Закрыть", 
                 command=result_window.destroy).pack(side="left", padx=10)
    
    def restart_game(self, window):
        window.destroy()
        self.current_hint = 0
        self.show_main_screen()
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = GuessAnimalGame()
    game.run()