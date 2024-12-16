def elegir_duracion_partida():
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

duracion = elegir_duracion_partida()
print(duracion)

# ***************************************************************************

# Variables para contar victorias
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