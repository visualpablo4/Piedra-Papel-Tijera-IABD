import os
import pandas as pd

# Ruta del archivo CSV dentro de la carpeta 'src'
historial_partidas = os.path.join("src", "data", "historial_partidas.csv")


# Función para guardar el historial
def guardar_historial(nombre_jugador, movimiento_jugador, movimiento_computadora, resultado):

    # Convertir el resultado a texto (en lugar de usar 0, 1, 2)
    if resultado == 0:
        resultado = "Victoria"
    elif resultado == 1:
        resultado = "Derrota"
    else:
        resultado = "Empate"

    # Crear un diccionario con los datos de la partida
    partida = {
        "Jugador": nombre_jugador,
        "MovimientoJugador": movimiento_jugador,
        "MovimientoComputadora": movimiento_computadora,
        "Resultado": resultado
    }

    # Intentar cargar el historial (si el archivo existe)
    try:
        df = pd.read_csv(historial_partidas)
    except (FileNotFoundError, pd.errors.EmptyDataError):
        df = pd.DataFrame(columns=["Jugador", "MovimientoJugador", "MovimientoComputadora", "Resultado"])
    
    # Agregar la nueva partida al DataFrame
    # Con la función concat de pandas, concatenamos el DataFrame existente con el nuevo DataFrame (pd.DataFrame([partida]))
    df = pd.concat([df, pd.DataFrame([partida])], ignore_index=True)

    # Guardar el DataFrame actualizado en el archivo CSV
    df.to_csv(historial_partidas, index=False)


# Función para cargar el historial
def cargar_historial():
    
    try:
        return pd.read_csv(historial_partidas)
    except (FileNotFoundError, pd.errors.EmptyDataError):
        return pd.DataFrame(columns=["Jugador", "MovimientoJugador", "MovimientoComputadora", "Resultado"])
    