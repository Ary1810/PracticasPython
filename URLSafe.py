from urllib.parse import quote
#Es para poner los diccionarios en el URL

diccionario_json = '{"d": 4, "e": 5, "f": 6}'
url_safe_json = quote(diccionario_json)
print(url_safe_json)  