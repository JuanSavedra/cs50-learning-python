# Estrutura de um try/except em Python

def main():
    number = get_int()
    print(f"You typed the number: {number}")

def get_int():
    while True: # Loop infinito que continuará pedindo ao usuário para digitar um número até que ele digite um número válido.
        try:
            # Código que pode gerar uma exceção
            return int(input("Type a number: "))
        except ValueError: # Código que será executado caso ocorra uma exceção do tipo ValueError
            print("Invalid input. Please enter a valid integer.")
            pass # Continua o loop caso ocorra uma exceção do tipo ValueError

main()