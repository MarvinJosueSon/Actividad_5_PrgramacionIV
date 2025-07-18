estudiantesList=[]
class Estudiante:
    def __init__(self,nombre,id,carrera,nota):
        self.nombre = nombre
        self.id = id
        self.carrera = carrera
        self.nota = nota
    def Mostrar(self):
        print(f"Nombre: {self.nombre}; Carné:{self.id}; carrera:{self.carrera}; nota:{self.nota}")
def ingresar():
    try:
        nombreAux=input("Ingrese el nombre del estudiante: ")
        idAux=int(input("Ingrese el id del estudiante: "))
        carreraAux=input("Ingrese la carrera del estudiante: ")
        notaAux=float(input("Ingrese la nota final del estudiante: "))
        if notaAux>0 and notaAux<=100 and idAux>0 :
            estudianteAux=Estudiante(nombreAux,idAux,carreraAux,notaAux)
            estudiantesList.append(estudianteAux)
            print("Agregado con exito")
        else:
            print("Nota y carné deben ser positivos")
    except ValueError:
        print("ERROR: Edad debe ser entero/Nota final debe ser un numero")
def promedio():
    if len(estudiantesList) > 0:
        suma=0
        for estudiante in estudiantesList:
            suma=suma+estudiante.nota
        print(f"El promedio general es: {suma/len(estudiantesList)}")
    else:
        print("No hay estudiantes en la lista")
def buscar():
    if len(estudiantesList) > 0:
        existe=False
        idAux=int(input("Ingrese el id del estudiante a buscar: "))
        for estudiante in estudiantesList:
            if estudiante.id == idAux:
                estudianteAux=estudiante
                existe=True

        if existe:
            estudianteAux.Mostrar()
        else:
            print("El estudiante no existe")
def mostrarTodos():
    if len(estudiantesList) > 0:
        for estudiante in estudiantesList:
            estudiante.Mostrar()
            print("")
    else:
        print("No hay estudiantes en la lista")

while True:
    print("==MENU==")
    print("1. Ingresar estudiante")
    print("2. Mostrar estudiantes registrados")
    print("3. Buscar estudiante")
    print("4. Promedio general de estudiantes")
    print("5. Salir")
    opcion=input("Ingrese la opcion: ")
    match opcion:
        case "1":
            ingresar()
        case "2":
            mostrarTodos()
        case "3":
            buscar()
        case "4":
            promedio()
        case "5":
            print("Saliendo...")
            break

