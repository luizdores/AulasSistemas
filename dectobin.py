dec = int(input("Entre com o valor em decimal para ser convertido para binario"))
temp = 0
mod = 1


while mod != 0:
    bin = dec / 2

    if bin / 2 != 0:
        temp = temp + bin
        mod = temp%2
        print(mod)
        print(temp)
        print(bin)


