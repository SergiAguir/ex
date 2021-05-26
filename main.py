from sala import Sala
from controlador import Controdador
from datetime import datetime

con = Controdador()

while True:
    print("Salas disponibles: ",con.getSalas())
    print("1.- Anyadir Sala")
    print("2.- Reservar Sala")
    print("3.- Listar Finalaizadas")
    print("4.- Confirmar Reserva")
    print("5.- Salir")

    op = int(input("Elige una opcion: "))

    if op == 1:
        nombreS = con.generarNombre()

        while True:
            try:
                capacidad = int(input("Introduce la capacidad de la sala: "))

                if capacidad <1:
                    print("La capacidad tiene que ser minimo de 1 persona")
                else:
                    break
            except ValueError:
                print("Introduce un numero!!!!")

        while True:
            try:
                precio = int(input("Introduce el precio de la sala: "))

                if precio <= 0:
                    print("El precio de la sala no puede ser 0 o menor que 0")
                else:
                    break
            except ValueError:
                print("El precio es un numero!!")



        sala = Sala(nombreS,capacidad,precio)

        if con.anyadirSala(sala):
            print("La sala "+sala.getNombre()+ " se ha anyadido correctamente!!")
        else:
            print("Error al anyadir la sala!!")


    if op == 2:
        while True:
            nombre = input("Introduce el nombre de la sala: ")

            if con.comSala(nombre) == False:
                print("La sala no existe!!")
            else:
                break

        while True:
            dni = input("Introduce el dni: ")

            if con._check_dni(dni) == False:
                print("DNI incorrecto!!")
            else:
                break

        while True:
            fecha = input("Introduce una fecha (formato DD-MM-YYYY): ")

            if con.compFecha(fecha) == False:
                print("La fecha introducida no es correcta")
            else:
                break

        if con.reservarSala(nombre,dni,fecha) == False:
            print("Error al reservar la sala!!")
        else:
            print("Sala reservada correctamente")

    if op == 3:
        for i in con.listarFinalizado():
            print(i)

    if op == 4:
        while True:
            dni = input("Introduce el dni: ")

            if con._check_dni(dni) == False:
                print("DNI incorrecto!!")
            else:
                break

        while True:
            fecha = input("Introduce una fecha (formato DD-MM-YYYY): ")

            if con.compFecha(fecha) == False:
                print("La fecha introducida no es correcta")
            else:
                break

        while True:
            nombre = input("Introduce el nombre de la sala: ")

            if con.comSala(nombre) == False:
                print("La sala no existe!!")
            else:
                break

            if con.confirmarReserva(dni,fecha,nombre) == False:
                print("Error al confirmar la reserva")
            else:
                print("Reserva confirmadad correrctamente")

    if op == 5:
        print("Adios!!!")
        break