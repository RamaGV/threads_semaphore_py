import random
import threading
import time
import os

"""
Ejercicio: La competencia de los pinguinos glotones.

En un mundo helado, se está llevando a cabo una
competencia entre pinguinos para ver quién come más
peces en un tiempo determinado. Sin embargo, solo
hay un área de pesca disponible y los pinguinos deben
competir por acceder a ella de manera segura y justa.
En este ejercicio, se pide implementar un programa que
simule la competencia de los pinguinos glotones,
aplicando los conceptos de secciones críticas y mutua
exclusión.
Cada pinguinos es representado por un hilo y la sección
crítica es el área de pesca, donde solo un pinguinos
puede acceder a la vez.

Ejercicio: La competencia de los pinguinos glotones
El programa debe cumplir con las siguientes especificaciones:
1. Cada pinguinos debe ser representado por una clase Pinguino, que herede de la clase Thread.
2. Cada pinguinos debe tener un nombre único y una cantidad de peces que ha comido.
3. La cantidad total de peces disponibles en el área de pesca es limitada.
4. Un pinguinos puede comer un pez a la vez y debe esperar su turno para acceder al área de pesca.
5. Se debe garantizar la exclusión mutua para evitar que dos pinguinos accedan al área de pesca almismo tiempo.
6. Al finalizar el tiempo establecido, se debe mostrar el nombre del pinguinos ganador, es decir, aquelque haya comido la mayor cantidad de peces
----------------------------------------------------------------------------------------------------------------
Detalles del programa:

* Cada pinguino se identifica por su nombre, se destaca la cantidad de peces que pesca y la cantidad de peces que ha comido.
* Existe un área de pesca con 50 peces disponibles, los cuales los pinguinos deben competir por pescar y luego comer.
* Cada pinguino puede comer un pez a la vez y debe esperar su turno para acceder al área de pesca.
* Se debe garantizar la exclusión mutua para evitar que dos pinguinos accedan al área de pesca al mismo tiempo.
* La cantidad de peces que pescará es aleatoria y va desde 1 hasta 5 peces, cada pez demora .5s en ser pescado.
* Solo puede pescar si hay peces disponibles y si no hay otro pinguinos pescando.
* Cada pez demora 2s en ser comido.
* Cuando ya no haya peces en el estanque, se muestra el nombre del pinguino ganador, es decir, aquel que haya comido la mayor cantidad de peces.

"""
lock = threading.Lock()
nombres = ["Harry", "Whisky", "Hermione", "Dobby", "Shrek", "Fiona"]
pinguinos = [None] * 6

global peces_en_estanque  # El estanque tiene x peces, cada vez que pescan se reduce la cantidad de peces.
peces_en_estanque = 50
global render_flag  # Bandera para renderizar la información, cambia si algún pinguino pesca o come.
render_flag = False

class Pinguino(threading.Thread):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
        self.comiendo = False
        self.pescando = False
        self.peces_comidos = 0
        self.peces_pescados = 0
    
    def comer(self):
        self.comiendo = True
        self.peces_comidos += 1
        self.peces_pescados -= 1
        time.sleep(1)
        self.comiendo = False
    
    def pescar(self):
        global peces_en_estanque
        peces = random.randint(1, 5)
        self.peces_pescados += peces
        peces_en_estanque -= peces
        if peces_en_estanque < 0:
            peces_en_estanque = 0
        return peces
    
    def run(self):
        global peces_en_estanque
        global render_flag
        
        while peces_en_estanque > 0:
            if self.peces_pescados > 0:
                render_flag = True
                self.comer()
            else:
                with lock:
                    self.pescando = True
                    peces_pescados = self.pescar()
                    render_flag = True
                    time.sleep(0.5 * peces_pescados)
                    self.pescando = False

def render():
    global render_flag
    
    if render_flag:
        os.system("clear")
        print("Peces en el estanque:", peces_en_estanque)
        print("Pinguinos pecando:")
        for _ in range(6):
            if pinguinos[_].pescando:
                print("                  ", pinguinos[_].nombre)
        for _ in range(6):
            print("---------------------------------------------------------")
            print("Pinguino: {:<10}".format(pinguinos[_].nombre))
            print(f"Peces restantes: {pinguinos[_].peces_pescados}")
            if pinguinos[_].pescando:
                print("Ahora está pescando...")
            else:
                print(
                    f"Ahora está {'comiendo...' if pinguinos[_].comiendo else 'en espera...'}"
                )
            print(f"Peces comidos: {pinguinos[_].peces_comidos}")
        print("---------------------------------------------------------")
        render_flag = False

def main():
    for _ in range(6):
        pinguinos[_] = Pinguino(nombres[_])
        pinguinos[_].peces_pescados = random.randint(1, 5)
        pinguinos[_].start()
    
    while peces_en_estanque > 0:
        render()
    
    for _ in range(6):
        pinguinos[_].join()
    print(
        "El ganador es:",
        max(pinguinos, key=lambda pinguino: pinguino.peces_comidos).nombre,
    )


if __name__ == "__main__":
    main()
