valores = [1,4,5,6,9,13,19,21]
lista = list(filter(lambda x:x%2!=0,valores))
print(lista)


lista = [  numero**2 for numero in range(1,6)]
print(lista)


lista =list(map(lambda x : x**2, range(1,6)))
print(lista)

from functools import reduce
valores = [2,2,2,2,2]
sumatoria =reduce(lambda x,x2 : x*x2, valores)
print(sumatoria)

