from unittest import case


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
                        case _:
                            print("Opcion invalida")
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
                      f"La cantidad total de ceros: {cero}\n"
                      f"la cantidad de multiplos de 3 son: {multiplo}\n")
                break
            case "3":
                print("Regresando al menu")
                break
            case _:
                print("opcion no valida")

def area_triangulo(a, b):
    area = a * b / 2
    print(f"El area del triangulo es de: {area}")

def perimetro_triangulo(a, b, c):
    perimeter = a + b + c
    print(f"El perimetro del triangulo es de: {perimeter}")

def n_primo():
    a = int(input("Ingresar un numero: "))
    if a % 2 == 0:
        print("El numero no es primo")
    else:
        print("El numero es primo")

def promedio():
    promedio = []
    while True:
        print("1. Ingresar calificacion\n"
              "2. ver resultados\n"
              "3. regresar al menu\n")
        select_calificacion = input("Seleccione una opcion: ")
        match select_calificacion:
            case "1":
                while True:
                    print("1. Ingresar calificacion\n"
                          "2. regresar al menu\n")
                    select1 = input("Seleccione una opcion: ")
                    match select1:
                        case "1":
                            calificacion = int(input("Ingresar calificacion: "))
                            promedio.append(calificacion)
                        case "2":
                            print("Regresando al menu")
                            break
                        case _:
                            print("Opcion invalida")
            case "2":
                print("Promedio de calificacion")
                alto = 0
                riesgo = 0
                for i in promedio:
                    if i >= 85:
                        alto += 1
                    if i < 60:
                        riesgo += 1
                print(f"El promedio de calificacion es de: {sum(promedio)/len(promedio)}\n"
                      f"Notas que estan arriba de 85: {alto}\n"
                      f"Notas que estan en zona ade riesgo: {riesgo}\n")
            case "3":
                print("Regresando al menu")
                break
            case _:
                print("opcion no valida")

def calcular():
    while True:
        print("----Bienvenido a la calculadora de operaciones basicas----\n"
              "1. Suma\n"
              "2. Resta\n"
              "3. Multiplicacion\n"
              "4. Division\n"
              "5. Salir")
        calc_select = input("Seleccione una opcion: ")
        match calc_select:
            case "1":
                print("Ingrese dos numeros para ser sumados\n")
                n1 = int(input("Ingresar primer numero: "))
                n2 = int(input("Ingresar segundo numero: "))
                print(f"La suma de {n1} + {n2} es = {n1 + n2}\n")
            case "2":
                print("Ingrese dos numeros para ser restados\n")
                r1 = int(input("Ingresar primer numero: "))
                r2 = int(input("Ingresar segundo numero: "))
                print(f"La resta de {r1} + {r2} es = {r1 - r2}")
            case "3":
                print("Ingrese dos numeros para ser multiplicacion\n")
                m1 = int(input("Ingresar primer numero: "))
                m2 = int(input("Ingresar segundo numero: "))
                print(f"La multiplicacion de {m1} * {m2} es = {m1 * m2}")
            case "4":
                print("Ingrese dos numeros para ser division\n")
                d1 = int(input("Ingresar primer numero: "))
                d2 = int(input("Ingresar segundo numero: "))
                print(f"La division de {d1} / {d2} es = {d1 / d2}")

while True:
