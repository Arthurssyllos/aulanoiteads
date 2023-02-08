n1 = float(input("Entre com a nota um: "))
n2 = float(input("Entre com a nota dois: "))
n3 = float(input("Entre com a nota três: "))
me = float(input("Entre com ME: "))

ma = (n1 + n2 * 2 + n3 * 3 + me)/7

if (ma >= 9):
    print ("Maior ou igual a 9")

if (ma < 4):
    print("Menor que 4")