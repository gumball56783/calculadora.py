matriz = []
A = []
B = []
C = []
print("Hola, por favor ingresa el tamaño de la matriz, luego las coordenadas de los puntos A,B y C")
matriz=[int(item) for item in input(" Tamaño Matriz ").split()]
A=[int(item) for item in input(" coordenadas A ").split()]
B=[int(item) for item in input(" coordenadas B ").split()]
C=[int(item) for item in input(" coordenadas C ").split()]
DAB=abs(abs(A[0]-B[0])+abs(A[1]-B[1]))
DAC=abs(abs(A[0]-C[0])+abs(A[1]-C[1]))
if DAC<DAB :
    print (DAC)
    print ("C")

else:
    print (DAB)
    print ("B")
#Envía un mensaje a todos