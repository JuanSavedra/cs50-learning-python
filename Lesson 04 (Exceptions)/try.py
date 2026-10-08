# Estrutura de um try/except em Python

def main():
    number = get_int()
    print(f"You typed the number: {number}")

def get_int():
    while True: # Loop infinito que continuará pedindo ao usuário para digitar um número até que ele digite um número válido.
        try:
            # Código que pode gerar uma exceção
            number = int(input("Type a number: "))
        except ValueError: # Código que será executado caso ocorra uma exceção do tipo ValueError
            print("Invalid input. Please enter a valid integer.")
        else: # Código que será executado caso não ocorra nenhuma exceção
            break # Sai do loop caso o usuário digite um número válido

    return number

main()