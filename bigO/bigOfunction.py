def o1(numero) :
    print(numero)

o1(5)

def on(numero):
    i = 1
    while i <= numero:
        print(i)
        i += 1

on(10)

def onsquared(numero):
    i = 1
    j = 1
    while i <= numero:
        linha = ''
        while j <= numero:
            linha += ' ' + str(j)
            print(linha)
            j += 1
        i += 1
onsquared(10)