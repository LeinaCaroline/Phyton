texto = input("Digite um texto ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:   
        print(letra, end="\n")
   
print()
        
print(list(range(4)))

carros = ["gol", "celta", "palio"]

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro} \n")