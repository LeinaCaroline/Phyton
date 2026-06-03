import tkinter as tk
from tkinter import messagebox

#este programa ainda não rodou direito

def somar_numeros():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    resultado = num1+num2
    messagebox.showinfo("Resultado", f"A soma dos numeros é: {resultado}")
    
    #criando a janela
    janela = tk.Tk()
    janela.tittle("Calculadora de Soma")
    
    #criando os widgets
    label_num1 = tk.Label(janela, text="Numero 1: ")
    label_num1.grid(row=0, column=0, padx=10, pady=5, sticky="e")
    
    entry_num1=tk.Entry(janela)
    entry_num1.grid(row=0, column=0, padx=10, pady=5)
    
    label_num2=tk.Label(janela, text="Numero 2: ")
    label_num2.grid(row=0, column= 0, padx= 10, pady=5, sticky="e")
    
    entry_num2= tk.Entry(janela)
    entry_num2.grid(row=0, column=0, padx=10, pady=5)
    
    botao_somar= tk.Button(janela, text="Somar", command=somar_numeros)
    botao_somar.grid(row=2, columnspan=2, padx=10, pady=5)
    
    janela.mainloop()