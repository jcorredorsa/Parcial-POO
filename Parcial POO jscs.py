class usuario:
    def __init__(self,nombre,id,rol):
        self.__nombre=nombre
        self.__id=id
        self.__rol=rol
    def get_nombre(self):
        return self.__nombre
    def get_id(self):
        return self.__id
    def get_rol(self):
        return self.__rol

        
class libro:
    def __init__(self,titulo,categoria):
        self.__categoria=categoria
        self.__titulo=titulo
    def get_titulo(self):
        return self.__titulo
    def get_categoria(self):
        return self.__categoria

class libreria:
    def __init__(self):
        self._usuarios =[]
        self._libros=[]
        self._categorias=["Ciencia","Matemática","Programación"]
    def registro(self):
        nombre = input("Ingrese el nombre del nuevo usuario: ")
        id= input("Ingrese el ID del nuevo usuario: ")
        rol = input("Ingrese el rol (Estudiante o Profesor): ")
        print(f"Usuario {nombre} registrado con éxito.")
        nuevo = usuario(nombre, id, rol)
        self._usuarios.append(nuevo)
    def registro_libro(self):
        titulo = input("Ingrese el título del libro: ")  
        categoria = input("Ingrese la categoría:")
        if categoria not in self._categorias:
            print ("Categoria no encontrada, solamente tenemos Ciencia, Matemática y Programación")
            return
        nuevo_libro = libro(titulo, categoria)
        self._libros.append(nuevo_libro)
        print(f"Libro {titulo} registrado con éxito.")
    def mostrar_menu(self):
        print("===============================================")
        print(" SIMULADOR DE OPERACIONES BÁSICAS DE BIBLIOTECA")
        print("===============================================")
        print("1. Registrar nuevo usuario")
        print("2. Registrar nuevo libro")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        return opcion
    def ejecutar(self):
        while True:
            opcion = self.mostrar_menu()
            if opcion =="1":
                self.registro()
            elif opcion =="2":
                self.registro_libro()
            elif opcion =="3":
                break
            else:
                print("Opción no valida")
if __name__ == "__main__":
    librerias = libreria() 
    librerias.ejecutar() 






        



        