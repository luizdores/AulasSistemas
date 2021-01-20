import itertools

n = int(input("Informe o numero de niveis: "))
niveis = 0
bits = 1

while niveis != n:
    niveis = 2 ** bits

    if n%niveis != 0:
        print("Entre apenas numeros compativeis")
        exit()

    elif niveis != n:
        bits = bits + 1

print("O numero de bits é de", bits,"\n")
print("E tem essas combinações possiveis")
for i in itertools.product([0,1], repeat=bits):
    print(i)

