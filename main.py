def datos():
    suma = []
    while True:
        print("")
        print("1. Ingresar numero\n"
              "2. ver datos\n"
              "3. regresar al menu")
        select_dato = input("Seleccione una opcion: ")
        match select_dato:
            case "1":
                while True:
                    print("1. Ingresar numero\n"
                          "2. regresar al menu\n")
                    select1 = input("Seleccione una opcion: ")
                    match select1:
                        case "1":
                            num_dato = int(input("Ingresar numero: "))
                            suma.append(num_dato)
                            print("Numero agregado")
                        case "2":
                            print("Regresando al menu")
                            break
            case "2":
                print("Datos regresados")
                positivo = 0
                negativo = 0
                cero = 0
                for i in suma:
                    if i > 0:
                        positivo += 1
                    if i < 0:
                        negativo += 1
                    if i == 0:
                        cero += 1
                multiplo = 0
                for e in suma:
                    if e % 3 == 0:
                        multiplo += 1
                print(f"La suma total es de: {sum(suma)}\n"
                      f"El promedio total es de: {sum(suma) / len(suma)}\n"
                      f"La cantidad total de positivos: {positivo}\n"
                      f"La cantidad total de negativos: {negativo}\n"
                      f"La cantidad total de ceros: {cero}\n")
datos()
