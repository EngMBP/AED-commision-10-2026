class Cola:
    def __init__(self):
        self._elementos = []
    def vacio(self): #verificamos si esta vacio
        return len(self._elementos)==0
        
    def encolar(self , dato): # agregamos elementos
        self._elementos.append(dato)
        print(f" Se agrego: {dato}")
        
    def desencolar(self): #borramos el ultimo elemento
        if self.vacio():
            print("lista vacia")
            return None
        elemento = self._elementos.pop(0)
        print(f"se saca el elemento {elemento}")
        return elemento
    #def mostrar_datos(self):
        # completar el mostrar
    def primer_elemento (self): # con esta funcion mostramos el valor del ultimo elemento qu ingreso
        if self.vacio():
            print("lista vacia")
            return None
        return self._elementos[0]
        #===========
cola = Cola()
cola.encolar(10)
cola.encolar(55)
cola.encolar(85)
print(cola.primer_elemento())