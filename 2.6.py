import tkinter as tk
from tkinter import ttk

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Конвертер валют")
        self.root.geometry("400x250")
        
        self.rates_to_usd = {
            'USD': 1.0,      
            'RUB': 77.69,    
            'EUR': 0.8495,   
            'CNY': 7.01      
        }
        
        self.create_widgets()
    
    def create_widgets(self):
        
        tk.Label(self.root, text="Конвертер валют", 
                font=("Arial", 16, "bold")).pack(pady=10)
        
        tk.Label(self.root, text="Сумма:", font=("Arial", 12)).pack()
        self.amount_entry = tk.Entry(self.root, font=("Arial", 12), width=15)
        self.amount_entry.pack(pady=5)
        self.amount_entry.insert(0, "1")
        
        currency_frame = tk.Frame(self.root)
        currency_frame.pack(pady=15)
        
        tk.Label(currency_frame, text="Из:", font=("Arial", 12)).grid(row=0, column=0, padx=5)
        self.from_currency = ttk.Combobox(currency_frame, 
                                         values=list(self.rates_to_usd.keys()), 
                                         font=("Arial", 12), 
                                         width=8, 
                                         state="readonly")
        self.from_currency.grid(row=0, column=1, padx=5)
        self.from_currency.set('USD')
        
        tk.Label(currency_frame, text="→", font=("Arial", 14)).grid(row=0, column=2, padx=10)
        
        tk.Label(currency_frame, text="В:", font=("Arial", 12)).grid(row=0, column=3, padx=5)
        self.to_currency = ttk.Combobox(currency_frame, 
                                       values=list(self.rates_to_usd.keys()), 
                                       font=("Arial", 12), 
                                       width=8, 
                                       state="readonly")
        self.to_currency.grid(row=0, column=4, padx=5)
        self.to_currency.set('RUB')
        
        tk.Button(self.root, text="Конвертировать", 
                 command=self.convert, 
                 font=("Arial", 12), 
                 bg="#4CAF50", 
                 fg="white", 
                 padx=20).pack(pady=15)
        
        self.result_label = tk.Label(self.root, text="", 
                                    font=("Arial", 14, "bold"), 
                                    fg="#2196F3")
        self.result_label.pack()
        
        info_frame = tk.Frame(self.root)
        info_frame.pack(pady=20)
        tk.Label(info_frame, text="Курсы к USD:", font=("Arial", 9)).pack()
        tk.Label(info_frame, text="1 USD = 77.69 RUB | 1 USD = 0.8495 EUR | 1 USD = 7.01 CNY", 
                font=("Arial", 9), fg="gray").pack()
    
    def convert(self):
        try:
            amount = float(self.amount_entry.get())
            from_curr = self.from_currency.get()
            to_curr = self.to_currency.get()
            
            amount_in_usd = amount / self.rates_to_usd[from_curr]
            
            result = amount_in_usd * self.rates_to_usd[to_curr]
            
            self.result_label.config(
                text=f"{amount} {from_curr} = {result:.2f} {to_curr}"
            )
            
        except ValueError:
            self.result_label.config(text="Ошибка: введите число!", fg="red")
        except:
            self.result_label.config(text="Ошибка конвертации!", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()