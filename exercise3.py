def main():

    numero1 = int(input("insira o nuemro 1: "))
    numero2 = int(input("insira o nuemro 2: "))
    numero3 = int(input("insira o nuemro 3: "))

    numeros = [numero1, numero2, numero3]

    numeros.sort()

    print(f"o menor numero é {numeros[0]}")

main()
