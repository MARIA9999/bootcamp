# tipo de dato string/cadena/str de texto
#"esto es string"
# tipo de dato integer/entero/int
#105
# liatas
#[]#lista vacia
#["MAbel", 24, "Administradora"] #Lista de 3 elementos
# variables
#nombre= "MAbel"
#edad=30+3
#edad_mal="30+3"
#variable_lista=["hola",nombre,44]
# Acceder a un elemento de la lista
#print(variable_lista[0],edad, variable_lista[2])
#Acciones/operaciones sobre listas
#variables_lista.append("bailar") #agregar elemento a lista
#variable_lista.pop() #eliminar ultimo elemento
#variable_lista[2] = 50
#print(variable_lista)
#variable_lista[2] = "chau"
#print("variable_lista es", variable_lista)

# Bucles / Loop / Ciclos
#Imprimir cada elemento de una lista
#for loquesea in varable_lista:
#    print(loquesea)

# Imprimir los numeros del 1 al 10
#for cualquiercosa in range(10): 
#    print(cualquiercosa +1)


# Imprimir el ultimo elemento de una lista sin saber cuantos
#Elementos tiene;solucion general
#otra_lista=[5, "hola que tal", "Chau",4]
#otra_lista.append("AAAA")
#print(otra_lista)
#print(otra_lista[len(otra_lista)-1])

#dimension_de_lista=len(otra_lista)-1


#print("--------------------------")
# Solucion paso por paso
#dim_lista=len(otra_lista)
#print("la dimension de otra_lista es", dim-lista)
#indice_del_ultimo=dim_lista-1
#print("el indice del ultimo elemento es", indice_del_ultimo)
#print(otra_lista[indice_del_ultimo])

# solucion de una lista
#print(otra_lista[len(otra_lista)-1)])

#esto es equivalente
#for numero in range(1,11):
#    print(numero)
#a esto
#for numero in range(1,10):
    print(numero)
# imprimir hola 10 veces
#for numero in [1,2,3,4,5,6,7,8,9,10]:
#    print("hola", numero) #imprimir numero es opcional

#imprimir el numero de resultado de la suma de los numeros del 1 al 10, 55

#desafio=[1,2,3,4,5,6,7,8,9,10] # se crea una lista
#a=0                            #se crea una variable de base
#for x in desafio:          # se crea un ciclo que va correr la cantidad de elemento lista de desafio
#    a=a+x              #se van acumulando las sumas parciales
#print(a)

#sumatoria=0
#for valor in range(1,11)
    sumatoria= sumatoria + valor

#print(sumatoria)

############# Funciones #############
def nombre_de_la_funcion

def suma (num1,num2):
    resultado= num1,num2
    return resultado

#equibalente a la de arriba
def suma2(num1,num2):
    return num1+num2

print(suma(5,10))
resul=suma(5,8)
print(resul)

# Crear una funcion resta, que reciba como parametro dos numeros
# y retorne la resta de esos numeros 
# luego llamer a la funcion e imprimir el resultado
# Crear una funcion saludo que reciba como parametro nombre y edad 
# e imprima "hola soy-____ " y tengao___anhos"
# llamar varias veces a la funcion con distintos valores 
# nota: retornar algo opcional

def saludos2(n1,n2):
    resultado2= n1-n2
    return resultado2
print("recibe el valor de",saludos2(20,10))


