def main():

    numero = int(input('Numero a verificar: '))
    contadorPrimo = 0

    for i in range(1, 100):        
        if numero % i == 0:
            contadorPrimo += 1
            
    if contadorPrimo  == 2 :
        print('o numero é primo')
    else:
        print('o numero nao é primo')

main()
