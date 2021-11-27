empresas = {
    108212313: "Tecsup",
    424134134: "UdeA",
}

while True:
    # Creacion de menu
    print("\n"
          "Opcion 1) Registrar clientes \n"
          "Opcion 2) Mostrar clientes \n"
          "Opcion 3) Buscar clientes \n"
          "Opcion 4) Actualizar  clientes \n"
          "Opcion 5) Eliminar  clientes \n"
          "Opcion 6) v Salir clientes"
          )

    opcion = input("Escoja una opcion: ")

    if opcion == "1":
        ruc = int(input("Ingrese el RUC: "))
        nombre = input("Nombre de empresa: ")
        empresas[ruc] = nombre
    elif opcion == "2":
        print("Mostrar clientes", empresas)
    elif opcion == "3":
        print("Buscar clientes")