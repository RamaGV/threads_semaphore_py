import threading

contador = 0


def incrementar():
    global contador
    for _ in range(1000000):
        contador += 1


def main():
    # Crear hilos
    hilos = [None] * 5
    for _ in range(5):
        hilos[_] = threading.Thread(target=incrementar)
    
    # Iniciar hilos
    for _ in range(5):
        hilos[_].start()
    
    # Esperar a que los hilos terminen
    for _ in range(5):
        hilos[_].join()
    
    # Imprimir el valor final del contador
    print("Contador:", contador)


if __name__ == "__main__":
    main()
