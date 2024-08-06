import json
from datetime import datetime

# Clase base Venta
class Venta:
    def __init__(self, fecha, cliente, productos_vendidos):
        self.fecha = fecha
        self.cliente = cliente
        self.productos_vendidos = productos_vendidos

    def __str__(self):
        return f"Venta del {self.fecha} al cliente {self.cliente}"

# Clase derivada VentaOnline
class VentaOnline(Venta):
    def __init__(self, fecha, cliente, productos_vendidos, metodo_pago):
        super().__init__(fecha, cliente, productos_vendidos)
        self.metodo_pago = metodo_pago

    def __str__(self):
        return super().__str__() + f" - Método de pago: {self.metodo_pago}"

# Clase derivada VentaLocal
class VentaLocal(Venta):
    def __init__(self, fecha, cliente, productos_vendidos, empleado):
        super().__init__(fecha, cliente, productos_vendidos)
        self.empleado = empleado

    def __str__(self):
        return super().__str__() + f" - Empleado: {self.empleado}"

# Operaciones CRUD
class GestorVentas:
    def __init__(self, archivo_ventas):
        self.ventas = []
        self.archivo_ventas = archivo_ventas

    def crear_venta(self, venta):
        try:
            self.ventas.append(venta)
            self.guardar_ventas()
            print("Venta creada con éxito")
        except Exception as e:
            print(f"Error al crear venta: {e}")

    def leer_ventas(self):
        try:
            with open(self.archivo_ventas, 'r') as file:
                self.ventas = json.load(file)
            print("Ventas leídas con éxito")
        except Exception as e:
            print(f"Error al leer ventas: {e}")

    def actualizar_venta(self, venta):
        try:
            for v in self.ventas:
                if v.fecha == venta.fecha and v.cliente == venta.cliente:
                    v.productos_vendidos = venta.productos_vendidos
                    self.guardar_ventas()
                    print("Venta actualizada con éxito")
                    return
            print("Venta no encontrada")
        except Exception as e:
            print(f"Error al actualizar venta: {e}")

    def eliminar_venta(self, fecha, cliente):
        try:
            self.ventas = [v for v in self.ventas if not (v.fecha == fecha and v.cliente == cliente)]
            self.guardar_ventas()
            print("Venta eliminada con éxito")
        except Exception as e:
            print(f"Error al eliminar venta: {e}")

    def guardar_ventas(self):
        try:
            with open(self.archivo_ventas, 'w') as file:
                json.dump([v.__dict__ for v in self.ventas], file)
            print("Ventas guardadas con éxito")
        except Exception as e:
            print(f"Error al guardar ventas: {e}")

# Uso del sistema
gestor = GestorVentas("ventas.csv")
gestor.leer_ventas()

venta1 = VentaOnline("2024-07-29", "Juan", ["Producto 1", "Producto 2"], "Tarjeta de crédito")
gestor.crear_venta(venta1)

venta2 = VentaLocal("2024-07-29", "María", ["Producto 3", "Producto 4"], "Empleado 1")
gestor.crear_venta(venta2)

gestor.actualizar_venta(VentaOnline("2024-07-29", "Juan", ["Producto 1", "Producto 2", "Producto 5"], "Tarjeta de crédito"))

gestor.eliminar_venta("2024-07-29", "María")
