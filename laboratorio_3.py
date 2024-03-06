#Clase fecha
class fecha:
    #Función constructora de los atributos
    def __init__(self, dd, mm, aa):
        self.dd = dd
        self.mm = mm
        self.aa = aa
    #Funciónes set
    def setDia(self, dia):
        self.dd = dia
    def setMes(self, mes):
        self.mm = mes
    def setA(self, year):
        self.aa = year
    #Funciónes get
    def getDia(self):
        return self.dd
    def getMes(self):
        return self.mm
    def getA(self):
        return self.aa
    #Función __str__ para definir que aparecerá en consola al hacer un print(fecha)
    def __str__(self):
        return f"{self.dd}/{self.mm}/{self.aa}"

#Clase dirección
class direccion:
   #Función constructora de los atributos 
    def __init__(self, calle, nomenclatura, barrio, ciudad, edificio, apto):
        self.calle = calle
        self.nomenclatura = nomenclatura
        self.barrio = barrio
        self.ciudad = ciudad
        self.edificio = edificio
        self.apto = apto
    #Funciónes set
    def setCalle(self, calle):
        self.calle = calle
    def setNomenclatura(self, nomenclatura):
        self.nomenclatura = nomenclatura
    def setBarrio(self, barrio):
        self.barrio = barrio
    def setCiudad(self, ciudad):
        self.ciudad = ciudad
    def setEdificio(self, edificio):
        self.edificio = edificio
    def setApto(self, apto):
        self.apto = apto
    #Funciónes get
    def getCalle(self):
        return self.calle
    def getNomenclatura(self):
        return self.nomenclatura
    def getBarrio(self):
        return self.barrio
    def getCiudad(self):
        return self.ciudad
    def getEdificio(self):
        return self.edificio
    def getApto(self):
        return self.apto
    #Función toString
    def toString(self):
        print("Calle:", self.calle,"Nomenclatura:", self.nomenclatura, "Barrio:", self.barrio, "Ciudad:", self.ciudad,
              "Edificio:", self.edificio, "Apto:", self.apto)
    #Función __str__, esta función hace basicamente lo mismo que toString, asi que la de arriba se vuelve redundante peeero pues la voy a dejar ahi
    def __str__(self):
        return f"Calle: {self.calle}, Nomenclatura: {self.nomenclatura}, Barrio: {self.barrio}, Ciudad: {self.ciudad}, Edificio: {self.edificio}, Apto: {self.apto}"

#Clase usuario, la principal del programa
class usuario:
    #función constructora de los atributos
    def __init__(self, nombre, id, dd, mm, aa, ciudad_nacimiento, tel, email, calle, nomenclatura, barrio, ciudad, edificio, apto):
        self.nombre = nombre
        self.id = id
        self.fecha_nacimiento = fecha(dd, mm, aa)
        self.ciudad_nacimiento = ciudad_nacimiento
        self.tel = tel
        self.email = email
        self.dir = direccion(calle, nomenclatura, barrio, ciudad, edificio, apto)
    #Funciones set
    def setNombre(self, nombre):
        self.nombre = nombre
    def setId(self, id):
        self.id = id
    def setFecha_Nacimiento(self, fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento
    def setCiudad_Nacimiento(self, ciudad_nacimiento):
        self.ciudad_nacimiento = ciudad_nacimiento
    def setTel(self, tel):
        self.tel = tel
    def setEmail(self, email):
        self.email = email
    def setDir(self, dir):
        self.dir = dir
    #Funciones Get
    def getNombre(self):
        return self.nombre
    def getId(self):
        return self.id
    def getFecha_Nacimiento(self):
        return self.fecha_nacimiento
    def getCiudad_Nacimiento(self):
        return self.ciudad_nacimiento
    def getTel(self):
        return self.tel
    def getEmail(self):
        return str(self.email)
    def getDir(self):
        return self.dir
    #Función __str__, esto puede ser cambiado por un toString y haría lo mismo realmente. Pero este es más conveniente >:3
    def __str__(self):
        return f"Nombre: {self.nombre}, ID: {self.id}, Fecha de Nacimiento: {self.fecha_nacimiento}, Ciudad de Nacimiento: {self.ciudad_nacimiento}, Teléfono: {self.tel}, Email: {self.email}, Dirección: {self.dir}"
    
#Clase agenda, nueva clase del lab 3
class agenda:
    #Funcion constructora, registro y conteo
    def __init__(self):
        self.registro = []
        self.no_reg = 0
        self.capacity = 5

    #Funcion agregar
    def agregar (self, U):
    #Primero busca si el usuario ya existe, si existe retorna False
        if self.buscar(U.id) != -1:
            return False
    #Luego agrega el usuario  
        if self.no_reg < self.capacity:
            self.registro.append(U)
            self.no_reg += 1
            return True
        else:
            return False
    #Funcion buscar, busca al usuario, si se encuentra retorna -1
    def buscar(self, id):
        for i in range(self.no_reg):
            if self.registro[i].id == id:
                return i
        return -1
    #Funcion eliminar, invoca la funcion buscar, si no lo encuentra retorna False
    def eliminar(self, id):
        I = self.buscar(id)
        if I == -1:
            return False
    #si lo encuentra lo borra, -1 en el numero del registro y retorna True  
        self.registro.pop(I)
        self.registro.append(None)
        self.no_reg -= 1
        return True
    #Funcion tofile, abre el archivo agenda ya precreado, y agrega todos los datos de cada usuario ya existentes
    def toFile(self):
        with open('agenda.txt', 'w') as f:
            for usuario in self.registro:
                if usuario:
                    f.write(str(usuario))
#creamos una agenda
mi_agenda = agenda()

#creamos los usuarios y los agregamos
Usuario_1 = usuario("Juan Miguel", 14, 10, 7, 2004, "Medellín", 3725482, "judurango@unal", 43, "55A", "Santa Marta", "Bogotá", "Null", "Null")
mi_agenda.agregar(Usuario_1)

Usuario_2 = usuario("Juan", 21, 10, 7, 2003, "Medellí", 37254182, "Juan@unal", 44, "55A", "Santa Marta", "Bogotá", "Null", "Null")
mi_agenda.agregar(Usuario_2)

Usuario_3 = usuario("Juana", 34, 10, 7, 2002, "Medellís", 37254182, "Juan@unal", 44, "55A", "Santa Marta", "Bogotá", "Null", "Null")
mi_agenda.agregar(Usuario_3)

Usuario_4 = usuario("Juanjo", 43, 10, 7, 2001, "Medellía", 37254182, "Juan@unal", 44, "55A", "Santa Marta", "Bogotá", "Null", "Null")
mi_agenda.agregar(Usuario_4)

Usuario_5 = usuario("nicho", 52, 13, 9, 2004, "Medellín", 32444412, "nbenjua@unal", 44, "55A", "Santa Marta", "Bogotá", "Null", "Null")
mi_agenda.agregar(Usuario_5)

#creamos una funcion para buscar cada usuario segun su id usando el metodo buscar ya creado y que nos retorne si la posicion en q esta
def buscar_usuario_id(id):
    posicion = mi_agenda.buscar(id)
    if posicion != -1:
        print(f"El usuario con ID {id} se encuentra en la posición {posicion} del arreglo.")
    else:
        print(f"No se encontró ningún usuario con el ID {id}.")

buscar_usuario_id(21)
buscar_usuario_id(14)
buscar_usuario_id(1)

mi_agenda.toFile()