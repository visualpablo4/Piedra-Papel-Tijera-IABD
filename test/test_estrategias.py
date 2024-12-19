#import pytest
from src.main import GameAction
from src.estrategias import estrategia_basada_en_tendencias, estrategia_combinada, analizar_rendimiento
import pandas as pd


def test_estrategia_basada_en_tendencias_sin_movimientos():
    """
    Si no hay movimientos, la estrategia debe devolver un movimiento aleatorio.
    """
    resultado = estrategia_basada_en_tendencias([])
    assert resultado in [0, 1, 2]  # Piedra, Papel o Tijeras


def test_estrategia_basada_en_tendencias_movimientos_recientes():
    """
    La estrategia debe basarse en los 10 movimientos más frecuentes de las últimas 10 partidas.
    
    En movimientos sale 6 veces 'Tijeras', 3 veces 'Piedra' y 5 veces 'Papel', 
    pero si solo tenemos en cuenta los ultimos 10, 'Tijera' solo aparece 2 veces, por lo tanto el más frecuente debería ser Papel
    """
    movimientos = ["Tijeras", "Tijeras", "Tijeras", "Tijeras", "Piedra", "Papel", "Papel", "Tijeras", "Papel", "Papel", "Piedra", "Tijeras", "Papel", "Piedra"]
    resultado = estrategia_basada_en_tendencias(movimientos)
    assert resultado == GameAction.Tijeras.value  # Contraataca "Papel", el más frecuente


def test_estrategia_combinada_patron_repetido():
    """
    Detectar el patrón de tres movimientos repetidos y devolver el contraataque.
    """
    movimientos = ["Piedra", "Piedra", "Piedra"]
    resultado = estrategia_combinada(movimientos)
    assert resultado == GameAction.Papel.value  # Contraataca "Piedra"


def test_estrategia_combinada_secuencia_rps():
    """
    Detectar la secuencia "Piedra, Papel, Tijeras" y devolver el contraataque.
    """
    movimientos = ["Piedra", "Papel", "Tijeras"]
    resultado = estrategia_combinada(movimientos)
    assert resultado == GameAction.Papel.value  # Contraataca "Piedra", el siguiente esperado


def test_analizar_rendimiento_derrotas_recientes():
    """
    Si la computadora ha perdido al menos 2 de las últimas 3 rondas, devolver True.
    """
    historial = pd.DataFrame({
        "Resultado": ["Victoria", "Derrota", "Derrota", "Victoria", "Victoria"]
    })
    resultado = analizar_rendimiento(historial)
    assert resultado == True


def test_analizar_rendimiento_sin_derrotas():
    """
    Si la computadora no ha perdido al menos 2 de las últimas 3 rondas, devolver False.
    """
    historial = pd.DataFrame({
        "Resultado": ["Victoria", "Empate", "Derrota", "Empate", "Victoria"]
    })
    resultado = analizar_rendimiento(historial)
    assert resultado == False
