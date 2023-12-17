import math
from prettytable import PrettyTable

def secant_method(equation, x0, x1, epsilon, max_iter):
    # Convertir la ecuación a funciones
    f = lambda x: eval(equation, {'x': x, 'math': math})

    # Inicializar el contador de iteraciones
    iter_count = 0

    # Crear una tabla para mostrar los resultados
    table = PrettyTable()
    table.field_names = ["n", "xn-1", "xn", "f(xn-1)", "f(xn)", "xn+1"]

    # Repetir mientras la diferencia sea mayor que el umbral y no se supere el máximo de iteraciones
    while True:
        # Calcular la siguiente aproximación usando el método de la secante
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))

        # Añadir los datos a la tabla
        table.add_row([iter_count + 1, f"{x0:.5f}", f"{x1:.5f}", f"{f(x0):.5f}", f"{f(x1):.5f}", f"{x2:.5f}"])

        # Actualizar las estimaciones y la diferencia
        x0, x1, diff = x1, x2, abs(x2 - x1)

        # Incrementar el contador de iteraciones
        iter_count += 1

        # Verificar las condiciones de salida
        if diff <= epsilon or iter_count >= max_iter:
            break

    # Devolver la estimación final, el número de iteraciones y la tabla
    return x2, iter_count, table

# Ingresar la ecuación
equation = input("Ingrese la ecuación en términos de 'x': ")

# Ingresar las dos estimaciones iniciales (x0 y x1)
x0 = float(input("Ingrese la primera estimación inicial (x0): "))
x1 = float(input("Ingrese la segunda estimación inicial (x1): "))

# Elegir el umbral y el máximo de iteraciones
epsilon = 0.00001
max_iter = int(input("Ingrese el máximo de iteraciones: "))

# Llamar a la función del método de la secante
root, iter_count, table = secant_method(equation, x0, x1, epsilon, max_iter)

# Imprimir el resultado final y la tabla
print(f"\nLa raíz es {root:.5f}, encontrada en {iter_count} iteraciones.")
print(table)
