def Soma(n1, n2):
    return n1 + n2


def Subitracao(n1, n2):
    return n1 - n2


def Divisao(n1, n2):
    return n1 / n2


def Multiplicacao(n1, n2):
    return n1 * n2


x = float(input("digite o primeiro numero : "))
y = float(input("digite o segundo numero : "))


while True:
    operacao = int(input("1: Soma \n2: Subitracao \n3: Divisao \n4: Multiplicacao \n5: Saída: "))


    if operacao == 1:
        resultado = Soma(x, y)
        print("A soma dos dois valores é: ",resultado)


    elif operacao == 2:
        resultado = Sub(x, y)
        print("A subtração dos dois valores é: ", resultado)


    elif operacao == 3:
        resultado = Div(x, y)
        print("A divisão dos dois valores é: ", resultado)


    elif operacao == 4:
        resultado = Mult(x, y)
        print("A multiplicação dos dois valores é: ", resultado)


    elif operacao == 5:
        break