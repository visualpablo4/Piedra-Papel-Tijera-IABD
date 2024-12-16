import random
from enum import IntEnum
from historial_admin import guardar_historial, cargar_historial
from estrategias import estrategia_basada_en_tendencias, estrategia_combinada, analizar_rendimiento


# Enumeración para las acciones posibles de la partida
class GameAction(IntEnum):
    Piedra = 0
    Papel = 1
    Tijeras = 2

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

    # Escoges Piedra
    elif user_action == GameAction.Piedra:
        if computer_action == GameAction.Tijeras:
            print("Piedra rompe Tijeras. Tú ganas!")
            game_resultado = GameResult.Victory
        else:
            print("Papel cubre Piedra. Tú pierdes!")
            game_resultado = GameResult.Defeat

    # Escoges Papel
    elif user_action == GameAction.Papel:
        if computer_action == GameAction.Piedra:
            print("Papel cubre Piedra. Tú ganas!")
            game_resultado = GameResult.Victory
        else:
            print("Tijeras cortan Papel. Tú pierdes!")
            game_resultado = GameResult.Defeat

    # Escoges Tijeras
    elif user_action == GameAction.Tijeras:
        if computer_action == GameAction.Piedra:
            print("Piedra rompe Tijeras. Tú pierdes!")
            game_resultado = GameResult.Defeat
        else:
            print("Tijeras cortan Papel. Tú ganas!")
            game_resultado = GameResult.Victory

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
        return GameAction(random.randint(0,2)) # Movimiento aleatorio (0: Piedra, 1: Papel, 2: Tijeras)
    
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
        print("Computadora ha perdido las últimas dos rondas. Introduciendo más aleatoriedad.")
        return GameAction(random.randint(0, 2))

    # Introducir aleatoriedad: 20% de probabilidad de hacer un movimiento aleatorio en cualquier jugada
    if random.random() < 0.2:
        print("Movimiento aleatorio para evitar ser predecible.")
        return GameAction(random.randint(0, 2))

    """
    Aclaración: muchos prints que estoy poniendo los quitaré o los comentaré cuando el proyecto esté finalizado, 
    ya que solamente los uso para comprobar que el flujo de programa va como deseo.
    """

    return GameAction(estrategia_base)  


def get_user_action():
    # Scalable to more options (beyond Piedra, Papel and Tijeras...)
    game_choices = [f"{game_action.name}[{game_action.value}]" for game_action in GameAction]
    game_choices_str = ", ".join(game_choices)
    
    user_selection = int(input(f"\nElige una acción ({game_choices_str}): "))
    #print(f"El jugador ha elegido {user_selection}")
    user_action = GameAction(user_selection)

    return user_action   


# Función para preguntar al usuario si le gustaría jugar otra partida o varias
def play_another_round():
    another_round = input("\n¿Jugar otra ronda? (y/n): ")
    if another_round.lower() == 'y':
        print("------------------------------------------------------------------------")
    return another_round.lower() == 'y'


def main():

    print("\n¡Bienvenido a Piedra, Papel o Tijera!")
    
    # Loguearse para que quede registrado en el historial.
    player_name = input("Introduce tu nombre: ")

    while True:
        try:
            user_action = get_user_action()
        except ValueError:
            print(f"Selección inválida. Escoge una acción dentro del rango [0, 1 o 2]!")
            continue

        computer_action = get_computer_action(player_name)
        resultado = assess_game(user_action, computer_action)

        # Guardar los datos de la partida en el historial
        guardar_historial(player_name, user_action.name, computer_action.name, resultado)

        '''
        # Mostrar la última partida del historial
        print("\n--- Última partida ---")
        print(cargar_historial().tail(1).to_string(index=False))
        '''

        #if not play_another_round():
        #    break


if __name__ == "__main__":
    main()
