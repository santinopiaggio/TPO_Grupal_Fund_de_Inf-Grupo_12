# En este archivo se encuentra el programa principal, con el menu y las funciones para cada opcion del menu. 
# Se importan las funciones del archoivo funciones.pypara ser utilizadas en este programa.

from funciones import op1, op2, op3, op4

# Programa principal, con el menu y las funciones para cada opcion del menu. 
def main():
    lst_pilotos = []
    lst_numeros = []
    lst_escuderias = []
    lst_puntos = []
    lst_promedios = []
    lst_presupuestos = []
    lst_abandonos = []   
    opcion = 0

    while opcion != 5:
        print("==================================================")
        print("Bienvenido al sistema de gestion de pilotos de F1")
        print("==================================================")
        print("[1] Registrar piloto")
        print("[2] Eliminar piloto")
        print("[3] Modificar puntos o tiempo promedio")
        print("[4] Informe general")
        print("[5] Salir")
        print("==================================================")
        
        opcion = int(input("Ingrese una opcion: "))

        if opcion == 1:
            op1(lst_pilotos, lst_numeros, lst_escuderias, lst_puntos, lst_promedios, lst_presupuestos, lst_abandonos)
        elif opcion == 2:
            op2(lst_numeros, lst_puntos, lst_escuderias, lst_pilotos, lst_promedios, lst_presupuestos, lst_abandonos)
        elif opcion == 3:
            op3(lst_pilotos, lst_numeros, lst_puntos, lst_promedios)
        elif opcion == 4:
            op4(lst_pilotos, lst_numeros, lst_escuderias, lst_puntos, lst_promedios, lst_presupuestos, lst_abandonos)

main()