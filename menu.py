emp = {501: "Plaza Vea", 502: "Batta", 503: "KFC"}

while True:
    n = input("Elija una opción: \n"
              "a. Registrar clientes \n"
              "b. Mostrar clientes \n"
              "c. Buscar clientes \n"
              "d. Actualizar clientes \n"
              "e. Eliminar clientes \n"
              "f. Salir\n")
    if n == "a":
        ruc = int(input("Ingrese el ruc de la empresa: "))
        nombre = (input("Ingrese el nombre de la empresa: "))
        emp[ruc] = nombre
        print("\nEMPRESA AGREGADA CON ÉXITO\n")
        print("*"*50, "\n")
    elif n == "b":
        for key in emp:
            print(key, " : ", emp[key])
        print("")
        print("*"*50, "\n")
    elif n == "c":
        ruc = int(input("Ingrese el número de RUC de la empresa a busca: "))
        print(emp[ruc])
        print("")
        print("*"*50, "\n")
    elif n == "d":
        ruc = int(input("Ingrese el número de RUC de la empresa a actualizar: "))
        nombre = input("Ingrese el nuevo nombre de la empresa: ")
        emp[ruc] = nombre
        print("\nEMPRESA ACTUALIZADA CON ÉXITO\n")
        print("*"*50, "\n")
    elif n == "e":
        ruc = int(input("Insertar el número de ruc de la empresa que quiere eliminar: "))
        del emp[ruc]
        print("\nEMPRESA ELIMINADA CON ÉXITO\n")
        print("*"*50, "\n")
    if n == "f":
        break
    
