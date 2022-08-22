'''
Ejercicio 6
a) Escribir en papel un programa que pida al usuario dos números, y que muestre en
pantalla al mayor de ambos. Luego hacer 3 corridas de escritorio, luego pasarlo a
Python y por último correr el programa con los valores iniciales de las corridas y
verificar que funciona como se esperaba.
b) Ídem anterior pero para encontrar el menor

'''

#valor1 = int(input('Escribir un número '))
#valor2 = int(input('Escribir un número '))
#if (valor1 > valor2):
#    print("El numero mayor es:" + str(valor1) + "El numero menor es:" + str(valor2))
#else:
#print("El numero mayor es:" + str(valor2) + "El numero menor es:" + str(valor1))

###################################################    


'''
Ejercicio 7
Escribir en papel un programa que pida al usuario dos números de punto otante y muestre
su promedio. Además, si el promedio es mayor que 7 el programa debe mostrar en pantalla
Aprobado y si no, debe mostrar desaprobado. Después de hacerlo en papel, pasarlo a Python.

'''

#nota1 = float(input("Escribir nota"))
#nota2 = float(input("Escribir nota"))

#promedio = (nota1+nota2)/2

#if (promedio >= 7):
#    print("Aprobado, tú nota es:" + " " + str(promedio))
#else:
#       print("Desaprobado,  tú nota es:" + " " + str(promedio))

'''
Ejercicio 8
Escribir en papel un programa que tome un número entero positivo ingresado por el usuario
y muestre por pantalla Usted ingresó un número de una sola cifra o Usted ingresó un número
de más de una cifra según corresponda. Realizar 4 corridas de escritorio, escribirlo en Python
y luego correrlo en la computadora con los valores iniciales de las corridas y verificar que hayan
dado como se esperaba.
'''

#cifra = int(input("Ingresar un numero para verificar la cifra"))

#if (cifra < 0):
#    print("Es un numero negrativo, intentalo de nuevo")
#    if (cifra > 9):
#        print("Es un numero de dos cifras")
#        if (cifra > 99):
#            print("Es un numero de tres cifras o mas cifras")
#    else:
#                print("Es un numero de una cifra")



'''
Ejercicio 9 F
Se tiene la siguiente lista con DNIs de personas.
30612453
23763290
21448503
34582048
15364857
Dado otro número de DNI cualquiera, se desea construir un programa que determine si es alguno
de los existentes en el listado. Escribir el programa en papel y luego pasarlo a Python.

'''

#dni = int(input("Escirbir DNI sin putos"))
#if(dni==30612453 or dni==23763290 or dni==214485 or dni==34582048 or dni == 15364857 ):
#    print("Tu DNI esta en la lista!")
#else:
#    print("Tu DNI, NO esta en la lista :(")


'''
Ejercicio 10 F
Hacer en pseudocodigo y luego un programa que calcule el importe que se le facturará a un
cliente por consumo de electricidad sabiendo que la compañía que se la provee cobra una tarifa
ja de 480 pesos que incluye los primeros 200 KW consumidos y los KW excedentes se los cobra
a 25,5 pesos el KW, además se agregan $78 de impuestos. Se leen los valores del medidor al
comienzo y al n del período.

'''
#consumoDeElectricidad = float(int("¿Cuantos KW consumio este mes?"))
#tarifaFija = 480
#adicional = 25.5
#impuestos = 78
#if (consumoDeElectricidad > 200):
#    print((200-consumoDeElectricidad)*adicional + impuestos + tarifaFija)
#else:
#    print(tarifaFija+impuestos)


'''
Ejercicio 11 F
Se desea escribir un programa que pida al usuario tres números y luego muestre el mayor de
ellos. Escribir el programa en papel, realizar 3 pruebas de escritorio y luego pasarlo a Python y
verificar los resutlados.

'''

#n1 = int(input("Escribir un numero "))
#n2 = int(input("Escribir un numero "))
#n3 = int(input("Escribir un numero "))
#3if (n1 > n2  and n1 > n3):
#    print(str(n1)+"El primer numero es el mayor")
#else:
#        print( str(n2) +"El segundo numero es el mayor")
#        if(n3>n1 and n3>n2):
#             print( str(n3) + "El tercer numero es el mayor")


'''
Ejercicio 12
Un profesor clasica las notas de sus alumnos de la siguiente manera:
1-3 Reprobado
4-6 Debe rendir examen nal
7-10 Eximido
a) Escribir un programa que indique la clasicación de una nota.
b) Escribir un programa que pida 3 notas, calcule el promedio e indique la clasicación
del mismo

'''

#nota1 = float(input("Escribir nota"))
#nota2 = float(input("Escribir nota"))
#nota3 = float(input("Escribir nota"))

#promedio = (nota1+nota2+nota3)/3

#if (promedio == 1 or promedio== 2 or promedio == 3):
#    print("Reprobado")
#else:
#    if(promedio == 6 or promedio == 5 or promedio == 4):
#        print("Debe rendir examen final")
#    else:
#            print("Eximido")


'''
Ejercicio 13 F
Escribir un programa que pida al usuario dos enteros y que luego muestre si el primero es
mayor que el segundo o viceversa.

'''

#entero1 = int(input("Escribir un numero entero"))
#entero2 = int(input("Escribir un numero"))

#if (entero1 > entero2):
#    print("El numero mayor es :" + " " + str(entero1))
#else:
#    print("El numero mayor es:"+ " "+ str(entero2))

'''
Ejercicio 14 
Escribir un programa que pida al usuario dos enteros y los guarde en dos variables. Si el
primero de los valores fuera menor que el segundo, el programa deberá además intercambiar los
valores de las variables y mostrarlos de mayor a menor.
'''

#entero1 = int(input("Escribir un numero entero"))
#entero2 = int(input("Escribir un numero"))

#if (entero1 > entero2):
#    print("El numero mayor es :" + " " + str(entero1) + " "+ "El menor es:"+ " " + str(entero2))
#else:
#    print("El numero mayor es:"+ " "+ str(entero2) + " "+ "El menor es:"+" "+ str(entero1))

'''
Ejercicio 15  ♣
Escribir un programa que pida al usuario tres enteros y los guarde en tres variables a, b y c.
El programa deberá luego hacer que en la variable a quede el menor de los valores recibidos, en
b el intermedio y en c el mayor (es decir, ordenará los valores).

'''

#a = int(input("Escribir un numero entero"))
#b = int(input("Escribir un numero"))
#c = int(input("Escribir un numero"))

#if (a>b and b>c and a>c):
#    print("El menor valor es:"+ " "+ str(c)+ " "+ "El valor medio es:"+" "+ str(b) + " " + "El valor mayor es:" + " " + str(a))
#else: 
#    if(b>a and a>c and b>c):
#        print("El menor valor es:"+ " "+ str(c)+ " "+ "El valor medio es:"+" "+ str(a) + " " + "El valor mayor es:" + " " + str(b))
#    else:
#        if(c>b and b>a and c>a):
#            print("El menor valor es:"+ " "+ str(a)+ " "+ "El valor medio es:"+" "+ str(b) + " " + "El valor mayor es:" + " " + str(c))



#Terminar

'''
Ejercicio 16 F
Un año es bisiesto si es múltiplo de 4. Pero no siempre, las excepciones son los años múltiplos
de 100 que no son múltiplos de 400 (1900 no es bisiesto pero 2000, sí). Escribir en papel un
programa que diga si un año ingresado por el usuario es bisiesto, realizar varias pruebas de
escritorio, luego pasarlo a Python y vericar los resutlados

'''

#año = int(input("Ingresar un año"))
#if(año % 4 == 0 and año % 100 !=0) or año % 400 == 0:
#    print("El año:", año, "Es bisiesto")
#else:
#    print("El años", año, "No es bisiesto")