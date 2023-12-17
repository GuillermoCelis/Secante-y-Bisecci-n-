import math
from prettytable import PrettyTable

def bisection(equation, a, b, epsilon, max_iter):
    # Convertir la ecuación a funciones
    f = lambda x: eval(equation, {'x': x, 'math': math})

    # Inicializar el contador de iteraciones
    iter_count = 0

    # Crear una tabla para mostrar los resultados
    table = PrettyTable()
    table.field_names = ["n", "xn-1", "xn", "f(xn-1)", "f(xn)", "xn+1"]

    # Verificar si los extremos a y b tienen signos opuestos
    if f(a) * f(b) > 0:
        raise ValueError("Los extremos a y b deben tener signos opuestos.")

    # Repetir mientras la longitud del intervalo sea mayor que el umbral y no se supere el máximo de iteraciones
    while (b - a) / 2 > epsilon and iter_count < max_iter:
        # Calcular el punto medio del intervalo
        c = (a + b) / 2

        # Añadir los datos a la tabla
        table.add_row([iter_count + 1, f"{a:.5f}", f"{b:.5f}", f"{f(a):.5f}", f"{f(b):.5f}", f"{c:.5f}"])

        # Verificar si el punto medio es la raíz o cambiar el intervalo
        if f(c) == 0:
            break
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c

        # Incrementar el contador de iteraciones
        iter_count += 1

    # Calcular y devolver la estimación final y el número de iteraciones
    root = (a + b) / 2
    return root, iter_count, table

# Ingresar la ecuación
equation = input("Ingrese la ecuación en términos de 'x': ")

# Ingresar los extremos del intervalo [a, b]
a = float(input("Ingrese el extremo izquierdo del intervalo (a): "))
b = float(input("Ingrese el extremo derecho del intervalo (b): "))

# Elegir el umbral y el máximo de iteraciones
epsilon = 0.00001
max_iter = int(input("Ingrese el máximo de iteraciones: "))

# Llamar a la función de bisección
root, iter_count, table = bisection(equation, a, b, epsilon, max_iter)

# Imprimir el resultado final y la tabla
print(f"\nLa raíz es {root:.5f}, encontrada en {iter_count} iteraciones.")
print(table)
