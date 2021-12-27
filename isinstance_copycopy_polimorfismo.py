# Superclase
class Producto:
    def __init__(self,referencia,nombre,pvp,descripcion):
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion
        
    def __str__(self):
        return """\
REFERENCIA\t{}
NOMBRE\t\t{}
PVP\t\t{}
DESCRIPCIÓN\t{}""".format(self.referencia,self.nombre,self.pvp,self.descripcion)

# Subclase Adorno
class Adorno(Producto):
    pass

ad = Adorno(2034,"Vaso adornado",15,"Vaso de porcelana adornado con árboles")
print(ad)


#Subclase Alimento
class Alimento(Producto):
    productor = ""
    distribuidor = ""
    
    def __str__(self):
        return """\
REFERENCIA\t{}
NOMBRE\t\t{}
PVP\t\t{}
DESCRIPCIÓN\t{}
PRODUCTOR\t{}
DISTRIBUIDOR\t{}""".format(self.referencia,self.nombre,self.pvp,self.descripcion,self.productor,self.distribuidor)
        
    
al = Alimento(2035,"Botella de Aceite de Oliva Extra",5,"250 ML")
al.productor = "La Aceitera"
al.distribuidor = "Distribuciones SA"

print(al)


# Subclase Libro
class Libro(Producto):
    isbn = ""
    autor = ""
    
    def __str__(self):
        return """\
REFERENCIA\t{}
NOMBRE\t\t{}
PVP\t\t{}
DESCRIPCIÓN\t{}
ISBN\t\t{}
AUTOR\t\t{}""".format(self.referencia,self.nombre,self.pvp,self.descripcion,self.isbn,self.autor)
    
li = Libro(2036,"Cocina Mediterránea",9,"Recetas sanas y buenas")
li.isbn = "0-123456-78-9"
li.autor = "Doña Juana"

print(li)


# Lista de productos
productos = [ad, al]
productos.append(li)
#print(productos)
print("___________________")

for producto in productos:
    print(producto,"\n")

# Función isinstance 
for p in productos:
    if( isinstance(p, Adorno) ):
        print(p.referencia,p.nombre)
    elif( isinstance(p, Alimento) ):
        print(p.referencia,p.nombre,p.productor)
    elif( isinstance(p, Libro) ):
        print(p.referencia,p.nombre,p.isbn)        

# Para crear una copia 100% nueva de un objeto debemos utilizar el módulo copy:
import copy

copia_ad = copy.copy(ad)

# Polimorfismo
def rebajar_producto(p, rebaja):
    p.pvp = p.pvp - (p.pvp/100 * rebaja)