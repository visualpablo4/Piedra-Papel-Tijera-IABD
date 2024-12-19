#import pytest
import sys
import os

from main import GameAction, GameResult, assess_game

# Tenía un problema al ejecutar pytest y no conseguía solucionarlo, pidiendo ayuda a chatGPT ya que no era capaz de solucionarlo, 
# al meterle esta línea y luego instalar un paquete en el entorno virtual se fueron los errores.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


def test_Empate():
    """
    Partidas con empate
    """
    assert GameResult.Tie == assess_game(
        user_action = GameAction.Papel,
        computer_action = GameAction.Papel
    )

    assert GameResult.Tie == assess_game(
        user_action = GameAction.Papel,
        computer_action = GameAction.Papel
    )

    assert GameResult.Tie == assess_game(
        user_action = GameAction.Papel,
        computer_action = GameAction.Papel
    )


def test_Piedra_loses():
    '''
    Piedra pierde con Papel
    '''
    assert GameResult.Victory == assess_game(
        user_action=GameAction.Papel,
        computer_action=GameAction.Piedra)


def test_Piedra_wins():
    '''
    Piedra gana a Tijeras
    '''
    assert GameResult.Defeat == assess_game(
        user_action=GameAction.Tijeras,
        computer_action=GameAction.Piedra)


def test_Papel_loses():
    '''
    Papel pierde con Tijeras
    '''
    assert GameResult.Victory == assess_game(
        user_action=GameAction.Tijeras,
        computer_action=GameAction.Papel)


def test_Papel_wins():
    '''
    Papel gana a Piedra
    '''
    assert GameResult.Defeat == assess_game(
        user_action=GameAction.Piedra,
        computer_action=GameAction.Papel)


def test_Tijeras_loses():
    '''
    Tijeras pierde con Piedra 
    '''
    assert GameResult.Victory == assess_game(
        user_action=GameAction.Piedra,
        computer_action=GameAction.Tijeras)


def test_Tijeras_wins():
    '''
    Tijeras gana a Papel 
    '''
    assert GameResult.Defeat == assess_game(
        user_action=GameAction.Papel,
        computer_action=GameAction.Tijeras)