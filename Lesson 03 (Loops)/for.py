# Define o "PARA" em Python
for i in [1, 2, 3]: # O colchete é usado para criar uma lista de elementos, que serão percorridos pelo loop.
    print(i)

# Define o range() em Python
for i in range(5): # O range() funciona como um "contador" que vai de 0 até o número passado como argumento, mas não inclui esse número.
    print(i)

# Define um array de itens em Python
items = ["apple", "banana", "cherry"]
for item in items: # O loop percorre cada elemento da lista "items" e imprime o valor de cada elemento.
    print(item)

# Pega a quantidade de elementos de uma lista em Python
students = ["Alice", "Bob", "Charlie"]
for i in range(len(students)): # O len() retorna a quantidade de elementos da lista "students", e o range() cria um contador que vai de 0 até a quantidade de elementos da lista, mas não inclui esse número.
    print(students[i]) # O loop percorre cada elemento da lista "students" e imprime o valor de cada elemento.

# Define um dicionário em Python e percorre suas chaves e valores
workers = {
    "Alice": 25,
    "Bob": 30,
    "Charlie": 35
}

for worker in workers: # O loop percorre cada chave do dicionário "workers" e imprime o valor de cada chave.
    print(worker, workers[worker], sep=", ") # O loop percorre cada chave do dicionário "workers" e imprime o valor de cada chave.

# Cria um array de dicionários em Python e percorre suas chaves e valores
students_harry_potter = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"}
]

for student in students_harry_potter:
    print(student["name"], student["house"], sep=", ")