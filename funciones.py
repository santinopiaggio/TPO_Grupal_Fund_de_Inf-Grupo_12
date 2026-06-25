# En este archivo se definen las funciones que se utilizan en el programa principal.

# op 1 - Agustin Carbone y Agustin Poletti
# op 2 - Dante Prividera y Santino Piaggio
# op 3 - Gonzalo Rodriguez y Agustin Poletti
# op 4 - Agustin Carbone, Dante Prividera, Gonzalo Rodriguez y Santino Piaggio
# crear_matriz - Gonzalo Rodriguez y Santino Piaggio
# imprimir_matriz - Agustin Poletti y Santino Piaggio
   
# Funcion para cargar un nuevo piloto, con sus datos correspondientes, a las listas.
def op1(lst_pilotos,lst_numeros,lst_escuderias,lst_puntos,lst_promedios,lst_presupuestos,lst_abandonos):
#Carga de piloto
    piloto = input("Ingrese el nombre y apellido del piloto: ")
    while piloto == "" or len(piloto.split()) != 2 or piloto in lst_pilotos:
        print ("Error. La variable no puede quedar vacia, debe tener 2 palabras y/o ya existe")
        piloto = input("Ingrese el nombre y apellido del piloto: ")
    lst_pilotos.append(piloto)

#Carga de numero
    print(f"Numeros de monoplaza disponibles: {lst_numeros}")
    numero = int(input("Ingrese el numero identificatorio del monoplaza: "))
    while numero < 1 or numero in lst_numeros:
        print(f"Numeros de monoplaza disponibles: {lst_numeros}")
        print ("Error. El numero identificatorio debe ser positivo y/o ya existe")
        numero = int(input("Ingrese el numero identificatorio del monoplaza: "))
    lst_numeros.append(numero)

#Carga de escuderia
    print(f"Escuderias ya creadas. {lst_escuderias}. Podes seleccionar alguna o crear otra!")
    escuderia = input("Ingrese a que escuderia pertence el pioloto: ")
    while escuderia == "":
        print(f"Escuderias ya creadas. {lst_escuderias}. Podes seleccionar alguna o crear otra!")
        print ("Error. La variable no puede quedar vacia")
        escuderia = input("Ingrese a que escuderia pertence el pioloto: ")
    lst_escuderias.append(escuderia)  

#Carga de puntos acumulados
    punto = int(input("Ingrese los puntos del piloto: "))
    while punto < 0:
        punto = int(input("Error. Ingrese un valor entero positivo o cero: "))
    lst_puntos.append(punto)
    
#Carga de tiempo promedio 
    tiempo = float(input("Ingrese el tiempo promedio por vuelta: "))
    while tiempo < 0:
        print ("Error. El tiempo no puede ser negativo")
        tiempo=float(input("Ingrese un valor positivo: "))
    lst_promedios.append(tiempo)
    
#Carga de presupuestos
    presupuesto = float(input("Ingrese el presupuesto: "))
    while presupuesto<0:
        print("Error el presupuesto debe ser positivo")
        presupuesto = float(input("Ingrese un presupuesto positivo: "))
    lst_presupuestos.append(presupuesto)
    
#Carga de cantidad de abandonos
    abandono = int(input("Abandonos del piloto: "))
    while abandono < 0:
        abandono = int(input("Error. Ingrese un numero entero positivo o cero: "))
    lst_abandonos.append(abandono)

    
# Eliminar piloto
def op2(lst_numeros, lst_puntos, lst_escuderias, lst_pilotos, lst_promedios, lst_presupuestos, lst_abandonos):
    indice = 0
    
    while len(lst_pilotos) == 0:
        print("Error: Aun no hay valores ingresados")
        return 
    print(f"Numeros de monoplaza disponibles: {lst_numeros}")
    
    numero_monoplaza = int(input("Ingrese el numero del piloto que desea eliminar: "))
    conf = False

    while numero_monoplaza not in lst_numeros:
        print(f"Numeros de monoplaza disponibles: {lst_numeros}")
        numero_monoplaza = int(input("ERROR. Ingrese un numero valido: "))
    
    indice = lst_numeros.index(numero_monoplaza)

    if numero_monoplaza in lst_numeros and lst_puntos[indice] == 0:
        num = int(input(f"Estas seguro de que quieres eliminar al piloto {lst_pilotos[indice]}? (Ingrese 1 si estas seguro, 2 si desea cancelar): "))
        while num != 1 and num != 2:
            num = int(input("Ingresa una opcion valida (Ingrese 1 si estas seguro, 2 si desea cancelar): "))
        if num == 1:
            conf = True
        if conf == True:
            print("==================================================")
            print(f"Se ha eliminado correctamente {lst_pilotos[indice]}")
            lst_numeros.pop(indice)
            lst_puntos.pop(indice)
            lst_escuderias.pop(indice)
            lst_pilotos.pop(indice)
            lst_promedios.pop(indice)
            lst_presupuestos.pop(indice)
            lst_abandonos.pop(indice)
        if num == 2:
            print("==================================================")
            print(f"Accion cancelada, volviendo al menu...")
    else:
        print("El piloto tiene al menos un punto, para ser eliminado no debe tener ninguno. Volviendo al menu...")


# Modificar tiempos o puntos promedio
def op3(lst_pilotos, lst_numeros, lst_puntos, lst_promedios):
    lst_numeros_str = [str(n) for n in lst_numeros]
    while len(lst_pilotos) == 0:
        print("Error: Aun no hay valores ingresados")
        return
    modificar = input("Nombre del piloto o numero del monoplaza: ")
    while modificar not in lst_pilotos and modificar not in lst_numeros_str:
        modificar = input("No se encuentra el dato ingresado. Ingrese un nombre o numero valido: ")

    print("[1] Modificar puntos acumulados.")
    print("[2] Modificar tiempo promedio por vuelta")
    print("[3] Volver al menu principal")
    decision = int(input("Seleccione una opcion: "))

    while decision > 3 or decision < 1:
        decision = int(input("Ingrese una opcion valida: "))

    if decision == 1:
        if modificar in lst_numeros_str:
            posicion = lst_numeros_str.index(modificar)
        else:
            posicion = lst_pilotos.index(modificar)
        puntos_mod = int(input("Ingrese la cantidad de puntos a agregar o quitar (positivo o negativo): "))
        lst_puntos[posicion] = lst_puntos[posicion] + puntos_mod
        if lst_puntos[posicion] < 0:
            lst_puntos[posicion] = 0
        print(f"El piloto tiene {lst_puntos[posicion]} puntos.")

    elif decision == 2:
        if modificar in lst_numeros_str:
            posicion = lst_numeros_str.index(modificar)
        else:
            posicion = lst_pilotos.index(modificar)
        tiempo_mod = float(input("Nuevo tiempo promedio en segundos: "))
        while tiempo_mod < 0:
            tiempo_mod = float(input("Ingrese un valor positivo: "))
        lst_promedios[posicion] = tiempo_mod
        print(f"El nuevo tiempo promedio es {lst_promedios[posicion]} segundos")


# Funcion para crear la matriz de opcion 4 
def crear_matriz(lst_pilotos, lst_numeros, lst_escuderias, lst_puntos, lst_promedios, lst_presupuestos, lst_abandonos):
    matriz = []

    for f in range(len(lst_pilotos)):
        fila = [
            lst_pilotos[f],
            lst_numeros[f],
            lst_escuderias[f],
            lst_puntos[f],
            lst_promedios[f],
            lst_presupuestos[f],
            lst_abandonos[f]
        ]

        matriz.append(fila)

    return matriz

# funcion para imprimir la matriz de la opcion 4
def imprimir_matriz(matriz):
    filas = len(matriz)

    if filas == 0:
        print("No hay datos para mostrar.")
        return
    
    titulos = ["Piloto", "Numero", "Escuderia", "Puntos", "Promedio", "Presupuesto", "Abandonos"]

    for titulo in titulos:
        print("%15s" % titulo, end="")
    print()

    print("-" * 105)

    columnas = len(matriz[0])

    for f in range(filas):
        for c in range(columnas):
            print("%15s" % str(matriz[f][c]), end="")
        print()

# Informe general de los pilotos ordenados.
def op4(lst_pilotos, lst_numeros, lst_escuderias, lst_puntos, lst_promedios, lst_presupuestos, lst_abandonos):

    for recorrido in range(1, len(lst_puntos)):
        for i in range(len(lst_puntos)-recorrido):
            if lst_puntos[i] < lst_puntos[i+1]:
                aux = lst_pilotos[i]
                lst_pilotos[i] = lst_pilotos[i+1]
                lst_pilotos[i+1] = aux

                aux2 = lst_puntos[i]
                lst_puntos[i] = lst_puntos[i+1]
                lst_puntos[i+1] = aux2

                aux3 = lst_numeros[i]
                lst_numeros[i] = lst_numeros[i+1]
                lst_numeros[i+1] = aux3

                aux4 = lst_presupuestos[i]
                lst_presupuestos[i] = lst_presupuestos[i+1]
                lst_presupuestos[i+1] = aux4

                aux5= lst_promedios[i]
                lst_promedios[i] = lst_promedios[i+1]
                lst_promedios[i+1] = aux5

                aux6 = lst_escuderias[i]
                lst_escuderias[i] = lst_escuderias[i+1]
                lst_escuderias[i+1] = aux6

                aux7 = lst_abandonos[i]
                lst_abandonos[i] = lst_abandonos[i+1]
                lst_abandonos[i+1] = aux7
                
            elif lst_puntos[i] == lst_puntos[i+1]:
                if lst_promedios[i] > lst_promedios[i+1]:
                    aux = lst_pilotos[i]
                    lst_pilotos[i] = lst_pilotos[i+1]
                    lst_pilotos[i+1] = aux

                    aux2 = lst_puntos[i]
                    lst_puntos[i] = lst_puntos[i+1]
                    lst_puntos[i+1] = aux2

                    aux3 = lst_numeros[i]
                    lst_numeros[i] = lst_numeros[i+1]
                    lst_numeros[i+1] = aux3

                    aux4 = lst_presupuestos[i]
                    lst_presupuestos[i] = lst_presupuestos[i+1]
                    lst_presupuestos[i+1] = aux4

                    aux5= lst_promedios[i]
                    lst_promedios[i] = lst_promedios[i+1]
                    lst_promedios[i+1] = aux5

                    aux6 = lst_escuderias[i]
                    lst_escuderias[i] = lst_escuderias[i+1]
                    lst_escuderias[i+1] = aux6

                    aux7 = lst_abandonos[i]
                    lst_abandonos[i] = lst_abandonos[i+1]
                    lst_abandonos[i+1] = aux7

    m = crear_matriz(
    lst_pilotos,
    lst_numeros,
    lst_escuderias,
    lst_puntos,
    lst_promedios,
    lst_presupuestos,
    lst_abandonos
    )

    imprimir_matriz(m)