def bin2dec(binario):
    # transforma binario em uma string
    binario = str(binario)
    # valor em decimal que sera a resposta
    decimal = 0
    # valor que vai multiplicar a ultima casa do binario
    multi = 1
    # tamanho do binario
    lenght = len(binario)
    # laço de repeticao
    for i in range(lenght):
        # ultimo numero do binario
        ultimo = int(binario[lenght - i - 1])
        # calcula o novo valor e soma no decimal
        soma = ultimo * multi
        print(
            f"Loop {i}: {decimal} + {soma}({ultimo} * {multi}) = {decimal + soma}")
        decimal = decimal + soma
        # calcula o novo valor para a proxima multiplicação
        multi = multi * 2
    # retornar o valor
    return decimal


def dec2bin(decimal):
    # valor em binario que sera a resposta
    binario = ""
    # valor que vai dividir a ultima casa do binario
    div = 1
    # laço de repeticao
    while div <= decimal:
        # calcula o novo valor para a proxima divisão
        div = div * 2
    # calcula o novo valor para a proxima divisão
    div = div // 2
    # laço de repeticao
    while div > 0:
        # calcula o novo valor para a proxima divisão
        if decimal >= div:
            binario = binario + "1"
            decimal = decimal - div
        else:
            binario = binario + "0"
        # calcula o novo valor para a proxima divisão
        div = div // 2
    # retornar o valor
    return binario


binario = int(input("Digite um valor: "))
decimal = bin2dec(binario)
print(f"O numero binario {binario} em decimal é {decimal}")
binario = dec2bin(decimal)
print(f"O numero decimal {decimal} em binario é {binario}")