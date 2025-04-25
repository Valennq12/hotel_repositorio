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

class Habitacion(ABC):
        

    @abstractmethod
    def calcular_precio_habitacion(self):
        pass


class HabitacionesSencillas(Habitacion):
    disponibilidad = 3
    PRECIO_BASE = 40
    DESCUENTO = 5


class HabitacionesDobles(Habitacion):
    disponibilidad = 2
    PRECIO_BASE = 80
    DESCUENTO = 10

class HabitacionesSuites(Habitacion):
    disponibilidad = 1
    PRECIO_BASE = 100
    DESCUENTO = 10

class Cliente: 
# -Cliente: de los cuales se guardará nombre, apellidos y DNI.
    def __init__(self, nombre, dni, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos 
        self.dni = dni 

    def __str__(self):
        return f'DATOS CLIENTE:\nNombre: {self.nombre}\nApellidos: {self.apellidos}\nDNI: {self.dni}'

class Reserva:
    def __init__(self,cliente, habitacion, fecha):
        self.cliente = cliente
        self.habitacion = habitacion
        self.fecha = fecha 

    def __str__(self):
        return f'DATOS RESERVA\n Cliente: {self.cliente}\nTipo de habitacion: {self.habitacion}\nFecha: {self.fecha}'


class Hotel:
#     -Hotel: Gestionará todas las operaciones relacionadas con las reservas. 
# oSe guardarán de forma independiente una lista de clientes y de reservas. 
# oSe debe poder dar de alta un cliente y eliminarlo
# oSe debe poder dar de alta una reserva, que tendrá asociada un tipo de habitación, un cliente (aunque la puedan ocupar más) y una fecha.
# oPara reservar una habitación se debe comprobar previamente su disponibilidad y disminuirla.
# oSe podrá cancelar una reserva buscando la misma por el nombre del cliente.
    clientes = []
    reservas = []

    @staticmethod
    def buscar_cliente_nombre(nombre):
        for cliente in Hotel.clientes:
            if cliente == nombre:
                return True
        return False

    @staticmethod # oSe debe poder dar de alta un cliente y eliminarlo
    def dar_alta_cliente(datos_cliente):
        Hotel.clientes.append(datos_cliente)

    @staticmethod # oSe debe poder dar de alta un cliente y eliminarlo
    def eliminar_cliente(dni_cliente):
        Hotel.clientes.remove(dni_cliente)

    @staticmethod # oSe debe poder dar de alta una reserva, que tendrá asociada un tipo de habitación, un cliente (aunque la puedan ocupar más) y una fecha.
    def reservar():
        habitaciones = ['HABITACION SENCILLA', 'HABITACION DOBLE','HABITACION SUITE']
        for indice, elemento in enumerate(habitaciones,start = 1):
            print(f'{indice}) {elemento}')
        habitacion = int(input('Tipo de habitacion: '))
                #VALIDAMOS SI HAY DISPONIBILIDAD
        if habitacion == 1 :
            habitacion = HabitacionesSencillas
            if Hotel.comprobar_disponibilidad(HabitacionesSencillas) :
                return True
            else:
                print('No hay disponibilidad para esta habitacion.')
                return False
        elif habitacion == 2 :
            habitacion = HabitacionesDobles
            if Hotel.comprobar_disponibilidad(HabitacionesDobles) :
                return True
            else:
                print('No hay disponibilidad para esta habitacion.')
                return False
        elif habitacion == 3:
            habitacion = HabitacionesSuites
            if Hotel.comprobar_disponibilidad(HabitacionesSuites) :
                return True
            else:
                print('No hay disponibilidad para esta habitacion.')
                return False
        nombre = input('Nombre cliente: ')
        if Hotel.buscar_cliente_nombre(nombre):
            return True
        else:
            print('Cliente no encontrado.')
            return False
        fecha = input('Dime la fecha con el siguiente formato: DD/MM/YYYY: ')
        n_personas = int(input('Numero de personas que la van a ocupar: '))
        return Habitacion, 


    @staticmethod
    def comprobar_disponibilidad(tipo_habitacion):
        if tipo_habitacion.disponibilidad > 0 :
            return True
        else :
            return False

    @staticmethod # Se podrá cancelar una reserva buscando la misma por el nombre del cliente.
    def cancelar_reserva():
        pass


def main():
    print('>>> HOTEL PARFAIT. GESTIONES CLIENTES Y RESERVAS <<<')
    menu = ['ALTA CLIENTES', 'BAJA CLIENTES', 'RESERVA HABITACION', 'CANCELAR RESERVA', 'LISTADO CLIENTES', 'LISTADO RESERVAS', 'SALIR']

    while True:
        for indice, elemento in enumerate(menu, strat=1) :
            print(f'{indice}) {elemento}')

        accion = input('Elige: ')
        if not accion.isdigit() :
            print('DEBES INTRODUCIR UN NUMERO (1-7)')
            return False
        
        match accion :
            case '1':
                #ALTA CLIENTES
                nombre = input('Nombre: ')
                dni = input('DNI: ')
                apellidos = input('Apellidos: ')
                datos_cliente = Cliente(nombre,dni,apellidos)
                Hotel.dar_alta_cliente(datos_cliente)
                print('Cliente añadido.\nBienvenido.')

            case '2':
                #BAJA CLIENTES con dni
                dni = input('Nombre cliente: ')
                for cliente in Hotel.clientes :
                    if isinstance(dni, Cliente):
                        Hotel.clientes.remove(cliente)
                        print('Cliente borrado con éxito.')
                
            case '3':
                #RESERVA HABITACION Para reservar una habitación se debe comprobar previamente su disponibilidad y disminuirla.
                habitaciones = ['HABITACION SENCILLA', 'HABITACION DOBLE','HABITACION SUITE']
                for indice, elemento in enumerate(habitaciones,start = 1):
                    print(f'{indice}) {elemento}')

                habitacion = int(input('Tipo de habitacion: '))
                #VALIDAMOS SI HAY DISPONIBILIDAD
                if habitacion == 1 :
                    if Hotel.comprobar_disponibilidad(HabitacionesSencillas) :
                        return True
                    else:
                        print('No hay disponibilidad para esta habitacion.')
                        return False
                elif habitacion == 2 :
                    if Hotel.comprobar_disponibilidad(HabitacionesDobles) :
                        return True
                    else:
                        print('No hay disponibilidad para esta habitacion.')
                        return False
                elif habitacion == 3:
                    if Hotel.comprobar_disponibilidad(HabitacionesSuites) :
                        return True
                    else:
                        print('No hay disponibilidad para esta habitacion.')
                        return False
                
                nombre = input('Nombre cliente: ')
                if Hotel.buscar_cliente_nombre(nombre):
                    return True
                else:
                    print('Cliente no encontrado.')

                fecha = input('Dime la fecha con el siguiente formato: DD/MM/YYYY: ')


            case '4':
                #CANCELAR RESERVA
                pass
            case '5':
                #LISTADO CLIENTES
                pass
            case '6':
                #LISTADO RESERVAs
                pass
            case '7':
                #SALIR
                print('Saliendo...')
                break


