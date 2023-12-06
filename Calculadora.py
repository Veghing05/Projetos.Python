import tkinter as tk
from tkinter import ttk

def press(key):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(key))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Erro")

# Criar a janela principal
window = tk.Tk()
window.title("Calculadora")

# Adicionar uma entrada para a expressão
entry = tk.Entry(window, width=20, font=('Arial', 16), borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Definir os botões
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Adicionar os botões à interface gráfica
row_val = 1
col_val = 0
for button in buttons:
    ttk.Button(window, text=button, style='TButton', command=lambda key=button: press(key) if key != '=' else calculate()).grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Botão para limpar a entrada
ttk.Button(window, text='C', style='TButton', command=clear).grid(row=row_val, column=col_val, padx=5, pady=5)

# Configurar o estilo dos botões
style = ttk.Style()
style.configure('TButton', font=('Arial', 14), padding=5)

# Iniciar o loop da interface gráfica
window.mainloop()

