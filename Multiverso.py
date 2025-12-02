#Atributos, clases, metodos y errores las escribo primera en mayuscula
#separandolas por _; para variables si en minuscula separando por _

class Nodo:
    def __init__(self, dato=None, vacio=True):
        self.Dato = dato
        self.Vacio = vacio
        self.Siguiente = None
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
        self.Tamaño = 0 
        #Debe iniciar con 3 nodos independiente de la capacidad
        #Asi se evita punteros en ambas direcciones
        for i in range(3):
             self.Agregar_Nodo(None, True)

    def Agregar_Nodo(self, dato, vacio=False):
        if not vacio:
            for n in self.Nodos:
                if n.Vacio:
                    n.Dato = dato
                    n.Vacio = False
                    return True
                
        if len(self.Nodos) >= self.Capacidad:
                return False
        nuevo = Nodo(dato, vacio)
        if not self.Nodos:
            pass
        
        else:
            primero = self.Nodos[0]
            ultimo = self.Final
            nuevo.Siguiente = primero
            ultimo.Siguiente = nuevo

        self.Final = nuevo
        self.Nodos.append(nuevo)
        self.Tamaño = len(self.Nodos)
        return True

    def Obtener_Nodo(self, posicion):
        if not self.Nodos:
            return None
        posicion = posicion % len(self.Nodos)
        return self.Nodos[posicion]

    def Mostrar(self):
        datos = [str(n.Dato) for n in self.Nodos]
        return "[" + ", ".join(datos) + "]"
    
class Sistema_Orbitas:
    def __init__(self, capacidad = 3):
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
        if not self.Orbitas:
            self.Crear_Orbita(self.Capacidad)
        
        actual = self.Orbitas[-1]
        if not actual.Agregar_Nodo(dato):
            # si se llena crea una nueva orbita con capcidad+1
            nueva_cap = actual.Capacidad + 1
            self.Crear_Orbita(nueva_cap)
            self.Orbitas[-1].Agregar_Nodo(dato)
        self.Contador += 1
   #---------------------------------------------------                      
    def Obtener_Id(self, num_orbita, posicion):
        if num_orbita < 0 or num_orbita >= len(self.Orbitas):
            raise ValueError("el número de órbita no es válido")

        orb = self.Orbitas[num_orbita]
        if not orb.Nodos:
            raise ValueError("la órbita está vacía")

        indice = posicion % len(orb.Nodos)

        id_base = sum(len(o.Nodos) for o in self.Orbitas[:num_orbita])
        id_final = id_base + indice + 1  # +1 para que empiece en 1
        return id_final
        


    def Convertir_Id(self, id_nodo):
        if id_nodo < 1 or id_nodo > self.Contador:
            raise ValueError("el id indicado no existe")

        acumulado = 0
        for i, orb in enumerate(self.Orbitas):
            if id_nodo <= acumulado + len(orb.Nodos):
                pos = id_nodo - acumulado - 1
                return i, pos
            acumulado += len(orb.Nodos)
        raise ValueError("id fuera de rango")


    def Obtener(self, *args):
        if len(args) == 1:
            id_nodo = args[0]
            num_orbita, pos = self.Convertir_Id(id_nodo)
            return self.Obtener(num_orbita, pos)

        elif len(args) == 2:
            num_orbita, pos = args
            if num_orbita < 0 or num_orbita >= len(self.Orbitas):
                raise ValueError("el número de órbita no es válido")
            orb = self.Orbitas[num_orbita]
            return orb.Obtener_Nodo(pos)

        else:
            raise ValueError("parámetros inválidos")
        
#------------------------------------------------------------------
    
    def Eliminar_Orbita(self, num_orbita=-1):
        if not self.Orbitas:
            return False  

        total_orbitas = len(self.Orbitas)
    
        if num_orbita < 0:#si pasan un negativo simplemente borro la ultima
            num_orbita = total_orbitas - 1

        if num_orbita >= total_orbitas:
            raise ValueError("el número de órbita no es válido")

        # actualiza punteros
        if num_orbita > 0:
            orb_anterior = self.Orbitas[num_orbita - 1]
            orb_anterior.Final.Orb_Siguiente = None

        # eliminar las orbitas siguientes
        for orb in self.Orbitas[num_orbita:]:
            self.Contador -= len(orb.Nodos)  # descontar todos los nodos
        self.Orbitas = self.Orbitas[:num_orbita]
        return True
    
    def Eliminar_Nodo(self, id_nodo):
        num_orbita, pos = self.Convertir_Id(id_nodo)
        orb = self.Orbitas[num_orbita]
        nodo = orb.Obtener_Nodo(pos)

        # si tiene 3 o menos nodos solo lo marcamos vacio
        if len(orb.Nodos) <= 3:
            if all(n.Vacio for n in orb.Nodos[:3]):
                return "la orbita está vacía"
            nodo.Dato = None
            nodo.Vacio = True
            #no toca mover los punteros ya que solo cambie dato y vacio
            return True

        # si hay más de 3 nodos elimino normal
        orb.Nodos.pop(pos)
        orb.Final = orb.Nodos[-1] if orb.Nodos else None
        orb.Tamaño = len(orb.Nodos)

        # actualizo punteros de la orbita
        if orb.Nodos:
            for i, n in enumerate(orb.Nodos):
                n.Siguiente = orb.Nodos[(i + 1) % len(orb.Nodos)]
            orb.Final = orb.Nodos[-1]

        # punteros hacia otras orbitas
        if num_orbita > 0:
            orb_anterior = self.Orbitas[num_orbita - 1]
            orb.Nodos[0].Orb_Anterior = orb_anterior.Final
            orb_anterior.Final.Orb_Siguiente = orb.Nodos[0]
        else:
            orb.Nodos[0].Orb_Anterior = None

        if num_orbita + 1 < len(self.Orbitas):
            orb_siguiente = self.Orbitas[num_orbita + 1]
            orb.Final.Orb_Siguiente = orb_siguiente.Nodos[0]
            orb_siguiente.Nodos[0].Orb_Anterior = orb.Final
        else:
            orb.Final.Orb_Siguiente = None

        self.Contador -= 1
        return True
    
    def Mostrar(self):
        texto = ""
        for i, o in enumerate(self.Orbitas):
            texto += f"orbita {i} (cap {o.Capacidad}): {o.Mostrar()}\n"
        return texto.strip()

    def Recorrer(self, id_origen, id_destino, impresion=True):
        origen = self.Obtener(id_origen)
        destino = self.Obtener(id_destino)

        recorrido = []
        nodo_actual = origen
        avanzar = id_destino > id_origen

        while True:
            if nodo_actual == origen or nodo_actual == destino:
                recorrido.append(f"[{nodo_actual.Dato}]")
            else:
                recorrido.append(str(nodo_actual.Dato))

            if nodo_actual == destino:
                break

            if avanzar:
                if nodo_actual.Orb_Siguiente:
                    nodo_actual = nodo_actual.Orb_Siguiente
                else:
                    nodo_actual = nodo_actual.Siguiente
            else:
                if nodo_actual.Orb_Anterior:
                    nodo_actual = nodo_actual.Orb_Anterior
                else:
                    nodo_actual = nodo_actual.Siguiente

        if impresion:
            print(" -> ".join(recorrido))
        return recorrido

