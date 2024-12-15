import random
from enum import IntEnum


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


def get_computer_action():
    computer_selection = random.randint(0, len(GameAction) - 1)
    computer_action = GameAction(computer_selection)
    print(f"\nLa computadora eligió {computer_action.name}.")

    return computer_action

def get_user_action():
    # Scalable to more options (beyond Piedra, Papel and Tijeras...)
    game_choices = [f"{game_action.name}[{game_action.value}]" for game_action in GameAction]
    game_choices_str = ", ".join(game_choices)
    
    user_selection = int(input(f"\nElige una acción ({game_choices_str}): "))
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

    while True:
        try:
            user_action = get_user_action()
        except ValueError:
            print(f"Selección inválida. Escoge una acción dentro del rango [0, 1 o 2]!")
            continue

        computer_action = get_computer_action()
        assess_game(user_action, computer_action)
        
        if not play_another_round():
            break


if __name__ == "__main__":
    main()
