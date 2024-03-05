def contar_numeros():
    contador_menor0 = 0
    contador_maior0 = 0
    intervalo_inferior = -100
    intervalo_superior = 100

    for i in range(intervalo_inferior, intervalo_superior + 1, 1):
        if i > 0:
            contador_maior0 += 1
        elif i < 0:
            contador_menor0 += 1
    print ("de -100 até +100 tem exatamente ", contador_menor0,
            " números menores que zero e ", contador_maior0, " números maiores que zero")


def numero_pares_impares():
    contador_par = 0
    contador_impar = 0
    intervalo_inferior = 1
    intervalo_superior = 100
    for i in range(intervalo_inferior, intervalo_superior + 1, 1):
        if i % 2 == 0:
            contador_par += 1
        else:
            contador_impar += 1
    print("de 1 até 100 tem ", contador_par, " numeros pares e ", contador_impar, " numeros impares")


def numeros_primos():
    contador_n_primos = 0
    contador_primos = 0
    intervalo_inferior = 1
    intervalo_superior = 100
    for i in range(intervalo_inferior + 1, intervalo_superior + 1, 1):
        for j in range(1, i+1, 1):
            if (i % j) == 0 and (j != 1):
                contador_n_primos += 1
                break
            if i == (j+1):
                contador_primos += 1
                break
    print("de 1 até 100 tem exatamente ", contador_primos, " numeros primos")


def fibonacce():
    termo_1 = 1
    termo_2 = 1
    termo_soma = 1
    lista = [1,1]
    for i in range(0, 10 - 2, 1):
        termo_1 = termo_2
        termo_2 = termo_soma
        termo_soma = termo_1 + termo_2
        lista.append(termo_soma)
    print("a sequencia de fibonaci até o decimo termo é: ", lista)


def tabuada():
    valor = input("entre com um numero: ")
    print("A tabuada de multiplicação do numero ", valor, " até o decimo termo é:")
    for i in range(1, 11, 1):
        print(i, " x ", valor, " = ", (i * int(valor)))


contar_numeros()
numero_pares_impares()
numeros_primos()
fibonacce()
tabuada()
