# ##condicionales
# # == igual
# # > mayor que
# # < menor que
# # >= mayor o igual 
# # <= menor o igual que
# # ! = distinto o no igual


# a=3 
# # pregunta 1
# if a > 3:
#     print("si, a es mayor a 3)")
#     print("chau!")
# else:
#     print("no, a no es mayor a 3")
# # pregunta 2
# if a ==3:
#     print("a es igual a 3")

# nota= 60
# # pregunta 3
# if nota>= 60:
#     print("pasasteeee!!!")
# else:
#         print("hule ya") 

# #########
# # Ej. crear una funcion que reciba como parametro una
# # nota del 1 al 100 e imprimir si pasaste o te aplazaste ( se aprueba con 61)

# nota_alum=1

# def info_calif(puntaje):
# # pregunta
#     if puntaje> 60:
#         print("lo lograste")
#     else:
#         print(" no pasaste")
# info_calif(nota_alum)
# ####

# def puntaje(nota, nombre):
#     if nota>=60:
#        print("pasaste", nombre)
#     else:
#       print("no pasate", nombre)
# puntaje(60,"pepito")

# a=6  
# if a > 5 and a < 10:
#     print("a es mayor 5 y menor que 10")
# else:
#     print("a no es igual en el rango; alguna de las 2 condiciones no se cumplieron")

# if a > 5 or a < 10:
#     print(" a es mayor que 5 o menor que 10")
# else:
#     print("a no es mayor que 5 ni menor que 10")
# #####
# edad=7
# if edad > 18:
#     print("deberia estar en la universidad")
# elif edad > 13:
#     print("deberia estar en la secundaria")
# elif edad > 6:
#     print("deberia estar en la primaria")
# else:
#     print("deberia estar en la casa")
# # anidado
# if edad > 18:
#      print("universidad")
# else:
#     if edad>13:
#         print("secundaria")
#     else:
#         if edad >6:
#             print("primaria")
#         else:
#             print("bbdc")

# # Ej. Crear una funcion puntaje que reciba como parametro una nota 
# # del 1 al 100 e imprima que nota sacaste
# # nota< 60--->1
# # nota entre 60 y 70 --->2
# # nota entre 71 y 75 ---> 3
# # nota entre 76 y 85 ---> 4
# # nota mayor que 85 ---> 5
# # sin funcion
# nota= 95
# def notafinal(nota):
#     if nota<=60:
#         print("te aplazaste")
#     elif nota >= 61 and nota<=70:
#         print("pasaste con un 2i")
#     elif nota >70 and nota <=75:
#         print("pasaste con 3")
#     elif nota >=76 and nota<=85:
#         print("pasate con 4") 
#     elif nota > 86 and nota <=100:
#         print("pasaste con 5")
# ##### con funcion
# #def nivel(puntaje):
# #    in puntaje < 60 and puntaje <70:
# #     print("sacaste 1")
# #    elif puntaje > 71 and puntaje < 75:
# #        print("sacaste 2")
# #    elif puntaje <76 and puntaje > 85:
# #        print("sacaste 3")
# #    elif puntaje > 85:
# #        print("sacaste 5")
# #    else:
# #        print("ausente")

# ############
# # Ej. Pedir al usuario que ingrese tres numeros y multiplicarlos
# # entre si, imprimir el resultado

# num1= input(("ingresar el primer numero:"))
# numero1= int(num1)
# num2=input("ingresar el segundo numero")
# numero2= int(num2)
# num3=input("ingresar el tercer numero")
# numero3= int(num3) 

# multiplicacion=(numero1*numero2*numero3)
# print("el resultado es",multiplicacion)
# ######
# # Ej. pedir al usuario un numero del 1 al 100 y llamar a la
# # funcion que retornaba la nota que creamos hace un rato
# # utilizando el valor ingresado por el usuario

# nota= int(input("ingrese la nota"))
# notafinal(nota)

# ######## Bucle while== mientras ###

# x=74956
# while x != 5:
#     print("hola esto es un bucle while, se va a ejecutar mientras x sea distinto")
#     x= int(input("ingresar un numero.")) # ingresamos un valor para x
#     print("el valor de x ahora es", x)
# print("termino!!!")
# # contador inverso
# contador= 10
# while contador > 0:
#     print("sigo en el bucle while")
#     contador= contador-1
#     print("te quedan", contador, "oportunidades")
# print("termino")

# # contador

# while contador>0:
#     print("sugo en el bucle while")
#     contador=contador+1

# # usando while pedir al usuario 5 ingredientes para hacer una pizza
# # y agregar a una lista, al final imprimir la lista


# lista_ingrediente=[]
# contador=0
# while contador < 10:
#     ingredientes=input("lista de compras")
#     lista_ingrediente.append(ingredientes)
#     contador=contador+1
# print("lista de compras", lista_ingrediente)

########
# Ej. crear un juego de adivinar el numero como el de arriba y
# darle pista al usuario si el numero que ingreso es mayor o menor
# al numero a adivinar
# pista usar elif

# numero_secreto=7
# adivino= False
# while adivino == False:
#     apuesta= input("adivina el numero secreto del 1 al 10: ")

#     if int(apuesta) == numero_secreto:
#         print("ganaste!!!")
#         adivino= True
#     else:
#         print("segui participando nde arruinado")

######
from random import randrange
numero_secre=randrange(10)
adivina= False
while adivina== False:
    apuesta=input("adivina el numero del 1 al 10: ")

    if int(apuesta) == numero_secre:
        print("bingooo!!!")
        adivina= True
    elif int (apuesta)> numero_secre:
        print("es un numero menor")
    else:
        print("es un numero mayor")








