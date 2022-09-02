"""
algoritimo que recebe uma lista de valores e retorna
a soma e a média
autor : Luca daniel tavare maximo
data: 02/09/2022 10:13
"""
#Definião da função
def soma(numeros):
    soma = sum(numeros)
    print(f'\nA soma é {soma}')



#Função da média
def media(valores):
    avg = sum(valores) / len(valores)
    print(f'\nA média é {avg}')



#Criação da lista
lista=[]

for a in range(5):
    lista.append(int(input('Entre com um número: ')))
soma(lista)
media(lista)
