# Números inteiros (int)
# Calculando a soma de dois números, convertendo-os para int diretamente na função input()
x = int(input("Type the first number: "))
y = int(input("Type the second number: "))

print(x + y)

# Números de ponto flutuante (float)
# Calculando a soma de dois números, convertendo-os para float diretamente na função input()
a = float(input("Type the first number: "))
b = float(input("Type the second number: "))

y = round(a + b, 2)  # Arredondando o resultado para 2 casas decimais
z = a + b

print(y)
print(z)

print(f"{z:.2f}")  # Usando f-string para formatar o resultado com 2 casas decimais
print(f"{z:,}")  # Usando f-string para formatar o resultado com separador de milhar