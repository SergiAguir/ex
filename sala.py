class Sala:
    def __init__(self,nombreS,capacidad,precio):
        self.nombreS = nombreS
        self.capacidad = capacidad
        self.precio = precio
        self.acomulado = 0
        self.numReservas = 0
        self.reservas = {}
        self.finalizado = []

    def getNombre(self):
        return self.nombreS

    def getCapacidad(self):
        return self.capacidad

    def getPrecio(self):
        return self.precio

    def getAcomulado(self):
        return self.acomulado
    
    def getNumReservas(self):
        return self.numReservas

    def reservarSala(self,dni,fecha):
        existeFecha = False
        for dni in self.reservas:
            if fecha in self.reservas[dni]:
                existeFecha = True
        if existeFecha == True:
            return False
        else:
            if dni not in self.reservas.keys():
                self.reservas = {dni:[fecha]}
                self.numReservas+= 1
                return True
            else:
                self.reservas[dni].append(fecha)
                self.numReservas+= 1
                return True
    
    def confirmarReserva(self,dni,fecha):
        if dni in self.reservas.items():
            self.finalizado.append((dni,fecha))
            self.reservas[dni].pop(fecha)
            if self.reservas[dni][0] == "":
                del self.reservas[dni]
            self.acomulado+= self.precio
            return True
        else:
            return False

    def listarFinalizado(self):
        ordenar = sorted(self.finalizado, key=lambda sala : sala[1])
        lista = ""
        for clave,valor in ordenar:
            lista += "DNI: "+str(clave)+" Fecha: "+str(valor)+"\n"
        ordenar = sorted(lista, key=lambda sala : sala[1])
        return lista