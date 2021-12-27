# Crea al menos un objeto de cada subclase y añádelos a una lista llamada vehiculos.
# Realiza una función llamada catalogar() que reciba la lista de vehiculos y los recorra mostrando el nombre de su clase y sus atributos.
# Modifica la función catalogar() para que reciba un argumento optativo ruedas, haciendo que muestre únicamente los que su número de ruedas concuerde con el valor del argumento. También debe mostrar un mensaje "Se han encontrado {} vehículos con {} ruedas:" únicamente si se envía el argumento ruedas. Ponla a prueba con 0, 2 y 4 ruedas como valor.

# Mirar imgEjHerencia.png antes de realizar el ejercicio

class Vehiculo():
    
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
        
    def __str__(self):
        return "color {}, {} ruedas".format( self.color, self.ruedas )
        
        
class Coche(Vehiculo):
    
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)  # utilizamos super() sin self en lugar de Vehiculo
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        
    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)


class Camioneta(Coche):
    
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga
        
    def __str__(self):
        return super().__str__() + ", {} kg de carga".format(self.carga)
    

class Bicicleta(Vehiculo):
    
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
        
    def __str__(self):
        return super().__str__() + ", {}".format(self.tipo)
    

class Motocicleta(Bicicleta):
    
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        
    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada) 
    
# Catálogo de una lista    
def catalogar(vehiculos):
    for v in vehiculos:
        print(type(v).__name__, v) # Para recuperar el nombre de la clase de un objeto


# Catálogo de una lista por número de ruedas       
def catalogar(vehiculos, ruedas=None):
      
    # Primera pasada, mostrar recuento
    if ruedas != None:
        i = 0
        for v in vehiculos:
            if v.ruedas == ruedas: 
                i += 1
        print("\nSe han encontrado {} vehículos con {} ruedas:".format(i, ruedas))
    
    # Segunda pasada, mostrar vehículos
    for v in vehiculos:
        if ruedas == None:
            print(type(v).__name__, v) 
        else:
            if v.ruedas == ruedas:
                print(type(v).__name__, v)
                
        
lista = [
    Coche("azul", 4, 150, 1200),
    Camioneta("blanco", 4, 100, 1300, 1500),
    Bicicleta("verde", 2, "urbana"),
    Motocicleta("negro", 2, "deportiva", 180, 900)
]

catalogar(lista)
catalogar(lista, 0)
catalogar(lista, 2)
catalogar(lista, 4)