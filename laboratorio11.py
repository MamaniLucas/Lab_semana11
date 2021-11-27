alumnos = {
    'alumno1': 'Juan Perez',
    'alumno2': 'Maria Lopez',
    'alumno3': 'Pedro Martinez',
    'alumno4': 'Ana Sanchez',
    'alumno5': 'Luis Gomez',
}
print(alumnos)
# len() es la funcion que se encarga de contar
# cuantos elementos tiene un diccionario
print(len(alumnos))
# Imprimir solo claves
print(alumnos.keys())
# Imprimir los valores
print(alumnos.values())

# version 1
print(alumnos['alumno1'])

print("*"*30)
for key in alumnos.keys():
    print(alumnos[key])

print("*"*30)

alumnos['alumno6'] = 'Lucas Solano'


alumnos_nuevos = {
    'alumno7': 'Carla Ferndez'
}

alumnos.update(alumnos_nuevos)

print("*"*30)
print(alumnos)

del alumnos['alumno6']

# En esta fase alumnos si tiene valores
alumnos_copy = alumnos.copy()

# Luego de asignar los valores a copy recien se esta eliminando
# alumnos
alumnos.clear()

print("*"*30)
print(alumnos)
print("alumnos_copy")
print("* "*30)
print(alumnos_copy)


# Convertir un diccionario a u tuplas
print(alumnos_copy.items())
print("* "*30)
print(alumnos_nuevos)

usuarios = {}

while True:
    email = input("Ingrese un email: ")
    password = input("Password: ")
    # verificar si el email existe
    if usuarios.get(email) is None:
        usuarios[email] = password
    else:
        print("El email ya existe")

    opcion = input("Desea ingresar otro email? (s/n) ")
    if opcion == "n":
        print("Usuarios registrados: ", usuarios)
        break