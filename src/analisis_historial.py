import pandas as pd
from historial_admin import cargar_historial


# Filtrar el historial solo para un jugador
def analizar_historial_jugador(nombre_jugador):
    """
    Función que utilizaré para ver que tal van las estrategias con unas métricas simples
    """

    # Cargar el historial completo
    historial = cargar_historial()

    # Filtrar el historial para el jugador específico
    historial_jugador = historial[historial["Jugador"] == nombre_jugador]

    if historial_jugador.empty:
        print(f"No hay partidas registradas para el jugador '{nombre_jugador}'.")
        return

    print(f"\n--- Análisis del historial de '{nombre_jugador}' ---")

    # Contar movimientos realizados
    movimientos_realizados = historial_jugador["MovimientoJugador"].value_counts()
    print("\nMovimientos realizados:")
    print(movimientos_realizados)

    # Contar resultados de las partidas
    resultados_partidas = historial_jugador["Resultado"].value_counts()
    print("\nResultados de las partidas:")
    print(resultados_partidas)

    # Calcular el total de partidas jugadas
    total_partidas = len(historial_jugador)
    print(f"\nTotal de partidas jugadas: {total_partidas}")

    # Calcular porcentaje de victorias, derrotas y empates
    victorias = resultados_partidas.get("Victoria", 0)
    derrotas = resultados_partidas.get("Derrota", 0)
    empates = resultados_partidas.get("Empate", 0)

    print(f"\nPorcentajes:")
    print(f" - Victorias: {victorias / total_partidas * 100:.2f}%")
    print(f" - Derrotas: {derrotas / total_partidas * 100:.2f}%")
    print(f" - Empates: {empates / total_partidas * 100:.2f}%")

# Ejecución
analizar_historial_jugador("Berto")