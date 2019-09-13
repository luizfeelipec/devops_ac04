def ehprimo(num):
    '''
    Função que retorna True se um número é primo.
    E False caso o contrário.
    '''
    for i in range(2, num//2):
        if num % i == 0:
            return False
    return True


def listaprimos2(num):
    primos = []
    for i in range(2, num):
        if ehprimo(i):
            primos.append(i)
    return primos


def listaprimos(num):
    '''
    Função que lista os números primos menores que num.
    '''
    primos = []
    for i in range(2, num):
        primo = True
        for j in range(2, i):
            if i % j == 0:
                primo = False
        if primo:
            primos.append(i)
    return primos


if __name__ == '__main__':
    print(listaprimos(150))
