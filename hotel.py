'''Desarrolla:
Implementa un programa para gestionar las reservas de un hotel utilizando las características estudiadas de Programación Orientada a Objetos.
Lee detalladamente el enunciado para identificar cuándo debes usar clase abstracta, clase estática y atributos de clase. 
También puedes implementar propiedades.
Implementa las siguientes clases:
-Habitación : cuyas características sean la orientación, el precio y la disponibilidad. 
oHay habitaciones sencillas, dobles y suites. 
oTenemos una disponibilidad inicial para cada una de ellas.
oSe debe calcular el precio de cada una de ellas en base a las personas que las vayan a ocupar y un posible descuento a aplicar a elección del comercial.
oTanto el descuento como el precio son valores diferentes dependiendo de si la habitación es sencilla doble o suite.
oSe debe reducir la disponibilidad de las habitaciones cuando se haga una reserva.

-Cliente: de los cuales se guardará nombre, apellidos y DNI.
-Hotel: Gestionará todas las operaciones relacionadas con las reservas. 
oSe guardarán de forma independiente una lista de clientes y de reservas. 
oSe debe poder dar de alta un cliente y eliminarlo
oSe debe poder dar de alta una reserva, que tendrá asociada un tipo de habitación, un cliente (aunque la puedan ocupar más) y una fecha.
oPara reservar una habitación se debe comprobar previamente su disponibilidad y disminuirla.
oSe podrá cancelar una reserva buscando la misma por el nombre del cliente.'''
from abc import ABC, abstractmethod

# Clase abstracta
class Habitacion(ABC):
    @abstractmethod
    def calcular_precio_habitacion(self, n_personas):
        pass

# Clase concreta general para habitaciones
class HabitacionConcreta(Habitacion):
    def __init__(self, tipo, disponibilidad, precio_base, descuento):
        self.tipo = tipo
        self.disponibilidad = disponibilidad
        self.precio_base = precio_base
        self.descuento = descuento

    def calcular_precio_habitacion(self, n_personas):
        precio_total = self.precio_base * n_personas
        precio_final = precio_total - (precio_total * self.descuento / 100)
        return precio_final

    def reservar(self):
        if self.disponibilidad > 0:
            self.disponibilidad -= 1
            return True
        return False

    def __str__(self):
        return f"{self.tipo} - {self.disponibilidad} disponibles - Precio base: {self.precio_base}€"

# Clase Cliente
class Cliente:
    def __init__(self, nombre, dni, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni

    def __str__(self):
        return f'DATOS CLIENTE:\nNombre: {self.nombre}\nApellidos: {self.apellidos}\nDNI: {self.dni}'

# Clase Reserva
class Reserva:
    def __init__(self, cliente, habitacion, fecha):
        self.cliente = cliente
        self.habitacion = habitacion
        self.fecha = fecha

    def __str__(self):
        return f'DATOS RESERVA\n Cliente: {self.cliente.nombre}\nTipo de habitacion: {self.habitacion.tipo}\nFecha: {self.fecha}'

# Clase Hotel
class Hotel:
    clientes = []
    reservas = []
    habitaciones = {
        1: HabitacionConcreta("SENCILLA", 3, 40, 5),
        2: HabitacionConcreta("DOBLE", 2, 80, 10),
        3: HabitacionConcreta("SUITE", 1, 100, 15),
    }

    @staticmethod
    def buscar_cliente_nombre(nombre):
        for cliente in Hotel.clientes:
            if cliente.nombre == nombre:
                return cliente
        return None

    @staticmethod
    def dar_alta_cliente(cliente):
        Hotel.clientes.append(cliente)

    @staticmethod
    def eliminar_cliente(dni):
        Hotel.clientes = [c for c in Hotel.clientes if c.dni != dni]

    @staticmethod
    def reservar(nombre, tipo_hab, fecha, n_personas):
        cliente = Hotel.buscar_cliente_nombre(nombre)
        if not cliente:
            print("Cliente no encontrado.")
            return None

        habitacion = Hotel.habitaciones.get(tipo_hab)
        if not habitacion or not habitacion.reservar():
            print("Habitación no disponible.")
            return None

        reserva = Reserva(cliente, habitacion, fecha)
        Hotel.reservas.append(reserva)
        print("Reserva realizada con éxito.")
        return reserva

    @staticmethod
    def cancelar_reserva(nombre):
        Hotel.reservas = [r for r in Hotel.reservas if r.cliente.nombre != nombre]

# Main
def main():
    print(">>> HOTEL PARFAIT <<<")
    while True:
        print("\n1) Alta Cliente\n2) Baja Cliente\n3) Reservar\n4) Cancelar Reserva\n5) Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            apellidos = input("Apellidos: ")
            dni = input("DNI: ")
            Hotel.dar_alta_cliente(Cliente(nombre, dni, apellidos))
            print("Cliente añadido.")
        
        elif opcion == "2":
            dni = input("DNI del cliente a eliminar: ")
            Hotel.eliminar_cliente(dni)
            print("Cliente eliminado.")
        
        elif opcion == "3":
            nombre = input("Nombre del cliente: ")
            for idx, hab in Hotel.habitaciones.items():
                print(f"{idx}) {hab}")
            tipo = int(input("Selecciona tipo de habitación: "))
            fecha = input("Fecha (DD/MM/YYYY): ")
            n_personas = int(input("Número de personas: "))
            Hotel.reservar(nombre, tipo, fecha, n_personas)
        
        elif opcion == "4":
            nombre = input("Nombre del cliente: ")
            Hotel.cancelar_reserva(nombre)
            print("Reserva cancelada.")
        
        elif opcion == "5":
            print("Saliendo...")
            break

if __name__ == "__main__":
    main()



