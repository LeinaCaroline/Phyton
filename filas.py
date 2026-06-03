
from collections import deque

fila = deque(["Leina","Carlos","Joana","Paulo","Catarina"])

fila.append("cliente1")
fila.append("cliente2")
fila.append("cliente3")

while fila:#  A fila existir
    pessoa = fila.popleft()
    print(f"Saiu da fila: {pessoa}")
    
    
'''
from collections import deque  

fila = deque(["Leina", "Carlos", "Maria", "João"])

for i in range(len(fila)):  # len original da fila
    pessoa = fila.popleft()  # sempre tira o primeiro
    print(f"Posição {i}: {pessoa}")
'''