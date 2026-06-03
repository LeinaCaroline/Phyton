import tkinter as tk

def capturar_clic(event):
    x = event.x
    y = event.y
    label_coordenadas["text"] = f"Ultimo clique X= {x}, Y= {y}"
    
    #Criando as janelas
janela = tk.Tk()
janela.title("Tratamento de eventos - Captura de Clique Esquerdo")
    
    #Criando o widget do rótulo
label_coordenadas = tk.Label(janela, text = "Clique em qualquer lugar da janela")
label_coordenadas.pack(padx=200, pady=100)
    
    #Ligando o evento do clique do mouse à função
janela.bind("<Button-3>", capturar_clic)
    
    #Rodando o loop principal
janela.mainloop()