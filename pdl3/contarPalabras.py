from multiprocessing import Process, Queue

"""
    Aplicar el uso de procesos y colas en python,
    para realizar el conteo de palabras,
    en varios archivos de texto de manera recurrente.

    Diseño de solución
    ------------------
    Conteo de palabras:
        Crear función para contar palabras en un archivo de texto.
        Utilizar procesos para realizar el conteo de palabras en paralelo.
        Utilizar colas para compartir los resultados del conteo entre los procesos.

    Implementación de la solución
    -----------------------------
    Conteo de palabras:
        Crear función count_words(filename, result_queue), recibe el nombre de un archivo de texto y una cola.
        Utilizar multiprocessing para crear un proceso que ejecute la función count_words.
        Utilizar una cola result_queue para almacenar el resultado del conteo de palabras.
"""


def count_words(filename, result_queue):
    word_count = 0
    with open(filename, "r") as file:
        for line in file:
            words = line.split()
            word_count += len(words)
    result_queue.put(word_count)


def main():
    files = ["txt1.txt", "txt2.txt", "txt3.txt"]
    result_queue = Queue()
    processes = []

    for file in files:
        process = Process(target=count_words, args=(file, result_queue))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    total_words = 0
    while not result_queue.empty():
        total_words += result_queue.get()

    print(f"Total words: {total_words}")


if __name__ == "__main__":
    main()
