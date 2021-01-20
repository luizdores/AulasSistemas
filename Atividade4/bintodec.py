import numpy

bin = int(input("Entre com um numero em binario: "))
lista = list(map(int, str(int(bin))))
array = numpy.array(lista)
reversed_array=numpy.flip(array)
expo = 0
temp = 0
temp2 = 0

while expo != len(reversed_array):
    temp = reversed_array[expo] * 2 ** expo
    temp2 = temp2 + temp
    expo = expo + 1

print(f"Seu valor em decimal é de {temp2}")

