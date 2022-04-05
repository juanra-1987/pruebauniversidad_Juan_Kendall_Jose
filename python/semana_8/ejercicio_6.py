import os
os.system ("cls")

#diccionarios
lista =[] #corchetes
tuplas = () #parentesi
diccionario = {
                "dato1":1,
                "dato2":2,
                "dato3":3

} #llaves el acronimo es dict

print (diccionario["dato1"])

diccionario["dato4"] =44

print (diccionario.get("dato1"))

print (diccionario.items())

print (diccionario.keys())

print (diccionario.values())

print (diccionario.pop("dato1"))

print (diccionario)

print (diccionario.popitem())

print (diccionario)