def main():

    a = int(input("insira o ponto a: "))
    b = int(input("insira o ponto b: "))
    c = int(input("insira o ponto c: "))

    if (a > b + c):
        print(f"Os valores lidos de a,b e c sao {a}, {b} e {c}")
    else:
        soma = (a + b + c) / 2
        area = (soma*(soma-a)*(soma-b)*(soma-c)) ** 0.5

        print(f"sou um triangulo { area }")

main()
