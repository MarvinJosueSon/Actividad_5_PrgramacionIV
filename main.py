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
        estudianteAux=Estudiante(nombreAux,idAux,carreraAux,notaAux)
        estudiantesList.add(estudianteAux)

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
        idAux=input("Ingrese el id del estudiante a buscar: ")
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

