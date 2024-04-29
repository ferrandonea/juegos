import random

def generar_secreto(longitud: int, colores: list[str]) -> list[str]:
    """
    Genera una lista aleatoria de colores como la combinación secreta.

    Args:
        longitud (int): Número de colores en la combinación secreta.
        colores (list[str]): lista de posibles colores.

    Returns:
        list[str]: lista de colores que representa la combinación secreta.
    """
    return [random.choice(colores) for _ in range(longitud)]

def obtener_pistas(secreto: list[str], intento: list[str]) -> tuple[int, int]:
    """
    Calcula el número de pines negros y blancos basado en la comparación entre
    la combinación secreta y el intento del usuario.

    Args:
        secreto (list[str]): La combinación secreta de colores.
        intento (list[str]): El intento del usuario para adivinar la combinación secreta.

    Returns:
        tuple[int, int]: Número de pines negros (posición y color correctos) y pines blancos (solo color correcto).
    """
    pines_negros = sum(s == i for s, i in zip(secreto, intento))
    pines_blancos = sum(min(secreto.count(c), intento.count(c)) for c in set(intento)) - pines_negros
    return pines_negros, pines_blancos

def validar_intento(intento: list[str], colores: list[str], longitud: int) -> bool:
    """
    Valida si el intento del usuario es válido, comprobando si todos los colores están en la lista permitida
    y si la longitud del intento es correcta.

    Args:
        intento (list[str]): El intento del usuario.
        colores (list[str]): lista de colores permitidos.
        longitud (int): Longitud correcta del intento.

    Returns:
        bool: True si el intento es válido, False en caso contrario.
    """
    return all(color in colores for color in intento) and len(intento) == longitud

def seleccionar_dificultad() -> tuple[int, int]:
    """
    Permite al usuario seleccionar el nivel de dificultad del juego y devuelve la longitud de la combinación
    secreta y la cantidad de colores posibles basado en la elección.

    Returns:
        tuple[int, int]: Longitud de la combinación secreta y cantidad de colores permitidos.
    """
    niveles: dict[str, tuple[int, int]] = {'1': (4, 6), '2': (6, 8), '3': (8, 10)}
    while True:
        nivel = input("Elige un nivel de dificultad (1-Fácil, 2-Medio, 3-Difícil): ")
        if nivel in niveles:
            return niveles[nivel]
        print("Entrada no válida. Por favor elige 1, 2 o 3.")

def jugar_mastermind(intentos_maximos: int = 10) -> None:
    """
    Ejecuta el juego Mastermind permitiendo al usuario intentar adivinar la combinación secreta de colores
    generada por la computadora o viceversa, basándose en la dificultad seleccionada.
    Permite configurar la cantidad máxima de intentos para adivinar la combinación secreta.

    Args:
        intentos_maximos (int): Cantidad máxima de intentos que el usuario tiene para adivinar la combinación secreta.
    """
    print("Bienvenido al juego de Mastermind.")
    longitud_secreto, cantidad_colores = seleccionar_dificultad()
    colores = ['rojo', 'azul', 'verde', 'amarillo', 'naranja', 'púrpura', 'marrón', 'blanco'][:cantidad_colores]
    secreto = generar_secreto(longitud_secreto, colores)
    estadisticas = {'jugados': 0, 'ganados': 0}

    while True:
        print(f"Tienes que adivinar la combinación de {longitud_secreto} colores.")
        print(f"Los colores posibles son: {', '.join(colores)}.")

        for intento_num in range(1, intentos_maximos + 1):
            intento = input(f"Intento {intento_num}/{intentos_maximos}. Ingresa tu combinación: ").lower().split()
            if validar_intento(intento, colores, longitud_secreto):
                pines_negros, pines_blancos = obtener_pistas(secreto, intento)
                print(f"Pines negros: {pines_negros}, Pines blancos: {pines_blancos}")
                if pines_negros == longitud_secreto:
                    print("¡Felicidades! Has adivinado la combinación secreta.")
                    estadisticas['ganados'] += 1
                    break
            else:
                print("Entrada no válida. Asegúrate de ingresar colores válidos y la cantidad correcta.")
        else:
            print("Has alcanzado el número máximo de intentos.")
            print(f"La combinación secreta era: {', '.join(secreto)}.")

        estadisticas['jugados'] += 1
        print(f"Estadísticas: Partidas jugadas: {estadisticas['jugados']}, Partidas ganadas: {estadisticas['ganados']}")

        continuar = input("¿Quieres jugar otra vez? (sí/no): ").lower()
        if continuar != 'sí':
            break
        secreto = generar_secreto(longitud_secreto, colores)  # Genera nuevo secreto para el siguiente juego

if __name__ == "__main__":
    jugar_mastermind(intentos_maximos=12)
