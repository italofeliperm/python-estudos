decimal = int(input("Digite um número decimal: ")) # recebe um número decimal do usuário

binario = "" # inicializa a variável binario como uma string vazia

while decimal > 0: # enquanto o decimal for maior que zero
    resto = decimal % 2 # calcula o resto da divisão por 2
    binario = str(resto) + binario # adiciona o resto na frente do número binário
    decimal //= 2 # divide o decimal por 2 (divisão inteira

print(f"O número {decimal} em binário é {binario}")