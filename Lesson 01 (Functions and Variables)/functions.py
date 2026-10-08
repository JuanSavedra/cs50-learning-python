# Definindo qual nome vai ser usado nos parâmetros da função
def hello(to):
    print(f"Hello, {to}!")

name = input("Type your name: ")
hello(name)

# Usando mais de um argumento na função, sendo um deles padrão caso não tenha sido passado
def hello_more_arguments(to, from_="Me"):
    print(f"Hello, {to}! From {from_}.")

other_name = input("Type another name: ")
hello_more_arguments(other_name)  # Chamando a função com apenas um argumento, o outro usará o valor padrão