#Atributos, clases, metodos y errores las escribo primera en mayuscula
#separandolas por _; para variables si en minuscula separando por _

class Nodo:
    def __init__(self, dato):
        self.Dato = dato
        self.Siguiente = None
        self.Anterior = None
        self.Orb_Anterior = None
        self.Orb_Siguiente = None

class Orbita:
    def __init__(self, capacidad = 3):
        #capacidad por defecto 3
        if capacidad <= 2:
            raise ValueError("La capacidad debe ser mayor a 2")
        self.Capacidad = capacidad
        self.Nodos = []
        self.Final = None
        #Debe iniciar con 3 nodos independiente de la capacidad
        #Asi se evita punteros en ambas direcciones
        #evito llamar a agregar nodo, ya que este reemplaza primero los
        #nodos None, falta manejar este caso para el contador
        for _ in range(3):
            nuevo = Nodo(None)
            if self.Nodos:
                primero = self.Nodos[0]
                ultimo = self.Final
                nuevo.Anterior = ultimo
                nuevo.Siguiente = primero
                ultimo.Siguiente = nuevo
                primero.Anterior = nuevo
            self.Nodos.append(nuevo)
            self.Final = nuevo

    def Agregar_Nodo(self, dato):
        for n in self.Nodos:
            if n.Dato is None:
                n.Dato = dato
                return True

        if len(self.Nodos) >= self.Capacidad:
            return False
        
        nuevo = Nodo(dato)
        # para el primer valor si se "rompe" la regla con los punteros
        if not self.Nodos:
            pass
        
        else:
            primero = self.Nodos[0]
            ultimo = self.Final
            nuevo.Anterior = ultimo
            nuevo.Siguiente = primero
            ultimo.Siguiente = nuevo
            primero.Anterior = nuevo
            
        self.Final = nuevo
        self.Nodos.append(nuevo)
        return True

    #le ponemos posicion por defecto?
    def Obtener_Nodo(self, posicion):
        if not self.Nodos:
            return None
        posicion = posicion % len(self.Nodos)
        return self.Nodos[posicion]

    def Mostrar(self):
        datos = [str(n.Dato) for n in self.Nodos]
        return "[" + ", ".join(datos) + "]"
    
#O lo llamamos simplemente Orbitas?
class Sistema_Orbitas:
    def __init__(self, capacidad = 3):
        #no pongo error ya que lo mandara al intentar crear la orbita
        self.Orbitas = []
        self.Capacidad = capacidad
        self.Contador = 0
        try:
            self.Crear_Orbita(capacidad)
        except ValueError as e:
            print("error al crear la orbita:", e)
            raise


    def Crear_Orbita(self, capacidad):
        nueva = Orbita(capacidad)
        
        if self.Orbitas:
            anterior = self.Orbitas[-1]
            anterior.Final.Orb_Siguiente = nueva.Nodos[0]
            nueva.Final.Orb_Anterior = anterior.Nodos[0]
        self.Orbitas.append(nueva)

    def Insertar(self, dato):
        actual = self.Orbitas[-1]
        if not actual.Agregar_Nodo(dato):
            # si se llena crea una nueva orbita con capcidad+1
            nueva_cap = actual.Capacidad + 1
            self.Crear_Orbita(nueva_cap)
            self.Orbitas[-1].Agregar_Nodo(dato)
        self.Contador += 1
   #---------------------------------------------------                      
 #Por el momento lo manejare con dos funciones luego creo una sola con
# las excepciones necesarias
    def Obtener_Por_Id(self, id_nodo):
        if id_nodo < 1 or id_nodo > self.Contador:
            return None
        contador = 0
        for o in self.Orbitas:
            for n in o.Nodos:
                contador += 1
                if contador == id_nodo:
                    return n
        return None

    def Obtener(self, num_orbita, pos):
        if num_orbita < 0 or num_orbita >= len(self.Orbitas):
            return None  #o lanzo error?
        orb = self.Orbitas[num_orbita]
        return orb.Obtener_Nodo(pos)
#------------------------------------------------------------------
    
    def Eliminar_Orbita(self, num_orbita):
        if num_orbita < 0 or num_orbita >= len(self.Orbitas):
            return
        pass #falta por implementar, luego pienso como manejar el cambio
                #con el contador
    
 #Pienso hacerlo tambien por id_nodo o numero de orbita y posicion
    
#por cierto manejo un valor por defecto, osea que si no se pasa parrametro
#que elimine el ultimo de la ultima orbita o asi?
    
#otra cosa este metodo aun falta corregirle para evitar que pueda dejar
#orbitas con menos de 3 elementos
    def Eliminar_Nodo(self, id_nodo):
        nodo_obj = self.Obtener_Por_Id(id_nodo)
        if not nodo_obj:
            return False
        for o in self.Orbitas:
            if nodo_obj in o.Nodos:
                o.Nodos.remove(nodo_obj)
                if o.Nodos:
                    o.Final = o.Nodos[-1]
                else:
                    o.Final = None
                self.Contador -= 1
                return True
        return False

    def Mostrar(self):
        texto = ""
        for i, o in enumerate(self.Orbitas):
            texto += f"orbita {i} (cap {o.Capacidad}): {o.Mostrar()}\n"
        return texto.strip()



# ------------------ prueba ------------------
sistema = Sistema_Orbitas(3)
    
for i in range(9):
    sistema.Insertar(i)
    
print("estado inicia del sistema:")
print(sistema.Mostrar())
print("---------------------------------------------------")
    
# obtener un nodo por id
nodo_5 = sistema.Obtener_Por_Id(5)
print("dato:", nodo_5.Dato)

    
# obtener un nodo por orbita y posicion
nodo_2_1 = sistema.Obtener(2, 1)
print("dato del nodo 2-1:", nodo_2_1.Dato)
print("--------------------------------------------")
    
# eliminando un nodo
print("eliminando nodo 3...")
if sistema.Eliminar_Nodo(3):
    print("nodo eliminado correctamente")
print("estado despues de eliminar nodo 3:")
print(sistema.Mostrar())
print("-------------------------------------------------")
    

 
