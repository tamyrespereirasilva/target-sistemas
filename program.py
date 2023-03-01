"""2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência."""

def main():
    intInput = int(input("Entre com numero:"))

    num0, num1, num2 = 0, 1, 1
    
    if intInput in set([num0, num1, num2]):
        print("Pertence a sequencia")

    while num0 < intInput:
        num0 = num1 + num2
        num2 = num1
        num1 = num0

    if num0 == intInput:
        print("Pertence a sequencia")
    else:
        print("Não Pertence a sequencia")


if __name__ == "__main__":
    main()