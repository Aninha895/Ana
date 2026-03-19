# Lista vazia

Frutas = []

print(Frutas)



# Adicionando itens
Frutas.append("Banana")

Frutas.append("Laranja")

Frutas.append("Uva")

print(Frutas)


# Remover item
Frutas = ["Banana", "Laranja", "Uva"]
Frutas.remove("Banana")
print(Frutas)

# Leitura de quatro inteiros e criação da lista
lista = []
for i in range(4):
    numero = int(input(f"Digite o {i+1}° número:"))
    lista.append(numero)

# Mostrar tamanho antes
print("Tamanho antes:", len(lista))

# Ler o valor alvo
alvo = int(input("Digite o valor a remover:"))

# Verificar e remover se existir
if alvo in lista:
    lista.remove(alvo)

# Mostrar tamanho depois
print("Tamanho depois:", len(lista))    
      

