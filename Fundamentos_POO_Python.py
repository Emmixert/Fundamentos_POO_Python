#Clase

class Coche():

#Atributo

    ruedas=4

#Metodo

    def desplazamiento(self):
        pass

#Objeto

miVehiculo=Coche()

#Polimorfismo

class Auto():
    ruedas=4
    def desplazamiento(self):
        print("El coche se esta desplazando sobre 4 ruedas")
class Moto():
    ruedas=2
    def desplazamiento(self):
        print("La moto se esta desplazando sobre 2 ruedas")

#Constructor

class Cachorro():
    def __init__(self, color, raza):
        self.color = color
        self.raza = raza
perrito = Cachorro("Marrón claro", "Golden retriever")

print("Este es un cachorro de la raza {} y es de color {}".format(perrito.raza, perrito.color))

#Encapsulacion

class Ejemplo():
    def publico(self):
        return "Soy un método público, a la vista de todo"
    def __privado(self):
        return "Soy un metodo privado, para ti no existo"
    
objeto = Ejemplo()

print(objeto.publico())
#print(objeto.__privado())

#Herencia

class Padre():
  
    caballo="negro"
    ojos="azules"
    def conducir_coche(self):
        print ("La persona sabe conducir coches")
class Hijo(Padre):
  
    def conducir_moto(self):
        print ("La persona sabe conducir moto")

persona=Hijo()

print(persona.caballo)
print(persona.ojos)

persona.conducir_coche()
persona.conducir_moto() 