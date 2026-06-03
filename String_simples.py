
#Métodos úteis da cjasse string

nome = "LEina CaROlinE"

print(nome.upper())
print(nome.lower())
print(nome.title())



texto = "  Olá mundo !"

print(texto + ".")
print(texto.lstrip()+".")
print(texto.strip() + ".")
print(texto.rstrip() + ".\n\n")

menu = "Java"

print(menu.center(14))
print(menu.center(14, "#"))

print("-".join(menu))

print(
    """
    ============= Menu ==================
    
    1 - Depositar
    2 - Sacar
    3 - Sair
    
    
    ======================================
    
    
    """  
)

