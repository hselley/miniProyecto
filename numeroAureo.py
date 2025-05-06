'''
Sucesión de Fibonacci versión lista
La función recibe como argumento la cantidad de cifras de la serie

El cálculo del número aureo está dado por:
\varphi = lim_{n\rightarrow \infty} = \dfrac{Fib(n+1)}{n}
'''

def Fib(n=10):
    lista = [0, 1]
    for _ in range(n):
        lista.append(lista[-1] + lista[-2])
    return lista

# print(Fib(5000))

# Se calcula la aproximación al número aureo
n=10000
sucesion = Fib(n)
print(sucesion[-1]/sucesion[-2])
