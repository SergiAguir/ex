from sala import Sala
import random
import string
from datetime import datetime


class Controdador:
    def __init__(self):
        self.listaSalas =  {}
        self.numSala = 1

    def getSalas(self):
        return len(self.listaSalas)

    def generarNombre(self):
        letra1 = random.choice(string.ascii_letters)
        letra2 = random.choice(string.ascii_letters)
        letra3 = random.choice(string.ascii_letters)

        nombre = letra1 + letra2 +letra3 + str(self.numSala)
        self.numSala+=1
        return nombre

    def anyadirSala(self,sala):
        if sala.getNombre() not in self.listaSalas:
            self.listaSalas[sala.getNombre()] = sala
            return True
        else:
            return False

    def comSala(self,nombre):
        if nombre in self.listaSalas:
            return True
        return False

    def _check_dni(self,dni):
        letras = ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
        
        letraDNI = dni[-1].upper()
        numDNI = dni[:-1]

        if (letraDNI.isalpha() == False):
            return False
        if len(dni) != 9:
            return False
        else:
            letraCalculada = letras[int(numDNI)%23]
            if (letraDNI != letraCalculada):
                return False
        return True

    def compFecha(self,fecha):
        if datetime.strptime(fecha, '%d-%m-%Y'):
            return True
        else:
            return False

    def reservarSala(self,nombre,dni,fecha):
        if self.listaSalas[nombre].reservarSala(dni,fecha):
            return True
        else:
            return False


    def confirmarReserva(self,dni,fecha,nombre):
        if self.listaSalas[nombre].confirmarReserva(dni,fecha):
            return True
        else:
            return False

    def listarFinalizado(self):
        lista = []
        for clave,valor in self.listaSalas.items():
            lista.append(str(clave)+" "+valor.listarFinalizado())
        return lista