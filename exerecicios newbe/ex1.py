##Escreva um programa Python que imprima "Hello, World!" na tela.
print ("hello world")
##Escreva um programa Python que leia dois números e exiba sua soma.

n1 = 2
n2 = 3
print(n1+n2)


##Escreva um programa Python que leia um número inteiro e exiba se ele é par ou ímpar.
n1 = 17
answers = n1 % 2
if answers == 0:
    print ("even")
else: 
    print ("odd")
print(answers)

##Escreva um programa Python que leia uma string e exiba quantas vezes cada letra aparece na string.

text = "hello world"
index = 0
for i in text:
    if i == "o":
        index += 1
print (index)


##Escreva um programa Python que leia uma string e exiba quantas vezes cada letra aparece na string 2.

string = "Escrevendo alguma coisa para testar o codigo e verificar"

freq = {}

for letra in string:
    if letra in freq:
        freq[letra] += 1
    else:
        freq[letra] = 1

print("Frequência das letras na string:")
for letra, count in freq.items():
    print(f"{letra}: {count}")
    

##Escreva um programa Python que leia uma lista de números e exiba a média dos números.

listofnumbers = [2, 6, 9, 10, 12,1]
somadosnumeros = 0
for i in listofnumbers:
    somadosnumeros += i
media = somadosnumeros/len(listofnumbers)
print(media)





