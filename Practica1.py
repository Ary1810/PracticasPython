from flask import Flask
from flask import Flask, json

app = Flask(__name__)

@app.route('/wellcome/')

@app.route('/wellcome/<name>')

@app.route('/wellcome/<int:ncontrol>')

@app.route('/wellcome/<name>/<int:ncontrol>')

def bienvenido(name=None,ncontrol=None):

    if name== None and ncontrol==None:

        return 'Bienvenido '

    if name!= None and ncontrol == None:

        return f'Bienvenido {name}'

    if name == None and ncontrol != None:

        return f'El número recibido es: {ncontrol}'

    else:

        return f'Bienvenido {name} tu numero de control es: {ncontrol}'
    
@app.route("/dict/<path:diccio>")
def show_diccionario(diccio):
    diccionario = json.loads(diccio)
    for clave, valor in diccionario.items():
        print(f"{clave}: {valor}")
    return diccionario

#1 Agregar valor nuevo y clave
@app.route("/dict/add/<path:diccio>/<clave>/<valor>")
def agregar_clave(diccio, clave, valor):
    diccionario = json.loads(diccio)
    print ("Clave a agregar: ", clave, " Valor a agregar: ", valor)
    print("Diccionario inicial:", diccionario)
    diccionario[clave] = valor
    print("Diccionario modificado:", diccionario)
    return diccionario

#2 Borrar con clave
@app.route("/dict/del/<path:diccio>/<clave>")
def eliminar_clave(diccio, clave):
    diccionario = json.loads(diccio)
    print("Clave a eliminar: ", clave)
    print("Diccionario inicial:", diccionario)
    if clave in diccionario:
        del diccionario[clave]
    else: return("Clave no valida")
    print("Diccionario modificado:", diccionario)
    return diccionario


#3 Modificar diccionario 
@app.route("/dict/mod/<path:diccionario>/<clave>/<nuevo_valor>")
def modificar_valor(diccionario, clave, nuevo_valor):
    diccionario = json.loads(diccionario)

    print("Clave a Modificar: ", clave, " Nuevo Valor: " , nuevo_valor)
    print("Diccionario inicial:", diccionario)
    if clave in diccionario:
        diccionario[clave] = nuevo_valor
        print("Diccionario modificado:", diccionario)
        return diccionario
    else: print("No se pudo modificar.")
    return ("Clave invalida")

# 4. Combinar dos diccionarios
@app.route("/dict/combine/<path:dic1>/<path:dic2>")
def combinar_diccionarios(dic1, dic2):
    dic1 = json.loads(dic1)
    dic2 = json.loads(dic2)
    dic3 = dic1 | dic2
    print("Diccionarios combinados:", dic3)
    return dic3

# 5. Agregar elemento a un conjunto
@app.route("/set/add/<path:conjunto>/<elemento>")
def agregar_elemento_conjunto(conjunto, elemento):
    conjunto = set(json.loads(conjunto))
    if elemento not in conjunto:
        conjunto.add(elemento)
        print("Conjunto modificado:", conjunto)
        return {"success": True, "conjunto": list(conjunto)}
    return {"success": False, "message": "El elemento ya está en el conjunto"}

# 6. Eliminar elemento de un conjunto
@app.route("/set/remove/<path:conjunto>/<elemento>")
def eliminar_elemento_conjunto(conjunto, elemento):
    conjunto = set(json.loads(conjunto))
    if elemento.isdigit():
        elemento = int(elemento)
    if elemento in conjunto:
        conjunto.remove(elemento)
        print("Conjunto modificado:", conjunto)
        return {"success": True, "conjunto": list(conjunto)}
    return {"success": False, "message": "No se pudo eliminar"}

# 7. Combinar dos conjuntos
@app.route("/set/combine/<path:conj1>/<path:conj2>")
def combinar_conjuntos(conj1, conj2):
    conj1 = set(json.loads(conj1))
    conj2 = set(json.loads(conj2))
    combinado = conj1 | conj2
    print("Conjunto combinado:", combinado)
    return list(combinado)

# 8. Diferencia de dos conjuntos
@app.route("/set/diff/<path:conj1>/<path:conj2>")
def diferencia_conjuntos(conj1, conj2):
    conj1 = set(json.loads(conj1))
    conj2 = set(json.loads(conj2))
    diferencia = conj1 - conj2
    print("Diferencia de conjuntos:", diferencia)
    return list(diferencia)

# 9. Agregar elemento a una tupla
@app.route("/tuple/add/<path:tupla>/<elemento>")
def agregar_a_tupla(tupla, elemento):
    tupla = tuple(json.loads(tupla))
    nueva_tupla = tupla + (elemento,)
    print("Tupla modificada:", nueva_tupla)
    return list(nueva_tupla)

# 10. Eliminar elemento de una tupla
@app.route("/tuple/remove/<path:tupla>/<elemento>")
def eliminar_de_tupla(tupla, elemento):
    tupla = tuple(json.loads(tupla))
    nueva_tupla = tuple(x for x in tupla if x != elemento)
    print("Tupla modificada:", nueva_tupla)
    return list(nueva_tupla)

# 11. Concatenar dos tuplas
@app.route("/tuple/concat/<path:tupla1>/<path:tupla2>")
def concatenar_tuplas(tupla1, tupla2):
    tupla1 = tuple(json.loads(tupla1))
    tupla2 = tuple(json.loads(tupla2))
    nueva_tupla = tupla1 + tupla2
    print("Tupla concatenada:", nueva_tupla)
    return list(nueva_tupla)

# 12. Revertir una tupla
@app.route("/tuple/reverse/<path:tupla>")
def revertir_tupla(tupla):
    tupla = tuple(json.loads(tupla))
    nueva_tupla = tupla[::-1]
    print("Tupla revertida:", nueva_tupla)
    return list(nueva_tupla)

# 13. Imprimir diccionario
@app.route("/dict/print/<path:diccionario>")
def imprimir_diccionario(diccionario):
    diccionario = json.loads(diccionario)
    print("Diccionario:", diccionario)
    return diccionario

# 14. Imprimir tupla
@app.route("/tuple/print/<path:tupla>")
def imprimir_tupla(tupla):
    tupla = tuple(json.loads(tupla))
    print("Tupla:", tupla)
    return list(tupla)

# 15. Imprimir conjunto
@app.route("/set/print/<path:conjunto>")
def imprimir_conjunto(conjunto):
    conjunto = set(json.loads(conjunto))
    print("Conjunto:", conjunto)
    return list(conjunto)