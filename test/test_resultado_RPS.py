#import pytest
import sys
import os

from src.RPSLS import GameAction, GameResult, assess_game

# Tenía un problema al ejecutar pytest y no conseguía solucionarlo, pidiendo ayuda a chatGPT ya que no era capaz de solucionarlo, 
# al meterle esta línea y luego instalar un paquete en el entorno virtual se fueron los errores.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


def test_Empate():
    """
    Partidas con empate
    """
    assert GameResult.Tie == assess_game(
        user_action = GameAction.Papel,
        computer_action = GameAction.Papel)

    assert GameResult.Tie == assess_game(
        user_action = GameAction.Papel,
        computer_action = GameAction.Papel)

    assert GameResult.Tie == assess_game(
        user_action = GameAction.Papel,
        computer_action = GameAction.Papel)


def test_Piedra_loses():
    '''
    Piedra pierde con Papel y Spock
    '''
    assert GameResult.Victory == assess_game(
        user_action=GameAction.Papel,
        computer_action=GameAction.Piedra)
    
    assert GameResult.Defeat == assess_game(
        user_action=GameAction.Piedra,
        computer_action=GameAction.Spock)


def test_Piedra_wins():
    '''
    Piedra gana a Tijeras y Lagarto
    '''
    assert GameResult.Defeat == assess_game(
        user_action=GameAction.Tijeras,
        computer_action=GameAction.Piedra)
    
    assert GameResult.Victory == assess_game(
        user_action=GameAction.Piedra,
        computer_action=GameAction.Lagarto)


def test_Papel_loses():
    '''
    Papel pierde con Tijeras y Lagarto
    '''
    assert GameResult.Victory == assess_game(
        user_action=GameAction.Tijeras,
        computer_action=GameAction.Papel)
    
    assert GameResult.Defeat == assess_game(
        user_action=GameAction.Papel,
        computer_action=GameAction.Lagarto)


def test_Papel_wins():
    '''
    Papel gana a Piedra y Spock
    '''
    assert GameResult.Defeat == assess_game(
        user_action=GameAction.Piedra,
        computer_action=GameAction.Papel)
    
    assert GameResult.Victory == assess_game(
        user_action=GameAction.Papel,
        computer_action=GameAction.Spock)


def test_Tijeras_loses():
    '''
    Tijeras pierde con Piedra y Spock
    '''
    assert GameResult.Victory == assess_game(
        user_action=GameAction.Piedra,
        computer_action=GameAction.Tijeras)
    
    assert GameResult.Defeat == assess_game(
        user_action=GameAction.Tijeras,
        computer_action=GameAction.Spock)


def test_Tijeras_wins():
    '''
    Tijeras gana a Papel y Lagarto
    '''
    assert GameResult.Defeat == assess_game(
        user_action=GameAction.Papel,
        computer_action=GameAction.Tijeras)
    
    assert GameResult.Victory == assess_game(
        user_action=GameAction.Tijeras,
        computer_action=GameAction.Lagarto)
    
    
def test_Lagarto_wins():
    """
    Lagarto gana a Papel y Spock
    """
    assert GameResult.Victory == assess_game(
        user_action=GameAction.Lagarto,
        computer_action=GameAction.Papel)
    
    assert GameResult.Victory == assess_game(
        user_action=GameAction.Lagarto,
        computer_action=GameAction.Spock)
    

def test_Lagarto_loses():
    """
    Lagarto pierde con Piedra y Tijeras
    """
    assert GameResult.Defeat == assess_game(
        user_action=GameAction.Lagarto,
        computer_action=GameAction.Piedra)
    
    assert GameResult.Defeat == assess_game(
        user_action=GameAction.Lagarto,
        computer_action=GameAction.Tijeras)
    

def test_Spock_wins():
    """
    Spock gana a Piedra y Tijeras
    """
    assert GameResult.Victory == assess_game(
        user_action=GameAction.Spock,
        computer_action=GameAction.Piedra)
    
    assert GameResult.Victory == assess_game(
        user_action=GameAction.Spock,
        computer_action=GameAction.Tijeras)
    

def test_Spock_loses():
    """
    Spock pierde con Papel y Lagarto
    """
    assert GameResult.Defeat == assess_game(
        user_action=GameAction.Spock,
        computer_action=GameAction.Papel)
    
    assert GameResult.Defeat == assess_game(
        user_action=GameAction.Spock,
        computer_action=GameAction.Lagarto)
    