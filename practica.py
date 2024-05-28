print("------------Suma----------------")
a = 5
b = 2
resultado = a + b
print(resultado)

print("------------Resta----------------")
a = 5
b = 2
resultado = a - b
print(resultado)

print("------------Multiplicación----------------")
a = 5
b = 2
resultado = a * b
print(resultado)

print("------------División----------------")
a = 5
b = 2
resultado = a / b
print(resultado)

print("------------División Entera----------------")
a = 5
b = 2
resultado = a // b
print(resultado)

print("------------Modulo----------------")
a = 5
b = 2
resultado = a % b
print(resultado)

print("------------Contador----------------")
contador = 0
contador += 1 
print(contador)

print("------------Igualdad----------------")
a = 5
b = 2
resultado = a == b
print(resultado)

print("------------Desigualdad----------------")
a = 5
b = 2
resultado = a != b
print(resultado)

print("------------Mayor que----------------")
a = 5
b = 2
resultado = a > b
print(resultado)

print("------------Menor que----------------")
a = 5
b = 2
resultado = a < b
print(resultado)

print("------------Mayor o igual que y menor o igual que----------------")
a = 5
b = 2
resultado = a >= b
print(resultado)

a = 5
b = 2
resultado = a <= b
print(resultado)

print("-----------------ESTRUCTURAS DE CONTROL---------------------")

a = 10
if a > 5:
    print("Es mayor que 5")
else:
    print("No es mayor que 5")

print("-----------------ESTRUCTURAS DE CONTROL IF-ELSE-IF-ELSE---------------------")

a = 10
if a > 0:
    print("Es mayor que 5")
elif a < 0:
    print("No es mayor que 5")
else:
    print("No es mayor que 5")

print("-----------------ESTRUCTURAS DE CONTROL WHILE---------------------")

contador = 1
while contador <= 5:
    print(contador)
    contador += 1	

print("-----------------ESTRUCTURAS DE CONTROL FOR---------------------")
frutas =["manzana", "banano", "naranja"]
     
for fruta in frutas:
        print(fruta)

for i in range(1, 6):
     print(i)

print("-----------------AREA DE UN TRIANGULO---------------------")

base = int(input("Ingrese la base del triangulo: "))

altura = int(input("Ingrese la altura del triangulo: "))

area = (base * altura) / 2
print("El area del triangulo es: ", area)

print("-----------------NUMERO PRIMO O NO---------------------")

numero = int(input("Ingrese un numero entero positivo: "))
es_primo = True

if numero <= 1:
     es_primo = False
else:
     for i in range(2, (numero // 2) + 1):
         if numero % i == 0:
             es_primo = False
             break
if es_primo:
     print("El numero es primo")
else:
     print("El numero no es primo")