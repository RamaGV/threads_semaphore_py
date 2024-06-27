import random
import string


def crear_archivo(archivo, cant_palabras):
    with open(archivo, "w") as archivo:
        for _ in range(cant_palabras):
            palabra = "".join(
                random.choice(string.ascii_lowercase)
                for _ in range(random.randint(1, 10))
            )
            archivo.write(palabra + " ")


palabras_por_archivo = [30, 20, 30]

# Replace with the desired file names
archivos = ["txt1.txt", "txt2.txt", "txt3.txt"]

for i, archivo in enumerate(archivos):
    crear_archivo(archivo, palabras_por_archivo[i])

print("Archivos creados exitosamente.")
