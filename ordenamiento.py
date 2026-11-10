import random


# ---------------------------------------------------------------
# Quick Sort (devuelve la lista ordenada y el número de iteraciones)
# Una iteración = una pasada del ciclo for de la partición.
# ---------------------------------------------------------------
def quick_sort(lista):
    arr = lista[:]          # copia para no modificar la original
    contador = [0]

    def particion(bajo, alto):
        pivote = arr[alto]
        i = bajo - 1
        for j in range(bajo, alto):
            contador[0] += 1
            if arr[j] <= pivote:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[alto] = arr[alto], arr[i + 1]
        return i + 1

    def ordenar(bajo, alto):
        if bajo < alto:
            p = particion(bajo, alto)
            ordenar(bajo, p - 1)
            ordenar(p + 1, alto)

    ordenar(0, len(arr) - 1)
    return arr, contador[0]


# ---------------------------------------------------------------
# Heap Sort (devuelve la lista ordenada y el número de iteraciones)
# Una iteración = una pasada de cualquiera de sus ciclos
# (construcción del heap, extracción y descenso en heapify).
# ---------------------------------------------------------------
def heap_sort(lista):
    arr = lista[:]
    n = len(arr)
    iteraciones = 0

    def heapify(tam, i):
        nonlocal iteraciones
        while True:
            iteraciones += 1
            mayor = i
            izq = 2 * i + 1
            der = 2 * i + 2
            if izq < tam and arr[izq] > arr[mayor]:
                mayor = izq
            if der < tam and arr[der] > arr[mayor]:
                mayor = der
            if mayor == i:
                break
            arr[i], arr[mayor] = arr[mayor], arr[i]
            i = mayor

    # Construir el max-heap
    for i in range(n // 2 - 1, -1, -1):
        iteraciones += 1
        heapify(n, i)

    # Extraer elementos uno por uno
    for i in range(n - 1, 0, -1):
        iteraciones += 1
        arr[0], arr[i] = arr[i], arr[0]
        heapify(i, 0)

    return arr, iteraciones


# ---------------------------------------------------------------
# Menú
# ---------------------------------------------------------------
def generar_lista():
    return [random.randint(1, 100) for _ in range(10)]


def comparar(lista):
    ordenada_q, it_q = quick_sort(lista)
    ordenada_h, it_h = heap_sort(lista)

    print("\nLista original :", lista)
    print("Quick Sort     :", ordenada_q, f"-> {it_q} iteraciones")
    print("Heap Sort      :", ordenada_h, f"-> {it_h} iteraciones")

    if it_q < it_h:
        print("\nResultado: Quick Sort usó menos iteraciones.")
    elif it_h < it_q:
        print("\nResultado: Heap Sort usó menos iteraciones.")
    else:
        print("\nResultado: ambos algoritmos usaron las mismas iteraciones.")


def menu():
    lista = generar_lista()

    while True:
        print("\n========== MENÚ ==========")
        print("Lista actual:", lista)
        print("1. Generar nueva lista aleatoria")
        print("2. Ordenar con Quick Sort")
        print("3. Ordenar con Heap Sort")
        print("4. Ordenar con ambos y comparar iteraciones")
        print("5. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            lista = generar_lista()
            print("Nueva lista:", lista)
        elif opcion == "2":
            ordenada, it = quick_sort(lista)
            print("Quick Sort:", ordenada, f"-> {it} iteraciones")
        elif opcion == "3":
            ordenada, it = heap_sort(lista)
            print("Heap Sort:", ordenada, f"-> {it} iteraciones")
        elif opcion == "4":
            comparar(lista)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    menu()
