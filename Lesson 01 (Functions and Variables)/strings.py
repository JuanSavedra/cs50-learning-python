# Entendendo I/O
name = input("What's your name? \n")
print("Your name is: " + name)
print("Hello,", name)
print("How are you doing today", name, sep=", ")

# Removendo espaços em branco da direita e da esquerda
name = name.strip()
print(f"Hello, {name}!")

# Deixando as primeiras letras maiúsculas
name = name.strip().title()
print(f"Hello, {name}!")

# Para um código melhor, poderíamos aplicar direto no input
formatted_name = input("What's your name? \n").strip().title()
print(f"Hello, {formatted_name}!")

# Pegando apenas o primeiro nome ou sobrenome
first_name, last_name = formatted_name.split(" ")
print(f"Hello, {first_name}!")
print(f"Hello, {last_name}!")

# Ou definindo com um array o primeiro ou outro elemento
first = formatted_name.split(" ")[0]
last = formatted_name.split(" ")[-1]

print(f"Hello, {first}!")
print(f"Hello, {last}!")
