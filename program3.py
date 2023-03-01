"""5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE: a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código; b) Evite usar funções prontas, como, por exemplo, reverse;"""

def main():
    strInput = input("Entre com a palavra: ")

    start, end = 0, len(strInput)-1

    while start < end:
        temp = strInput[end]
        strInput = strInput[:end] + strInput[start] + strInput[end+1:]
        strInput = strInput[:start] + temp + strInput[start+1:]
        start+=1
        end-=1

    print(f"A palavra invertida é: {strInput}")

if __name__ == "__main__":
    main()