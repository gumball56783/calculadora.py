# inicializaa variable
cadena = []
# pide los datos
print("dame la cantidad de numeros a procesar")
valor = int(input())
cadena=[int(item) for item in input(" ingresar numeros > ").split()]
print (cadena)
# inicializa las variables a utilizar
A=cadena[0]
B=cadena[1]
DIF=abs(A-B)
RES=DIF
VALA=A
VALB=B
POSA=0
POSB=1
# Realiza calculos
for x in range(valor-1): 
    for y in range(x+1):
      for y in range((x+1),valor):
        if abs(cadena[x]-cadena[y])<RES: 
            RES=abs(cadena[x]-cadena[y]) 
            VALA=cadena[x]
            VALB=cadena[y]
            POSA=x
            POSB=y
# Imprime resultado
print (RES)
print (VALA," ",VALB)
print (POSA," ",POSB)
# Final del programa
# inicializaa variable
cadena = []
# pide los datos
print("dame la cantidad de numeros a procesar")
valor = int(input())
cadena=[int(item) for item in input(" ingresar numeros > ").split()]
print (cadena)
# inicializa las variables a utilizar
A=cadena[0]
B=cadena[1]
DIF=abs(A-B)
RES=DIF
VALA=A
VALB=B
POSA=0
POSB=1
# Realiza calculos
for x in range(valor-1): 
    for y in range(x+1):
      for y in range((x+1),valor):
        if abs(cadena[x]-cadena[y])<RES: 
            RES=abs(cadena[x]-cadena[y]) 
            VALA=cadena[x]
            VALB=cadena[y]
            POSA=x
            POSB=y
# Imprime resultado
print (RES)
print (VALA," ",VALB)
print (POSA," ",POSB)
# Final del programa