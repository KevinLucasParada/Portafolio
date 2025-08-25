# iteraciones.py

# Bucle for
print("Recorriendo una lista con for:")
frutas = ["manzana", "pera", "plátano"]
for fruta in frutas:
    print("- ", fruta)

# Bucle for con range
print("\nNúmeros del 1 al 5:")
for i in range(1, 6):
    print(i)

# Bucle while
print("\nContando con while:")
contador = 0
while contador < 3:
    print("Contador:", contador)
    contador += 1

# Usando break
print("\nUso de break:")
for num in range(10):
    if num == 5:
        break
    print(num)

# Usando continue
print("\nUso de continue:")
for num in range(5):
    if num == 2:
        continue
    print(num)
