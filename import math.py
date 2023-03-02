import math 
print("===CALCULADORA===")
print("Elige una opción")
print("1-Suma")
print("2-Resta")
print("3-Multiplicación")
print("4-División")
print("5-potenciación")
print("6-raiz cuadrada")
x= input("Escribe tu elección:")
y=float(x)

if(y==1):
    a=input("Introduce el primer numero\n")
    b=input("Introduce el segundo numero\n")
    a2=float(a)
    b2=float(b)
    resultado= a2+b2
    print("El resultado de la suma es:",resultado)
elif(y==2):
    a=input("Introduce el primer numero\n")
    b=input("Introduce el segundo numero\n")
    a2=float(a)
    b2=float(b)
    resultado= a2-b2
    print("El resultado de la resta es:",resultado)
elif(y==3):
    a=input("Introduce el primer numero\n")
    b=input("Introduce el segundo numero\n")
    a2=float(a)
    b2=float(b)
    resultado= a2*b2
    print("El resultado de la multiplicación es:",resultado)
elif(y==4):
    a=input("Introduce el primer numero\n")
    b=input("Introduce el segundo numero\n")
    a2=float(a)
    b2=float(b)
    resultado= a2/b2
    print("El resultado de la división es:",resultado)
elif(y==5):
    a=input("introduce el primer numero\n")
    b=input("Introduce el segundo numero\n")
    a2=float(a)
    b2=float(b)
    resultado= a2**b2
    print("El resultado de la potencia es:",resultado)
elif(y==6):
    a=input("introduce el primer numero\n")
    b=input("Introduce el segundo numero\n")
    a2=float(a)
    b2=float(b)
    resultado= math.sqrt(a2)
    print("el resultado de la raiz cuadrada es:",resultado)
else:
    print("NUMERO INVALIDO")