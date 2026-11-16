import random

# Generamos una lista con 100 notas aleatorias entre 0 y 10
notas = []
while len(notas) < 100:
    nota = random.randint(0, 10)
    notas.append(nota)

# Contamos cuántos ceros hay en la lista
numCeros = notas.count(0)
print("En mi lista tengo", numCeros, "ceros.")

# Eliminamos todos los ceros de la lista de forma eficiente
# La comprensión de listas crea una nueva lista con todos los elementos que NO son cero
notas = [nota for nota in notas if nota != 0]

# Mostramos la lista ya sin ceros y su longitud
print(len(notas), notas)
