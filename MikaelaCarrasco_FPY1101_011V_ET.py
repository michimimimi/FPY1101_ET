import csv
import random

trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]

#definir funciones
def asignar_sueldos(trabajadores):
    nombre = input("Ingrese el nombre del trabajador: ") 
    sueldo = int(input("El sueldo del trabajador es: "))   
    while sueldo >300000 <2500000:            

        trabajadores.append({
        "Nombre" : nombre,
        "Sueldo" : sueldo
        })

def clasificar_sueldos(trabajadores):
    for trabajador in trabajadores:
        print(trabajador)

def ver_estadisticas():
    print()

def reporte_sueldos(trabajadores):
    nombre = input("Ingrese el nombre del trabajador: ")
    sueldo = int(input("Ingrese el sueldo del trabajador: "))
    descuento_salud = sueldo * 0.07
    descuento_afp = sueldo * 0.12
    sueldo_liquido = sueldo - descuento_salud - descuento_afp
    trabajadores.append({
        "Nombre" : nombre,
        "Sueldo base" : sueldo,
        "Descuento salud" : descuento_salud,
        "Descuento afp" : descuento_afp,
        "Sueldo liquido" : sueldo_liquido
    })
    print(f"El sueldo base del trabajador es: ",sueldo)
    print(f"El descuento de salud del trabajador es: ",descuento_salud)
    print(f"El descuento afp del trabajador es: ",descuento_afp)
    print(f"El sueldo liquido del trabajador es: ",sueldo_liquido)


def salir_programa(trabajadores):

    print("Finalizando el programa...""\n"
          "Desarrollado por Mikaela Carrasco""\n"
          "Rut 19.111.614-3""\n")
    
while True:
    print("Bienvenido al sistema de sueldos")
    print("1. Asignar sueldo")
    print("2. Clasificar sueldo")
    print("3. Ver estadisticas")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")

    opcion = int(input("Ingrese la opcion que desea: "))

    if opcion == 1:
        asignar_sueldos(trabajadores)
    elif opcion == 2:
        clasificar_sueldos(trabajadores)
    elif opcion == 3:
        ver_estadisticas()
    elif opcion == 4:
        reporte_sueldos(trabajadores)
    elif opcion == 5:
        salir_programa(trabajadores)
        break    
    else:
        print("Opcion invalida, intente nuevamente")

