#----------
#dada la lista de elemenetos numeros enteros
# -> 54 88 44 68 74 01
# vamos a multiplicar por 3 el valor

class Pila:
    def __init__(self):
        self._elementos = []
    def vacio(self): #verificamos si esta vacio
        return len(self._elementos)==0
        
    def push(self , dato): # agregamos elementos
        self._elementos.append(dato)
        print(f" Se apilo: {dato}")
        
    def pop(self): #borramos el ultimo elemento
        if self.vacio():
            print("lista vacia")
            return None
        elemento = self._elementos.pop()
        print(f"se saca el elemento {elemento}")
        return elemento
    #def mostrar_datos(self):
        # completar el mostrar
    def   tope (self): # con esta funcion mostramos el valor del ultimo elemento qu ingreso
        if self.vacio():
            print("lista vacia")
            return None
        return self._elementos[-1]
        #===========
  
  
  
pila = Pila()
pila.pop()
pila.push(1)
pila.push(55)
print(pila.tope())
pila.pop()
pila.pop()
pila.pop()