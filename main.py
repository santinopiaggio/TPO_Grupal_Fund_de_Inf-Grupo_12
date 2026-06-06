import random
def op1(lst_pilotos,lst_numeros,lst_escuderias,lst_puntos,lst_promedios,lst_presupuestos,lst_abandonos):
    
#Carga de piloto
    piloto = input("Ingrese el nombre y apellido del piloto: ")
    while piloto == "" or len(piloto.split()) != 2:
        print ("Error. La variable no puede quedar vacia y debe tener 2 palabras")
        piloto = input("Ingrese el nombre y apellido del piloto: ")
    lst_pilotos.append(piloto)
    
#Carga de numero
    numero = int(input('Ingrese el numero identificatorio del monoplaza: '))
    while numero < 1:
        print ("Error. El numero identificatorio debe ser positivo")
        numero=int(input('ingrese el numero identificatorio del monoplaza'))
    lst_numeros.append(numero)
        
#Carga de escuderia
    escuderia = input('Ingrese a que escuderia pertence el pioloto: ')
    while escuderia == "":
        print ("Error. La variable no puede quedar vacia")
        escuderia = input('Ingrese a que escuderia pertence el pioloto: ')
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
        tiempo=float(input('Ingrese un valor positivo: '))
    lst_promedios.append(tiempo)
    
#Carga de presupuestos
    presupuesto = float(input('ingrese el presupuesto'))
    while presupuesto<0:
        print('Error el presupuesto debe ser positivo')
        presupuesto = float(input('Ingrese un presupuesto positivo: '))
    lst_presupuestos.append(presupuesto)
    
#Carga de cantidad de abandonos
    abandono = int(input("Abandonos del piloto: "))
    while abandono < 0:
        abandono = int(input("Error. Ingrese un numero entero positivo o cero: "))
    lst_abandonos.append(abandono)

    
# Eliminar piloto
def op2(lst_numeros, lst_puntos, lst_escuderias, lst_pilotos, lst_promedios, lst_presupuestos, lst_abandonos):
    indice = 0
    print(lst_numeros)
    numero_monoplaza = int(input("Ingrese el numero del piloto que desea eliminar: "))
    conf = False
    
    while numero_monoplaza not in lst_numeros:
        print(lst_numeros)
        numero_monoplaza = int(input("ERROR. Ingrese un numero valido: "))
    
    indice = lst_numeros.index(numero_monoplaza)

    
    if numero_monoplaza in lst_numeros and lst_puntos[indice] == 0:
        num = int(input('Estas seguro de que quieres eliminar al piloto? (Ingrese 1 si estas seguro, 2 si desea cancelar)'))
        while num != 1 and num != 2:
            num = int(input('Ingresa una opcion valida (Ingrese 1 si estas seguro, 2 si desea cancelar)'))
        if num == 1:
            conf = True
        if conf == True:
            lst_numeros.pop(indice)
            lst_puntos.pop(indice)
            lst_escuderias.pop(indice)
            lst_pilotos.pop(indice)
            lst_promedios.pop(indice)
            lst_presupuestos.pop(indice)
            lst_abandonos.pop(indice)
    else:
        print("El piloto tiene al menos un punto, para ser eliminado no debe tener ninguno.")
        

#Modificar tiempos o puntos promedio
def op3(lst_pilotos, lst_numeros, lst_puntos, lst_promedios):
    lst_numeros_str = [str(n) for n in lst_numeros]

    modificar = input("Nombre del piloto o numero del monoplaza: ")
    while modificar not in lst_pilotos and modificar not in lst_numeros_str:
        modificar = input("No se encuentra el dato ingresado. Ingrese un nombre o numero valido: ")

    print("[1] Modificar puntos acumulados.")
    print("[2] Modificar tiempo promedio por vuelta")
    print("[3] Volver al menu principal")
    decision = int(input("Seleccione una opcion: "))

    while decision > 3 or decision < 1:
        decision = int(input('Ingrese una opcion valida: '))

    if decision == 1:
        if modificar in lst_numeros_str:
            posicion = lst_numeros_str.index(modificar)
        else:
            posicion = lst_pilotos.index(modificar)
        puntos_mod = int(input("Ingrese la cantidad de puntos a agregar o quitar (positivo o negativo): "))
        lst_puntos[posicion] = lst_puntos[posicion] + puntos_mod
        if lst_puntos[posicion] < 0:
            lst_puntos[posicion] = 0
        print('El piloto tiene', lst_puntos[posicion], 'puntos.')

    elif decision == 2:
        if modificar in lst_numeros_str:
            posicion = lst_numeros_str.index(modificar)
        else:
            posicion = lst_pilotos.index(modificar)
        tiempo_mod = float(input("Nuevo tiempo promedio en segundos: "))
        while tiempo_mod < 0:
            tiempo_mod = float(input('Ingrese un valor positivo: '))
        lst_promedios[posicion] = tiempo_mod
        print('El nuevo tiempo promedio es', lst_promedios[posicion])

        
        
        
        
        
    

def main ():
    lst_pilotos = ['norris','colapinto','hamilton']
    lst_numeros = [16,2,321]
    lst_escuderias = ['ferrari','alpine','mclaren']
    lst_puntos = [26,10,30]
    lst_promedios = [87.90,89.15,90]
    lst_presupuestos = [2500,1350,3000]
    lst_abandonos = [2,0,4]   

    opcion = 0
    while opcion != 5:
        print("[1] Registrar piloto")
        print("[2] Eliminar piloto")
        print("[3] Modificar puntos o tiempo promedio")
        print("[4] Informe general")
        print("[5] Salir")
        opcion = int(input("Ingrese una opcion: "))

        if opcion == 1:
            op1(lst_pilotos, lst_numeros, lst_escuderias, lst_puntos, lst_promedios, lst_presupuestos, lst_abandonos)
        elif opcion == 2:
            op2(lst_numeros, lst_puntos, lst_escuderias, lst_pilotos, lst_promedios, lst_presupuestos, lst_abandonos)
        elif opcion == 3:
            op3(lst_pilotos, lst_numeros, lst_puntos, lst_promedios)
main()