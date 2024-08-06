import os
import platform

from Desafio2 import (
    VentaOnline,
    VentaLocal,
    GestorVentas,
)

def limpiar_pantalla():
    ''' Limpiar la pantalla según el sistema operativo'''
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear') # Para Linux/Unix/MacOs
gestor = GestorVentas("ventas.csv")

while True:
    print("========== Menú de Gestión de Ventas ==========")
    print('1. Agregar Colaborador Ventas online')
    print('2. Agregar Colaborador Ventas local')
    print('3. Actualizar venta')
    print('4. Eliminar venta')
    print('5. Mostrar todas las ventas')
    print('6. Salir')
    print('======================================================')
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        # Agregar Colaborador Ventas online
        fecha = input("Ingrese la fecha: ")
        cliente = input("Ingrese el cliente: ")
        productos_vendidos = input("Ingrese los productos vendidos: ")
        metodo_pago = input("Ingrese el método de pago: ")
        venta = VentaOnline(fecha, cliente, productos_vendidos, metodo_pago)
        gestor.crear_venta(venta)
    elif opcion == '2':
        # Agregar Colaborador Ventas local
        fecha = input("Ingrese la fecha: ")
        cliente = input("Ingrese el cliente: ")
        productos_vendidos = input("Ingrese los productos vendidos: ")
        empleado = input("Ingrese el empleado: ")
        venta = VentaLocal(fecha, cliente, productos_vendidos, empleado)
        gestor.crear_venta(venta)
    elif opcion == '3':
        # Actualizar venta
        fecha = input("Ingrese la fecha: ")
        cliente = input("Ingrese el cliente: ")
        productos_vendidos = input("Ingrese los productos vendidos actualizados: ")
        venta = VentaOnline(fecha, cliente, productos_vendidos, "")
        gestor.actualizar_venta(venta)
    elif opcion == '4':
        # Eliminar venta
        fecha = input("Ingrese la fecha: ")
        cliente = input("Ingrese el cliente: ")
        gestor.eliminar_venta(fecha, cliente)
    elif opcion == '5':
        # Mostrar todas las ventas
        gestor.leer_ventas()
        for venta in gestor.ventas:
            print(venta)
    elif opcion == '6':
        # Salir
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")