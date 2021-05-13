# -*- coding: utf8 -*-

__author__ = 'Suilan Estévez Velarde'

from tools import oo
from game_logic import *

def minimax(game, player, depth, h, moves):
    """Retorna el mejor tablero para el jugador
    correspondiente
    """
    best, value = maxplay(game, None, player, depth, h, moves)
    return best

def maxplay(game, play, player, depth, h, moves, alpha=-oo , beta=oo):
    """Retorna la mejor jugada tablero para el jugador"""
    best = None
    best_value = -oo

    if game.winner() != EMPTY:
        return play, -1
        #return play, 1 if game.winner() == player else -1

    if not depth:
        return play, h(game, player)

    for x,y in moves(game, player):
        b, value = minplay(game.clone_play(x,y), (x,y), player, depth - 1, h, moves)
        alpha = max(alpha, value)

        if alpha >= beta:
            break

        if value > best_value:
            best = (x,y)
            best_value = value
        
    return best, best_value

def minplay(game, play, player, depth, h, moves, alpha=-oo , beta=oo):
    """Retorna la mejor jugada para el jugador contrario"""
    best = None
    best_value = oo

    if game.winner() != EMPTY:
        return play, 1
        #return play, 1 if game.winner() == player else -1

    if not depth:
        return play, h(game, player)

    for x,y in moves(game, player):
        _, value = maxplay(game.clone_play(x,y), (x,y), player, depth - 1, h, moves)
        beta = min(beta, value)

        if beta <= alpha:
            break
    
        if value < best_value:
            best = (x,y)
            best_value = value

    return best, best_value