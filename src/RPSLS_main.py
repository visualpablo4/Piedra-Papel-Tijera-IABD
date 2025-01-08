"""
LAGARTO gana a SPOCK y a PAPEL, pierde contra TIJERA y PIEDRA
SPOCK gana a TIJERA y a PIEDRA, pierde contra LAGARTO y PAPEL
"""

import random
from enum import IntEnum
from historial_admin import guardar_historial, cargar_historial
from RPSLS_estrategias import estrategia_basada_en_tendencias, estrategia_combinada, analizar_rendimiento


# Enumeración para las acciones posibles de la partida
class GameAction(IntEnum):
    Piedra = 0
    Papel = 1
    Tijeras = 2
    Lagarto = 3
    Spock = 4

# Enumeración para los resultados posibles de la partida (Victoria, Derrota, Empate)
class GameResult(IntEnum):
    Victory = 0
    Defeat = 1
    Tie = 2


# Función para evaluar el resultado de la partida
def assess_game(user_action, computer_action):

    game_resultado = None

    # Misma elección
    if user_action == computer_action:
        print(f"El jugador y la computadora eligieron {user_action.name}. Es empate!")
        game_resultado = GameResult.Tie

    # Condiciones para ganar
    # La barra (/) permite que el código continúe en la siguiente línea
    elif (user_action == GameAction.Piedra and computer_action in [GameAction.Tijeras, GameAction.Lagarto]) or \
         (user_action == GameAction.Papel and computer_action in [GameAction.Piedra, GameAction.Spock]) or \
         (user_action == GameAction.Tijeras and computer_action in [GameAction.Papel, GameAction.Lagarto]) or \
         (user_action == GameAction.Lagarto and computer_action in [GameAction.Papel, GameAction.Spock]) or \
         (user_action == GameAction.Spock and computer_action in [GameAction.Piedra, GameAction.Tijeras]):
        print(f"{user_action.name} vence a {computer_action.name}. ¡Tú ganas!")
        game_resultado = GameResult.Victory

    # Si no ganas ni empatas, pierdes
    else:
        print(f"{computer_action.name} vence a {user_action.name}. Tú pierdes!")
        game_resultado = GameResult.Defeat

    return game_resultado


def get_computer_action(nombre_jugador):
    """
    Estrategia combinada para decidir el movimiento de la computadora:
    1. Historial vacío: Movimiento aleatorio.
    2. Usar historial completo si el jugador tiene pocas partidas registradas.
    3. Usar historial específico del jugador cuando haya suficientes partidas registradas.
    """
    # Cargar el historial completo
    historial = cargar_historial()

    # Caso 1: Historial vacío --> Movimiento aleatorio 
    if historial.empty:
        print("Historial vacío. Seleccionando un movimiento aleatorio.")
        return GameAction(random.randint(0, 4)) # Movimiento aleatorio (0: Piedra, ..., 4: Spock)
    
    # Filtrar el historial del jugador específico
    historial_jugador = historial[historial["Jugador"] == nombre_jugador]

    # Caso 2: Historial insuficiente --> Usar historial global
    if len(historial_jugador) <= 5:
        print(f"Historial insuficiente para {nombre_jugador}. Usando historial global.")
        estrategia_base = estrategia_basada_en_tendencias(historial["MovimientoJugador"].tolist())
    # Caso 3: Usar historial específico del jugador
    else:
        print(f"Usando historial específico para {nombre_jugador}.")
        estrategia_base = estrategia_combinada(historial_jugador["MovimientoJugador"].tolist())

    # Estrategia adaptativa: Revisar rendimiento reciente
    if len(historial_jugador) >= 3 and analizar_rendimiento(historial_jugador):
        #print("Computadora ha perdido las últimas dos rondas. Introduciendo más aleatoriedad.")
        return GameAction(random.randint(0, 4))

    # Introducir aleatoriedad: 20% de probabilidad de hacer un movimiento aleatorio en cualquier jugada
    if random.random() < 0.2:
        #print("Movimiento aleatorio para evitar ser predecible.")
        return GameAction(random.randint(0, 4))

    return GameAction(estrategia_base)  


def get_user_action():
    game_choices = [f"{game_action.name}[{game_action.value}]" for game_action in GameAction]
    game_choices_str = ", ".join(game_choices)
    
    user_selection = int(input(f"\nElige una acción ({game_choices_str}): "))
    user_action = GameAction(user_selection)

    return user_action   


def elegir_duracion_partida():
    # Función para decidir la duración de la partida
    print("\nEscoge la duración de la partida:\n 1. Una sola ronda\n 2. Hasta que uno llegue a 3 victorias\n 3. Hasta que uno llegue a 5 victorias")

    while True:
        try:
            opcion = int(input("Introduce tu elección (1, 2 o 3): "))
            if opcion in [1, 2, 3]:
                return opcion
            else:
                print("Por favor, selecciona una opción válida (1, 2 o 3).")
        except ValueError:
            print("Entrada inválida. Introduce un número (1, 2 o 3).")


def gestionar_partida(player_name, duracion):
    # Flujo del juego

    # Inicializar variables para contar victorias y rondas
    victorias_jugador = 0
    victorias_computadora = 0
    rondas_jugadas = 0

    # Definir objetivo de victorias según la duración seleccionada
    if duracion == 1:
        objetivo_victorias = 1
    elif duracion == 2:
        objetivo_victorias = 3
    else:
        objetivo_victorias = 5

    while victorias_jugador < objetivo_victorias and victorias_computadora < objetivo_victorias:
        rondas_jugadas += 1
        print(f"\n--- Ronda {rondas_jugadas} ---")

        try:
            user_action = get_user_action()
        except ValueError: # Manejo de errores
            print(f"Selección inválida. Escoge una acción dentro del rango [0, 1, 2, 3 o 4]!")
            continue

        computer_action = get_computer_action(player_name)
        resultado = assess_game(user_action, computer_action)

        # Guardar los datos de la partida en el historial
        guardar_historial(player_name, user_action.name, computer_action.name, resultado)

        # Actualizar victorias
        if resultado == GameResult.Victory:
            victorias_jugador += 1
        elif resultado == GameResult.Defeat:
            victorias_computadora += 1

        # Mostrar el marcador
        print(f"\nMarcador --> {player_name} {victorias_jugador} - {victorias_computadora} Computadora ")

    return victorias_jugador, victorias_computadora


def mostrar_resultado_final(victorias_jugador, victorias_computadora, player_name):
    # Final de la partida
    if victorias_jugador > victorias_computadora:
        print(f"\n¡Felicidades {player_name}! ¡Ganaste la partida con {victorias_jugador} victorias!")
    else:
        print(f"\nLa computadora ganó la partida. Resultado: {victorias_jugador} - {victorias_computadora}. ¡Mejor suerte la próxima vez!")


def play_another_round():
    # Función para preguntar al usuario si le gustaría jugar otra partida
    another_round = input("\n¿Jugar otra partida? (y/n): ")
    if another_round.lower() == 'y':
        print("------------------------------------------------------------------------")
    return another_round.lower() == 'y'



def main():

    print("\n¡Bienvenido a Piedra, Papel, Tijera, Lagarto o Spock!")
    
    while True:
        # Loguearse para que quede registrado en el historial.
        player_name = input("Introduce tu nombre: ")

        duracion = elegir_duracion_partida()

        victorias_jugador, victorias_computadora = gestionar_partida(player_name, duracion)

        mostrar_resultado_final(victorias_jugador, victorias_computadora, player_name)

        # Preguntar si quiere jugar otra partida
        if not play_another_round():
            print(f"¡Gracias por jugar {player_name}! ¡Hasta la próxima!")
            break


if __name__ == "__main__":
    main()
