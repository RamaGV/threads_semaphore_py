import threading

"""
Ejercicio: Control de acceso a una sala de espera (semáforo)
Descripción:
◦ Implementa un programa en Python que simule el control de acceso a una sala de esperautilizando semáforos como mecanismo de sincronización. La sala de espera tiene una capacidadmáxima de 5 personas y se requiere que las personas esperen su turno para ingresar.
El programa debe tener las siguientes características:
1. Definir una clase SalaEspera que controle el acceso a la sala de espera.
2. Utilizar un semáforo para controlar la capacidad máxima de la sala.
3. Implementar los siguientes métodos en la clase SalaEspera:
◦ entrar(): Permite a una persona entrar a la sala de espera. Si la capacidad máxima ha sido alcanzada, la persona debeesperar hasta que haya espacio disponible.
◦ salir(): Permite a una persona salir de la sala de espera, liberando un espacio.
◦ obtener_cantidad_personas(): Devuelve la cantidad de personas actualmente en la sala de espera.
"""

class SalaEspera:
    def __init__(self):
        self.aforo = 5
        self.semaphore = threading.Semaphore(self.aforo)
        self.person_count = 0

    def render(self):
        print(f"Personas en la sala de espera: {self.person_count}")

    def enter(self):
        self.semaphore.acquire()
        self.person_count += 1

    def exit(self):
        self.semaphore.release()
        self.person_count -= 1

    def get_person_count(self):
        return self.person_count
