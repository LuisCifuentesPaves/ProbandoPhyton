#imprimir varios elementos

milista = [1,2,3,4,5]

for elemento in milista:
    print(elemento)

#para agregar elementos a una lista .append

milista = [1,2,3,4,5]
milista.append(6)
for elemento in milista:
   print(elemento)

# .insert permite insertar dentro de la lista

milista = [1,2,3,4,5]
milista.insert(3,"Juan")

for elemento in milista:
  print(elemento)

  # .remove permite remover elementos

milista = [1,2,3,"Juan",4,5]
           
milista.remove("Juan")

# .reverse() invertir los elementos de una lista

milista = [1,2,3,"Juan",4,5]
milista.reverse()

#También podemos utilizar la función sort() para ordenar los elementos de numéricos de menor a mayor.
#.sort choca cuando tiene un string, solo se utiliza con números
milista = [1,2,3,"Juan",4,5]
           
milista.sort()

#Diccionarios - Los diccionarios son estructuras de datos eficientes y versátiles que nos sirven para referenciar un valor con una clave.

diccionario = {"nombre": "Cesar Huispe",
"fonos": [
988778882,
988877776,
877666333],
"activo": True}

# Búsqueda
print("Nombre:", diccionario["nombre"])
print("Segundo teléfono:", diccionario["fonos"][1])
# Inserción
diccionario["email"] = "cesar.huispe@example.com"
diccionario["fonos"].append(123456789)
# Actualización
diccionario["activo"] = False
diccionario["fonos"][0] = 999999999
# Eliminación
del diccionario["activo"]
diccionario["fonos"].pop(2)
print(diccionario)
