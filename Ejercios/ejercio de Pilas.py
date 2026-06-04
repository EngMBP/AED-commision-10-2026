#----------
#dada la lista de elemenetos numeros enteros
# -> 54 88 44 68 74 01
# vamos a multiplicar por 3 el valor

class Pila:
    def __init__(self):
        self._elementos = []
    def vacio(self):
        return len(self._elementos)==0
        
    def push(self , dato):
        self._elementos.append(dato)
        print(f" Se apilo: {dato}")
        
    def pop(self):
        if self.vacio():
            print("lista vacia")
            return None
        elemento = self._elementos.pop()
        print(f"se saca el elemento {elemento}")
        return elemento
    #def mostrar_datos(self):
        # completar el mostrar
        
#===========
        
pila = Pila()
pila.pop()
pila.push(1)
pila.push(55)
pila.pop()
pila.pop()
pila.pop()