import random
from collections import Counter
from enum import IntEnum

# Enumeración para las acciones posibles de la partida
class GameAction(IntEnum):
    Piedra = 0
    Papel = 1
    Tijeras = 2


def estrategia_basada_en_tendencias(movimientos):
    """
    Estrategia principal basada en tendencias:
    Selecciona el contraataque al movimiento más frecuente de las últimas 10 partidas.
    """
    if not movimientos:
        return random.randint(0,2) # Si no hay movimientos registrados, elige aleatoriamente
    
    # Limitar los movimientos a las últimas 10 partidas
    movimientos_recientes = movimientos[-10:]

    # Convertir los movimientos de str a int usando GameAction
    try:
        movimientos_int = [GameAction[movimiento].value for movimiento in movimientos_recientes]
    except KeyError as error:
        print(f"Error: Movimiento inválido encontrado en el historial: {error}")
        return random.randint(0,2) # Manejo de errores: movimiento no reconocido
    
    # Contar la frecuencia de los movimientos
    contador = Counter(movimientos_int)
    movimiento_frecuente = max(contador, key=contador.get) # Movimiento más frecuente
    print(f"La estrategia basada en tendencias: movimiento más frecuente es '{GameAction(movimiento_frecuente).name}'.")
    return (movimiento_frecuente + 1) % 3 # Contraataca el movimiento más frecuente


def estrategia_combinada(movimientos_jugador):
    """
    Estrategia combinada:
    - Detectar patrones específicos (movimientos repetidos y secuencia 'Piedra, Papel, Tijera').
    - Falta añadir algún patrón más
    """
    # Convertir movimientos de str a int usando GameAction
    try:
        movimientos_int = [GameAction[movimiento].value for movimiento in movimientos_jugador]
    except KeyError as error:
        print(f"Error: Movimiento inválido encontrado en el historial: {error}")
        return random.randint(0,2) # Manejo de errores: movimiento no reconocido
    
    # Para que se dé alguno de estos dos patrones debe haber 3 movimientos registrados mínimo
    if len(movimientos_int) >= 3:
        # Patrón 1: Tres movimientos repetidos
        if movimientos_int[-1] == movimientos_int [-2] == movimientos_int[-3]:
            movimiento_repetido = movimientos_int[-1]
            print("Patrón detectado: tres movimientos repetidos.")
            return (movimiento_repetido + 1) % 3 # Contraataca el movimiento repetido
        
        # Patrón 2: Secuencia 'Piedra, Papel, Tijera'
        if movimientos_int[-3:] == [0, 1, 2]: # Piedra (0), Papel (1), Tijeras (2)
            print("Patrón detectado: secuencia 'Piedra, Papel, Tijera'.")
            return 1 # Contraataca con 'Papel' (siguiente esperado sería 'Piedra')
    
    # Si no hay patrones específicos, aplicar la estrategia principal
    return estrategia_basada_en_tendencias(movimientos_jugador)


def analizar_rendimiento(historial_jugador):
    """
    Analiza el rendimiento reciente de la computadora contra el jugador.
    Si la cmoputadora ha perdido al menos 2 de las últimas 3 rondas,
    introducimos más aleatoriedad
    """
    ultimos_resultados = historial_jugador["Resultado"].tail(3).tolist()
    derrotas_computadora = ultimos_resultados.count("Victoria")
    return derrotas_computadora >= 2 # Si perdió al menos 2 de las últimas 3 rondas, devuelve True
