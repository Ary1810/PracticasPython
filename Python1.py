#Elaborado por Quevedo Ramirez Ary Alberto                                                  C20491106 
# 1. Función que reciba un diccionario y agregue una clave-valor, retornando el diccionario modificado

def agregar_clave(diccionario, clave, valor):
    print ("Clave a agregar: ", clave, " Valor a agregar: ", valor)
    print("Diccionario inicial:", diccionario)
    diccionario[clave] = valor
    print("Diccionario modificado:", diccionario)
    return diccionario

# 2. Función que reciba un diccionario y elimine una clave-valor, retornando el diccionario modificado

def eliminar_clave(diccionario, clave):
    print("Clave a eliminar: ", clave)
    print("Diccionario inicial:", diccionario)
    if clave in diccionario:
        del diccionario[clave]
    else: print("Clave no valida")
    print("Diccionario modificado:", diccionario)
    return diccionario

# 3. Función que reciba un diccionario y modifique el valor de una clave, retornando verdadero si pudo modificar y falso si no pudo

def modificar_valor(diccionario, clave, nuevo_valor):
    print("Clave a Modificar: ", clave, " Nuevo Valor: " , nuevo_valor)
    print("Diccionario inicial:", diccionario)
    if clave in diccionario:
        diccionario[clave] = nuevo_valor
        print("Diccionario modificado:", diccionario)
        return True
    else: print("No se pudo modificar.")
    return False

# 4. Función que combine dos diccionarios, regresando el diccionario resultante

def combinar_diccionarios(dic1, dic2):
    print("Diccionarios iniciales:", dic1, dic2)
    dic3 = dic1 | dic2
    print("Diccionario combinado:", dic3)
    return dic3

# 5. Función que agregue elementos a un conjunto, retornando verdadero si pudo agregar y falso si no pudo

def agregar_elemento_conjunto(conjunto, elemento):
    print("Elemento a agregar: " + elemento)
    print("Conjunto inicial:", conjunto)
    if elemento not in conjunto:
        conjunto.add(elemento)
        print("Conjunto modificado:", conjunto)
        return True
    print("El elemento ya está en el conjunto.")
    return False

# 6. Función que elimine un elemento de un conjunto, retornando verdadero si pudo eliminar y falso si no pudo

def eliminar_elemento_conjunto(conjunto, elemento):
    print("Elemento a eliminar: " + elemento)
    print("Conjunto inicial:", conjunto)
    if elemento in conjunto:
        conjunto.remove(elemento)
        print("Conjunto modificado:", conjunto)
        return True
    print("No se pudo eliminar.")
    return False

# 7. Función que combine dos conjuntos, regresando el conjunto resultante

def combinar_conjuntos(conj1, conj2):
    print("Conjuntos iniciales:", conj1, conj2)
    combinado = conj1 | conj2
    print("Conjunto combinado:", combinado)
    return combinado

# 8. Función que regrese la diferencia de dos conjuntos

def diferencia_conjuntos(conj1, conj2):
    print("Conjuntos iniciales:", conj1, conj2)
    diferencia = conj1 - conj2
    print("Diferencia de conjuntos:", diferencia)
    return diferencia

# 9. Función que agregue un elemento a una tupla y lo guarde en una nueva tupla, regresando la nueva tupla

def agregar_a_tupla(tupla, elemento):
    print("Elemento a agregar: ", elemento)
    print("Tupla inicial:", tupla)
    nueva_tupla = tupla + (elemento,)
    print("Tupla modificada:", nueva_tupla)
    return nueva_tupla

# 10. Función que elimine un elemento de una tupla y lo guarde en una nueva tupla, regresando la nueva tupla

def eliminar_de_tupla(tupla, elemento):
    print("Elemento a eliminar: ", elemento)
    print("Tupla inicial:", tupla)
    nueva_tupla = tuple(x for x in tupla if x != elemento)
    print("Tupla modificada:", nueva_tupla)
    return nueva_tupla

# 11. Función que concatene dos tuplas en una nueva, regresando la nueva tupla

def concatenar_tuplas(tupla1, tupla2):
    print("Tuplas iniciales:", tupla1, tupla2)
    nueva_tupla = tupla1 + tupla2
    print("Tupla concatenada:", nueva_tupla)
    return nueva_tupla

# 12. Función que revierta el orden de una tupla y lo guarde en una nueva tupla, regresando la nueva tupla

def revertir_tupla(tupla):
    print("Tupla inicial:", tupla)
    nueva_tupla = tupla[::-1]
    print("Tupla revertida:", nueva_tupla)
    return nueva_tupla

# 13. Función que recibe un diccionario y lo imprime

def imprimir_diccionario(diccionario):
    print("Diccionario:", diccionario)

# 14. Función que recibe una tupla y la imprime

def imprimir_tupla(tupla):
    print("Tupla:", tupla)

# 15. Función que recibe un conjunto y lo imprime

def imprimir_conjunto(conjunto):
    print("Conjunto:", conjunto)

#############################################################################################################

# Diccionario de prueba  
diccionario = {'ary' : 1, 'alberto' : 2, 'manzana': 3}
#Agregar clave y dato 
print("Agregar clave y dato")
agregar_clave(diccionario, 'ramirez', 4)

#Quitar clave junto a su dato
print("\nEliminar clave y su dato asociado")
eliminar_clave(diccionario, "ary")

#Modificar clave 
print("\nModificar clave de diccionario")
modificar_valor(diccionario, 'alberto', "Nuevo valor")

#Combinar dos diccionarios 
print("\nUnir dos diccionarios")
diccionario2 = {'clave1' : 'rojo', 'clave2' : 'blanco', 'clave3' : 'amarillo', 'clave4' : 'rojo'}
combinar_diccionarios(diccionario, diccionario2)

#Agregar a un conjunto 
conjunto_1 = set (['C1', 'C2','C3','C4'])
print("\nAgregar a un conjunto")
agregar_elemento_conjunto(conjunto_1, 'ElmExtra')

#Eliminar de un conjunto
print("\nEliminar de un conjunto")
eliminar_elemento_conjunto(conjunto_1,'ElmExtra')

#Combinar 2 conjuntos
conjunto_2 = set (['D1', 'D2','D3','D4','C4'])
print("\nCombinar dos conjuntos")
combinar_conjuntos(conjunto_1,conjunto_2)

#Diferencia entre 2 conjuntos
print("\nDiferencia entre dos juntos")
diferencia_conjuntos(conjunto_1, conjunto_2)

#Agregar un elemento a una tupla, regresando una tupla nueva modificada
print("\nCrear una tupla agregando un elemento a una tupla ya existente")
tupla = (1,2,3)
agregar_a_tupla(tupla,4)

#Eliminar de una tupla creando una nueva tupla 
print("\n Eliminar de tupla") 
eliminar_de_tupla(tupla,3)

#Unir 2 tuplas 
tupla2 = (4,5,6)
print("\nConcatenar 2 tuplas en una nueva") 
concatenar_tuplas(tupla, tupla2)

#Invertir tuplas
print("\nInvertir una tupla en una nueva") 
revertir_tupla(tupla)

#Imprimir diccionario 
print("\nImprimir diccionario") 
imprimir_diccionario(diccionario)

#Imprimir tupla
print("\nImprimir tupla")
imprimir_tupla(tupla)

#Imprimir conjunto
print("\nImprimir conjunto")
imprimir_conjunto(conjunto_1)