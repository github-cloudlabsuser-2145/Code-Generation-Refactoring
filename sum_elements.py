# Programa mejorado para sumar una lista de números enteros proporcionados por el usuario.

MAX_ELEMENTS = 100

def calculate_sum(numbers):
    """Calcula la suma de una lista de números."""
    return sum(numbers)

def get_integer_input(prompt):
    """Solicita al usuario un número entero y maneja errores de entrada."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

def main():
    print("Programa para sumar números enteros.")
    
    # Solicitar el número de elementos
    n = get_integer_input(f"Introduce el número de elementos (1-{MAX_ELEMENTS}): ")
    if not 1 <= n <= MAX_ELEMENTS:
        print(f"Entrada inválida. Por favor, ingrese un número entre 1 y {MAX_ELEMENTS}.")
        return

    # Solicitar los números
    numbers = []
    print(f"Introduce {n} números enteros:")
    for i in range(n):
        num = get_integer_input(f"Número {i + 1}: ")
        numbers.append(num)

    # Calcular y mostrar la suma
    total = calculate_sum(numbers)
    print(f"La suma de los números es: {total}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nPrograma terminado por el usuario.")